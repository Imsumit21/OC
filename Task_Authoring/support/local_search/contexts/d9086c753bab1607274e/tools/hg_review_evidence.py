"""Check exact evidence anchors. Presence is not proof of authority or truth."""

import hashlib
import json
from pathlib import Path


class EvidenceReader:
    def __init__(self, root):
        self.root = Path(root)
        self.files = {}

    def quote(self, anchor):
        if not isinstance(anchor, dict):
            raise ValueError("Evidence anchor must be an object")
        for key in ("path", "sha256", "quote"):
            if not isinstance(anchor.get(key), str) or not anchor[key].strip():
                raise ValueError("Evidence anchor needs " + key)
        path = (self.root / anchor["path"]).resolve()
        if path not in self.files:
            raw = path.read_bytes()
            self.files[path] = (hashlib.sha256(raw).hexdigest(), raw.decode("utf-8-sig"))
        sha, text = self.files[path]
        if sha != anchor["sha256"]:
            raise ValueError("Missing/changed evidence source: " + anchor["path"])
        if "line_start" in anchor or "line_end" in anchor:
            first, last = anchor.get("line_start"), anchor.get("line_end")
            lines = text.splitlines(keepends=True)
            if ("pointer" in anchor or type(first) is not int or type(last) is not int or
                    not 1 <= first <= last <= len(lines)):
                raise ValueError("Evidence lines need a valid inclusive range; do not combine with pointer")
            text = "".join(lines[first-1:last])
        if "pointer" in anchor:
            pointer = anchor["pointer"]
            if not isinstance(pointer, str) or (pointer and not pointer.startswith("/")):
                raise ValueError("Evidence pointer must be an RFC 6901 JSON pointer")
            value = json.loads(text)
            try:
                for token in pointer.split("/")[1:] if pointer else []:
                    token = token.replace("~1", "/").replace("~0", "~")
                    if isinstance(value, list):
                        if not token.isdigit() or (len(token) > 1 and token[0] == "0"):
                            raise ValueError("Invalid array index")
                        value = value[int(token)]
                    else:
                        value = value[token]
            except (KeyError, IndexError, TypeError, ValueError) as error:
                raise ValueError("Evidence pointer does not resolve: " + pointer) from error
            text = value if isinstance(value, str) else json.dumps(value, ensure_ascii=False, sort_keys=True)
        if anchor["quote"] not in text:
            raise ValueError("Quoted evidence is absent from selected source: " + anchor["path"])
        return text


def sources(reader, entries):
    if not isinstance(entries, list):
        raise ValueError("sources must be an array")
    result = {}
    for item in entries:
        if not isinstance(item, dict) or not isinstance(item.get("id"), str) or not item["id"]:
            raise ValueError("Evidence source needs an ID")
        if item["id"] in result:
            raise ValueError("Duplicate evidence source ID")
        reader.quote(item)
        if item.get("visibility") not in {"VISIBLE", "INACCESSIBLE", "UNRESOLVED"}:
            raise ValueError("Source visibility needs VISIBLE, INACCESSIBLE or UNRESOLVED")
        if not isinstance(item.get("access"), str) or not item["access"].strip():
            raise ValueError("Source access needs persona/ACL evidence or a precise limitation")
        result[item["id"]] = item
    return result


def links(ids, known, label, nonempty=True):
    if (not isinstance(ids, list) or (nonempty and not ids) or
            any(not isinstance(i, str) or i not in known for i in ids) or len(ids) != len(set(ids))):
        raise ValueError(label + " needs unique, known source IDs")
    return [known[i] for i in ids]


def authority(ids, known, root, context):
    chain = links(ids, known, "authority_chain")
    inputs = context.get("inputs", {})
    prompt_paths = [f["path"] for k in ("prompt", "source:prompt")
                    for f in inputs.get(k, {}).get("files", [])]
    if not prompt_paths:
        prompt_paths = ["Evals/task_inputs/04_Prompt.txt"]
    if (Path(root) / chain[0]["path"]).resolve() not in {
            (Path(root) / p).resolve() for p in prompt_paths}:
        raise ValueError("Authority chain must begin with the actual saved prompt")
    for previous, current in zip(chain, chain[1:]):
        if current.get("incorporated_by") != previous["id"]:
            raise ValueError("Each incorporated instruction needs its preceding authority source ID")
        if not isinstance(current.get("incorporation_reason"), str) or not current["incorporation_reason"].strip():
            raise ValueError("Explain how the quoted passage incorporates the next instruction")
    return all(s["visibility"] == "VISIBLE" for s in chain)
