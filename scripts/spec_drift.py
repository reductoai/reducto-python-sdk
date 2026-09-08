#!/usr/bin/env -S uv run python
"""Report drift between the SDK types and the Reducto OpenAPI spec.

Schema names in the spec do not match SDK type names, so nothing is matched by
name. Each SDK request/response type is anchored to an endpoint discovered from
`src/reducto/resources/*.py`, then both sides are normalized into one shape model
and walked in parallel, comparing JSON property names, types, enum values, and
required-ness.

`spec/drift-allowlist.json` lists known, intentional deviations with a reason.
Matching items are reported as allowed and do not fail the check. Entries that
match nothing are flagged as stale.

The check runs against the committed snapshot `spec/openapi.json` by default, so
it is reproducible and needs no network. `--live` checks against the public URL.
`--update-snapshot` fetches the live spec, rewrites the snapshot, then checks.
Refreshing the snapshot is a manual step; commit it together with the SDK sync.

Usage:
    uv run python scripts/spec_drift.py [--spec URL|PATH | --live] [--update-snapshot] [--json] [--warn-only]
"""

from __future__ import annotations

import ast
import sys
import json
import types
import typing
import argparse
import datetime
import importlib
import urllib.request
import collections.abc
import typing_extensions
from typing import Any, Dict, List, Tuple, Union, Literal, Optional
from pathlib import Path
from dataclasses import field, asdict, replace, dataclass
from typing_extensions import Required, Annotated, NotRequired, get_args, get_origin, is_typeddict

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "src"))

from reducto._types import FileTypes, SequenceNotStr  # noqa: E402
from reducto._utils import PropertyInfo  # noqa: E402
from reducto._models import BaseModel  # noqa: E402

LIVE_SPEC = "https://reducto.ai/openapi.json"
SNAPSHOT = REPO / "spec" / "openapi.json"
ALLOWLIST = REPO / "spec" / "drift-allowlist.json"
HTTP_VERBS = ("get", "post", "put", "patch", "delete")
HTTP_METHODS = {name: verb for verb in HTTP_VERBS for name in (verb, "_" + verb)}
SUCCESS_CODES = ("200", "201", "202")
SIMILARITY_DEPTH = 2

JsonDict = Dict[str, Any]


# Shape model


@dataclass
class Shape:
    kind: Literal["object", "enum", "primitive", "array", "map", "union", "any"]
    type: str = ""
    props: Dict[str, Shape] = field(default_factory=lambda: {})
    required: typing.Set[str] = field(default_factory=lambda: set())
    values: typing.Set[Any] = field(default_factory=lambda: set())
    items: Optional[Shape] = None
    members: List[Shape] = field(default_factory=lambda: [])
    label: str = ""
    has_default: bool = False


ANY = Shape("any")
NULL = Shape("primitive", type="null")


def prim(t: str) -> Shape:
    return Shape("primitive", type=t)


def union(members: List[Shape]) -> Shape:
    flat: List[Shape] = []
    for m in members:
        flat.extend(m.members if m.kind == "union" else [m])
    dedup: List[Shape] = []
    for m in flat:
        if not any(same_signature(m, d) for d in dedup):
            dedup.append(m)
    return dedup[0] if len(dedup) == 1 else Shape("union", members=dedup)


def same_signature(a: Shape, b: Shape) -> bool:
    if a.kind != b.kind:
        return False
    if a.kind == "primitive":
        return a.type == b.type
    if a.kind == "object":
        return set(a.props) == set(b.props) and all(same_signature(a.props[k], b.props[k]) for k in a.props)
    if a.kind == "enum":
        return a.values == b.values
    if a.kind in ("array", "map"):
        return a.items is not None and b.items is not None and same_signature(a.items, b.items)
    if a.kind == "union":
        return len(a.members) == len(b.members) and all(any(same_signature(x, y) for y in b.members) for x in a.members)
    return True


# Spec side


class Spec:
    def __init__(self, doc: JsonDict) -> None:
        self.doc = doc
        self.schemas: JsonDict = doc.get("components", {}).get("schemas", {})
        self.version: str = str(doc.get("info", {}).get("version", "unknown"))

    def resolve(self, node: JsonDict) -> JsonDict:
        while "$ref" in node:
            name = node["$ref"].rsplit("/", 1)[-1]
            node = self.schemas[name]
        return node

    def shape(self, node: JsonDict, seen: typing.FrozenSet[str] = frozenset()) -> Shape:
        shape = self.shape_of(node, seen)
        if "default" in node and not shape.has_default:
            shape = replace(shape, has_default=True)
        return shape

    def shape_of(self, node: JsonDict, seen: typing.FrozenSet[str]) -> Shape:
        label = ""
        if "$ref" in node:
            label = node["$ref"].rsplit("/", 1)[-1]
            if label in seen:
                return Shape("any", label=label)
            seen = seen | {label}
            node = self.resolve(node)

        variants = node.get("anyOf") or node.get("oneOf")
        if variants:
            return union([self.shape(v, seen) for v in variants])
        if "allOf" in node:
            merged: JsonDict = {"type": "object", "properties": {}, "required": []}
            for part in node["allOf"]:
                part = self.resolve(part)
                merged["properties"].update(part.get("properties", {}))
                merged["required"].extend(part.get("required", []))
            node = merged

        if "const" in node:
            return Shape("enum", values={node["const"]}, label=label)
        if "enum" in node:
            return Shape("enum", values=set(node["enum"]), label=label)

        t = node.get("type")
        if isinstance(t, list):
            variants_by_type = typing.cast(List[str], t)
            return union([self.shape({**node, "type": x}, seen) for x in variants_by_type])
        if t == "array":
            return Shape("array", items=self.shape(node.get("items", {}), seen), label=label)
        if t == "object" or "properties" in node:
            if "properties" in node:
                props = {k: self.shape(v, seen) for k, v in node["properties"].items()}
                return Shape("object", props=props, required=set(node.get("required", [])), label=label)
            extra = node.get("additionalProperties")
            if isinstance(extra, dict):
                return Shape("map", items=self.shape(typing.cast(JsonDict, extra), seen), label=label)
            return Shape("map", items=ANY, label=label)
        if t == "string" and node.get("format") == "binary":
            return prim("file")
        if t in ("string", "integer", "number", "boolean", "null"):
            return prim(t)
        return Shape("any", label=label)

    def operation(self, method: str, path: str) -> Optional[JsonDict]:
        op = self.doc.get("paths", {}).get(path, {}).get(method)
        return typing.cast(Optional[JsonDict], op)

    def request_body(self, op: JsonDict) -> Optional[Shape]:
        content = op.get("requestBody", {}).get("content", {})
        for ct in ("application/json", "multipart/form-data", "application/x-www-form-urlencoded"):
            if ct in content:
                return self.shape(content[ct]["schema"])
        return None

    def query(self, op: JsonDict) -> Optional[Shape]:
        params = [p for p in op.get("parameters", []) if p.get("in") == "query"]
        if not params:
            return None
        props = {p["name"]: self.shape(p.get("schema", {})) for p in params}
        required = {p["name"] for p in params if p.get("required")}
        return Shape("object", props=props, required=required)

    def response(self, op: JsonDict) -> Optional[Shape]:
        for code in SUCCESS_CODES:
            content = op.get("responses", {}).get(code, {}).get("content", {})
            if "application/json" in content:
                return self.shape(content["application/json"]["schema"])
        return None

    def endpoints(self) -> typing.Set[typing.Tuple[str, str]]:
        out: typing.Set[typing.Tuple[str, str]] = set()
        for path, ops in self.doc.get("paths", {}).items():
            for method in ops:
                if method in HTTP_METHODS.values():
                    out.add((method, path))
        return out


# SDK side


PRIMITIVES: Dict[Any, str] = {
    str: "string",
    int: "integer",
    float: "number",
    bool: "boolean",
    type(None): "null",
    datetime.datetime: "string",
    datetime.date: "string",
}


LITERAL_ORIGINS = {Literal, typing_extensions.Literal}
WRAPPER_ORIGINS = {Annotated, Required, NotRequired}
ARRAY_ORIGINS = {
    list,
    tuple,
    set,
    frozenset,
    collections.abc.Sequence,
    collections.abc.Iterable,
    collections.abc.Collection,
    SequenceNotStr,
}
MAP_ORIGINS = {dict, collections.abc.Mapping, collections.abc.MutableMapping}


UNION_TYPE: Any = getattr(types, "UnionType", None)


def is_union(origin: Any) -> bool:
    return origin is Union or (UNION_TYPE is not None and origin is UNION_TYPE)


def sdk_shape(tp: Any, seen: typing.FrozenSet[Any] = frozenset()) -> Shape:
    origin = get_origin(tp)
    args = get_args(tp)

    if origin in WRAPPER_ORIGINS:
        return sdk_shape(args[0], seen)
    if tp is Any or tp is object:
        return ANY
    if tp in PRIMITIVES:
        return prim(PRIMITIVES[tp])
    if tp is FileTypes or tp in get_args(FileTypes):
        return prim("file")
    if origin in LITERAL_ORIGINS:
        return Shape("enum", values=set(args))
    if is_union(origin):
        return union([sdk_shape(a, seen) for a in args])
    if origin in ARRAY_ORIGINS:
        return Shape("array", items=sdk_shape(args[0], seen) if args else ANY)
    if origin in MAP_ORIGINS:
        return Shape("map", items=sdk_shape(args[1], seen) if len(args) > 1 else ANY)

    if isinstance(tp, type):
        if tp in seen:
            return Shape("any", label=tp.__name__)
        if is_typeddict(tp):
            return typeddict_shape(tp, seen | {tp})
        if issubclass(tp, BaseModel):
            return model_shape(tp, seen | {tp})
        if tp.__name__ == "SequenceNotStr":
            return Shape("array", items=ANY)

    return Shape("any", label=f"{tp}")


def unwrap_field(hint: Any, default_required: bool) -> Tuple[Any, Optional[str], bool]:
    alias: Optional[str] = None
    required = default_required
    while get_origin(hint) in WRAPPER_ORIGINS:
        origin = get_origin(hint)
        args = get_args(hint)
        if origin is Required:
            required = True
        elif origin is NotRequired:
            required = False
        else:
            for meta in args[1:]:
                if isinstance(meta, PropertyInfo) and meta.alias:
                    alias = meta.alias
        hint = args[0]
    return hint, alias, required


def typeddict_shape(td: Any, seen: typing.FrozenSet[Any]) -> Shape:
    hints = typing_extensions.get_type_hints(td, include_extras=True)
    total = bool(getattr(td, "__total__", True))
    props: Dict[str, Shape] = {}
    required: typing.Set[str] = set()
    for name, hint in hints.items():
        inner, alias, is_required = unwrap_field(hint, total)
        wire = alias or name
        props[wire] = sdk_shape(inner, seen)
        if is_required:
            required.add(wire)
    return Shape("object", props=props, required=required, label=td.__name__)


def model_shape(model: Any, seen: typing.FrozenSet[Any]) -> Shape:
    props: Dict[str, Shape] = {}
    required: typing.Set[str] = set()
    fields = getattr(model, "model_fields", None) or getattr(model, "__fields__", {})
    for name, f in fields.items():
        wire = getattr(f, "alias", None) or name
        annotation = getattr(f, "annotation", None) or getattr(f, "outer_type_", Any)
        props[wire] = sdk_shape(annotation, seen)
        is_required = f.is_required() if hasattr(f, "is_required") else bool(getattr(f, "required", False))
        if is_required:
            required.add(wire)
    return Shape("object", props=props, required=required, label=model.__name__)


# Endpoint discovery


@dataclass
class Endpoint:
    method: str
    path: str
    source: str
    body: Any = None
    query: Any = None
    response: Any = None


def literal_path(node: ast.AST) -> Optional[str]:
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "path_template":
        return literal_path(node.args[0]) if node.args else None
    if isinstance(node, ast.JoinedStr):
        parts: List[str] = []
        for v in node.values:
            if isinstance(v, ast.Constant):
                parts.append(str(v.value))
            elif isinstance(v, ast.FormattedValue) and isinstance(v.value, ast.Name):
                parts.append("{" + v.value.id + "}")
        return "".join(parts)
    return None


def resolve_expr(node: ast.AST, module: Any) -> Any:
    if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "cast":
        return resolve_expr(node.args[1], module)
    if isinstance(node, ast.Name):
        if node.id == "object":
            return object
        if node.id == "str":
            return str
        return getattr(module, node.id, None)
    if isinstance(node, ast.Attribute):
        base = resolve_expr(node.value, module)
        return getattr(base, node.attr, None) if base is not None else None
    return None


def transform_target(node: Optional[ast.AST], module: Any) -> Any:
    if (
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id
        in (
            "maybe_transform",
            "async_maybe_transform",
        )
    ):
        if len(node.args) >= 2:
            return resolve_expr(node.args[1], module)
    return None


def find_query(options: Optional[ast.AST], module: Any) -> Any:
    if isinstance(options, ast.Call):
        for kw in options.keywords:
            if kw.arg == "query":
                return transform_target(kw.value, module)
    return None


def discover_endpoints() -> List[Endpoint]:
    files = sorted((REPO / "src/reducto/resources").glob("*.py")) + [REPO / "src/reducto/_client.py"]
    found: Dict[typing.Tuple[str, str], Endpoint] = {}
    for file in files:
        rel = file.relative_to(REPO / "src").with_suffix("")
        module = importlib.import_module(".".join(rel.parts))
        tree = ast.parse(file.read_text())
        for node in ast.walk(tree):
            if not isinstance(node, ast.Call) or not isinstance(node.func, ast.Attribute):
                continue
            if node.func.attr not in HTTP_METHODS or not node.args:
                continue
            if not (isinstance(node.func.value, ast.Name) and node.func.value.id == "self"):
                continue
            if node.func.attr in HTTP_VERBS and not str(file).endswith("_client.py"):
                continue
            path = literal_path(node.args[0])
            if path is None:
                continue
            method = HTTP_METHODS[node.func.attr]
            key = (method, path)
            if key in found:
                continue
            kws = {kw.arg: kw.value for kw in node.keywords}
            found[key] = Endpoint(
                method=method,
                path=path,
                source=f"{file.relative_to(REPO)}:{node.lineno}",
                body=transform_target(kws.get("body"), module),
                query=find_query(kws.get("options"), module),
                response=resolve_expr(kws["cast_to"], module) if "cast_to" in kws else None,
            )
    return list(found.values())


# Comparison


@dataclass
class Drift:
    endpoint: str
    location: str
    kind: Literal["endpoint", "missing", "extra", "type", "enum", "required"]
    detail: str


DRIFT_KINDS = ("endpoint", "missing", "extra", "type", "enum", "required")


class Comparator:
    def __init__(self, endpoint: str, ignore_null: bool, seen_pairs: typing.Set[Tuple[str, str]]) -> None:
        self.endpoint = endpoint
        self.ignore_null = ignore_null
        self.seen_pairs = seen_pairs
        self.drifts: List[Drift] = []

    def report(self, loc: str, kind: Any, detail: str) -> None:
        self.drifts.append(Drift(self.endpoint, loc, kind, detail))

    def compare(self, spec: Shape, sdk: Shape, loc: str) -> None:
        if spec.kind == "any" or sdk.kind == "any":
            return
        if self.ignore_null:
            spec, sdk = strip_null(spec), strip_null(sdk)
        if spec.kind == "union" or sdk.kind == "union":
            self.compare_union(spec, sdk, loc)
            return
        if spec.kind == "object" and spec.label and sdk.label:
            pair = (spec.label, sdk.label)
            if pair in self.seen_pairs:
                return
            self.seen_pairs.add(pair)
        if spec.kind != sdk.kind:
            self.report(loc, "type", f"spec {describe(spec)}, sdk {describe(sdk)}")
            return
        if spec.kind == "primitive":
            if spec.type != sdk.type and not (spec.type == "number" and sdk.type == "integer"):
                self.report(loc, "type", f"spec {spec.type}, sdk {sdk.type}")
        elif spec.kind == "enum":
            missing = spec.values - sdk.values
            extra = sdk.values - spec.values
            if missing:
                self.report(loc, "enum", f"sdk lacks values {sorted(map(str, missing))}")
            if extra:
                self.report(loc, "enum", f"spec lacks values {sorted(map(str, extra))}")
        elif spec.kind in ("array", "map"):
            assert spec.items is not None and sdk.items is not None
            self.compare(spec.items, sdk.items, loc + ("[]" if spec.kind == "array" else "{}"))
        elif spec.kind == "object":
            self.compare_object(spec, sdk, loc)

    def compare_object(self, spec: Shape, sdk: Shape, loc: str) -> None:
        for name in sorted(set(spec.props) - set(sdk.props)):
            self.report(f"{loc}.{name}", "missing", f"spec has field, sdk lacks it ({describe(spec.props[name])})")
        for name in sorted(set(sdk.props) - set(spec.props)):
            self.report(f"{loc}.{name}", "extra", f"sdk has field, spec lacks it ({describe(sdk.props[name])})")
        for name in sorted(set(spec.props) & set(sdk.props)):
            child = f"{loc}.{name}"
            self.compare_required(spec, sdk, name, child)
            self.compare(spec.props[name], sdk.props[name], child)

    def compare_required(self, spec: Shape, sdk: Shape, name: str, loc: str) -> None:
        spec_req, sdk_req = name in spec.required, name in sdk.required
        if spec_req == sdk_req:
            return
        # Response models express nullable fields as Optional[...] = None, so
        # "required but nullable" in the spec is not drift there. A response
        # field with a server default is always present, so the sdk may
        # require it.
        if self.ignore_null and spec_req and is_nullable(spec.props[name]):
            return
        if self.ignore_null and sdk_req and spec.props[name].has_default:
            return
        self.report(loc, "required", f"spec {req_word(spec_req)}, sdk {req_word(sdk_req)}")

    def compare_union(self, spec: Shape, sdk: Shape, loc: str) -> None:
        spec_members = list(spec.members) if spec.kind == "union" else [spec]
        sdk_members = list(sdk.members) if sdk.kind == "union" else [sdk]
        for si, ki in assign_members(spec_members, sdk_members):
            sm = spec_members[si]
            self.compare(sm, sdk_members[ki], f"{loc}<{sm.label or si}>")
        matched_spec = {si for si, _ in assign_members(spec_members, sdk_members)}
        matched_sdk = {ki for _, ki in assign_members(spec_members, sdk_members)}
        for i, sm in enumerate(spec_members):
            if i not in matched_spec:
                self.report(loc, "missing", f"spec union member {describe(sm)} has no sdk counterpart")
        for i, km in enumerate(sdk_members):
            if i not in matched_sdk:
                self.report(loc, "extra", f"sdk union member {describe(km)} has no spec counterpart")


def req_word(required: bool) -> str:
    return "required" if required else "optional"


def strip_null(s: Shape) -> Shape:
    if s.kind != "union":
        return s
    rest = [m for m in s.members if not (m.kind == "primitive" and m.type == "null")]
    return union(rest) if rest else s


def is_nullable(s: Shape) -> bool:
    if s.kind == "primitive" and s.type == "null":
        return True
    return s.kind == "union" and any(is_nullable(m) for m in s.members)


def assign_members(spec_members: List[Shape], sdk_members: List[Shape]) -> List[Tuple[int, int]]:
    """Greedy one-to-one matching of union members by structural similarity."""
    scored: List[Tuple[float, int, int]] = []
    for si, sm in enumerate(spec_members):
        for ki, km in enumerate(sdk_members):
            score = similarity(sm, km, SIMILARITY_DEPTH)
            if score > 0:
                scored.append((score, si, ki))
    scored.sort(key=lambda t: (-t[0], t[1], t[2]))
    used_spec: typing.Set[int] = set()
    used_sdk: typing.Set[int] = set()
    pairs: List[Tuple[int, int]] = []
    for _, si, ki in scored:
        if si in used_spec or ki in used_sdk:
            continue
        used_spec.add(si)
        used_sdk.add(ki)
        pairs.append((si, ki))
    return sorted(pairs)


def similarity(a: Shape, b: Shape, depth: int) -> float:
    if a.kind == "any" or b.kind == "any":
        return 0.1
    if a.kind == "union" or b.kind == "union":
        am = a.members if a.kind == "union" else [a]
        bm = b.members if b.kind == "union" else [b]
        return max(similarity(x, y, depth) for x in am for y in bm)
    if a.kind != b.kind:
        return 0.0
    if a.kind == "primitive":
        return 1.0 if a.type == b.type else 0.0
    if a.kind == "enum":
        if not a.values or not b.values:
            return 0.5
        inter = len(a.values & b.values)
        return 0.5 + 0.5 * inter / len(a.values | b.values) if inter else 0.2
    if a.kind == "object":
        ak, bk = set(a.props), set(b.props)
        if not ak and not bk:
            return 1.0
        shared = ak & bk
        name_score = len(shared) / max(len(ak | bk), 1)
        if depth <= 0 or not shared:
            return 0.5 + 0.5 * name_score
        child_score = sum(similarity(a.props[k], b.props[k], depth - 1) for k in shared) / len(shared)
        return 0.5 + 0.3 * name_score + 0.2 * child_score
    if a.kind in ("array", "map"):
        assert a.items is not None and b.items is not None
        return 0.5 + 0.5 * similarity(a.items, b.items, depth)
    return 0.5


def describe(s: Shape) -> str:
    if s.kind == "primitive":
        return s.type
    if s.kind == "enum":
        return "enum" + str(sorted(map(str, s.values)))
    if s.kind == "object":
        return f"object{{{', '.join(sorted(s.props))}}}" if len(s.props) <= 6 else f"object({len(s.props)} fields)"
    if s.kind == "array":
        return f"array<{describe(s.items) if s.items else 'any'}>"
    if s.kind == "map":
        return f"map<{describe(s.items) if s.items else 'any'}>"
    if s.kind == "union":
        return " | ".join(describe(m) for m in s.members)
    return "any"


# Driver


def load_doc(source: str) -> JsonDict:
    if source.startswith(("http://", "https://")):
        with urllib.request.urlopen(source, timeout=30) as resp:
            return typing.cast(JsonDict, json.load(resp))
    return typing.cast(JsonDict, json.loads(Path(source).read_text()))


def write_snapshot(doc: JsonDict, path: Path) -> bool:
    text = json.dumps(doc, indent=2, ensure_ascii=False) + "\n"
    changed = not path.exists() or path.read_text() != text
    if changed:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)
    return changed


def spec_order(spec: Spec, endpoints: List[Endpoint]) -> List[Endpoint]:
    paths = list(spec.doc.get("paths", {}))
    rank = {p: i for i, p in enumerate(paths)}
    return sorted(endpoints, key=lambda e: (rank.get(e.path, len(paths)), e.path, e.method))


def merge_objects(a: Optional[Shape], b: Optional[Shape]) -> Optional[Shape]:
    if a is None or b is None:
        return a or b
    if a.kind != "object" or b.kind != "object":
        return a
    return Shape("object", props={**a.props, **b.props}, required=a.required | b.required, label=a.label)


def run(spec: Spec, endpoints: List[Endpoint]) -> List[Drift]:
    drifts: List[Drift] = []
    covered: typing.Set[Tuple[str, str]] = set()
    seen_pairs: typing.Set[Tuple[str, str]] = set()
    for ep in spec_order(spec, endpoints):
        label = f"{ep.method.upper()} {ep.path}"
        op = spec.operation(ep.method, ep.path)
        if op is None:
            drifts.append(Drift(label, "", "endpoint", f"sdk calls this endpoint ({ep.source}) but spec lacks it"))
            continue
        covered.add((ep.method, ep.path))

        pairs: List[Tuple[str, Optional[Shape], Any, bool]]
        if ep.body is not None and ep.body is ep.query:
            # One params type feeds both body and query (e.g. /upload).
            pairs = [("request", merge_objects(spec.request_body(op), spec.query(op)), ep.body, False)]
        else:
            pairs = [
                ("request", spec.request_body(op), ep.body, False),
                ("query", spec.query(op), ep.query, False),
            ]
        pairs.append(("response", spec.response(op), ep.response, True))
        for section, spec_shape, sdk_type, ignore_null in pairs:
            if spec_shape is None and sdk_type is None:
                continue
            if spec_shape is None:
                drifts.append(Drift(label, section, "extra", f"sdk sends {section} but spec defines none"))
                continue
            if sdk_type is None:
                if not (spec_shape.kind == "any" or (spec_shape.kind == "object" and not spec_shape.props)):
                    drifts.append(
                        Drift(
                            label,
                            section,
                            "missing",
                            f"spec defines {section} ({describe(spec_shape)}) but sdk has none",
                        )
                    )
                continue
            cmp = Comparator(label, ignore_null=ignore_null, seen_pairs=seen_pairs)
            cmp.compare(spec_shape, sdk_shape(sdk_type), section)
            drifts.extend(cmp.drifts)

    for method, path in sorted(spec.endpoints() - covered):
        drifts.append(
            Drift(f"{method.upper()} {path}", "", "endpoint", "spec defines this endpoint but sdk has no method for it")
        )
    return drifts


def display(source: str) -> str:
    path = Path(source)
    if path.is_absolute() and REPO in path.parents:
        return str(path.relative_to(REPO))
    return source


@dataclass
class Allowed:
    endpoint: str
    location: str
    kind: str
    reason: str
    detail: Optional[str] = None

    def matches(self, d: Drift) -> bool:
        if (self.endpoint, self.location, self.kind) != (d.endpoint, d.location, d.kind):
            return False
        return self.detail is None or self.detail == d.detail


def load_allowlist(path: Path) -> List[Allowed]:
    if not path.exists():
        return []
    entries = typing.cast(List[JsonDict], json.loads(path.read_text()))
    return [Allowed(**e) for e in entries]


def split_allowed(drifts: List[Drift], allowlist: List[Allowed]) -> Tuple[List[Drift], List[Drift], List[Allowed]]:
    active: List[Drift] = []
    allowed: List[Drift] = []
    used: typing.Set[int] = set()
    for d in drifts:
        hit = next((i for i, a in enumerate(allowlist) if a.matches(d)), None)
        if hit is None:
            active.append(d)
        else:
            allowed.append(d)
            used.add(hit)
    stale = [a for i, a in enumerate(allowlist) if i not in used]
    return active, allowed, stale


def print_report(
    drifts: List[Drift],
    allowed: List[Drift],
    stale: List[Allowed],
    endpoints: List[Endpoint],
    spec: Spec,
    source: str,
) -> None:
    print(f"Spec: {display(source)} (version {spec.version})")
    print(f"Checked {len(endpoints)} sdk endpoints.")
    if allowed:
        print(f"{len(allowed)} allowed drift item(s), see {ALLOWLIST.relative_to(REPO)}:")
        for d in allowed:
            loc = f" {d.location}" if d.location else ""
            print(f"  {d.endpoint} [{d.kind}]{loc}: {d.detail}")
    for a in stale:
        print(f"Stale allowlist entry matches nothing: {a.endpoint} [{a.kind}] {a.location}", file=sys.stderr)
    if not drifts:
        print("No drift found.")
        return
    by_endpoint: Dict[str, List[Drift]] = {}
    for d in drifts:
        by_endpoint.setdefault(d.endpoint, []).append(d)
    for endpoint, items in by_endpoint.items():
        print(f"\n{endpoint}")
        for d in items:
            loc = f" {d.location}" if d.location else ""
            print(f"  [{d.kind}]{loc}: {d.detail}")
    counts: Dict[str, int] = {}
    for d in drifts:
        counts[d.kind] = counts.get(d.kind, 0) + 1
    summary = ", ".join(f"{k}={v}" for k, v in sorted(counts.items()))
    print(f"\n{len(drifts)} drift item(s): {summary}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    spec_group = parser.add_mutually_exclusive_group()
    spec_group.add_argument("--spec", default=str(SNAPSHOT), help="OpenAPI spec URL or file path (default: snapshot)")
    spec_group.add_argument("--live", action="store_true", help=f"check against {LIVE_SPEC}")
    parser.add_argument(
        "--update-snapshot",
        action="store_true",
        help="fetch the live spec, rewrite spec/openapi.json, then check against it",
    )
    parser.add_argument("--json", action="store_true", help="emit JSON instead of text")
    parser.add_argument("--warn-only", action="store_true", help="exit 0 even when drift is found")
    parser.add_argument(
        "--ignore",
        action="append",
        default=[],
        metavar="KIND",
        choices=DRIFT_KINDS,
        help=f"drift kind to ignore ({', '.join(DRIFT_KINDS)}); repeatable",
    )
    args = parser.parse_args()

    source: str = LIVE_SPEC if args.live else args.spec
    if args.update_snapshot:
        doc = load_doc(LIVE_SPEC)
        changed = write_snapshot(doc, SNAPSHOT)
        state = "updated" if changed else "unchanged"
        print(f"Snapshot {display(str(SNAPSHOT))} {state} (version {Spec(doc).version})", file=sys.stderr)
        source = str(SNAPSHOT)

    spec = Spec(load_doc(source))
    endpoints = discover_endpoints()
    found = [d for d in run(spec, endpoints) if d.kind not in args.ignore]
    drifts, allowed, stale = split_allowed(found, load_allowlist(ALLOWLIST))

    if args.json:
        payload = {
            "spec": source,
            "spec_version": spec.version,
            "drifts": [asdict(d) for d in drifts],
            "allowed": [asdict(d) for d in allowed],
        }
        print(json.dumps(payload, indent=2))
    else:
        print_report(drifts, allowed, stale, endpoints, spec, source)
    return 0 if not drifts or args.warn_only else 1


if __name__ == "__main__":
    sys.exit(main())
