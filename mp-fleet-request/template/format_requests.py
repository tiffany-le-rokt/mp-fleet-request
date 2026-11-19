import json, re, sys
LABELS = {"Customer context", "How it works today", "Proposed direction", "Data mapping", "Out of scope",
          "Guardrails", "Success signals", "Deliverables"}
PREFIXES = ("Type:", "Platform area:", "The ask:", "Business impact:", "Expected vs actual:",
            "How to reproduce:", "Reach and workaround:", "Existing customers:", "Backward compatibility:",
            "Confident:", "To confirm:", "Partner docs:")
u16 = lambda s: len(s.encode("utf-16-le")) // 2
pt = lambda n: {"magnitude": n, "unit": "PT"}
raw = json.load(open(sys.argv[1]))
if isinstance(raw, list): raw = json.loads(raw[0]["text"])
doc = raw.get("content", raw)
tab = doc["tabs"][0]["documentTab"] if "tabs" in doc else doc
bullets, labels, bold = [], [], []
for el in tab["body"]["content"]:
    p = el.get("paragraph")
    if not p or p["paragraphStyle"].get("namedStyleType") != "NORMAL_TEXT": continue
    s, e = el["startIndex"], el["endIndex"]
    text = "".join(x.get("textRun", {}).get("content", "") for x in p["elements"]).rstrip("\n")
    off, body = 0, text
    if text.startswith("•"):
        if bullets and bullets[-1][1] == s: bullets[-1][1] = e
        else: bullets.append([s, e])
        m = re.match(r"•\s+", text); off, body = u16(m.group(0)), text[len(m.group(0)):]
    if text in LABELS:
        labels.append([s, e]); bold.append((s, s + u16(text))); continue
    for pre in PREFIXES:
        if body.startswith(pre): bold.append((s + off, s + off + u16(pre))); break
reqs = [{"updateParagraphStyle": {"range": {"startIndex": a, "endIndex": b},
         "paragraphStyle": {"indentStart": pt(22), "indentFirstLine": pt(10), "spaceBelow": pt(2)},
         "fields": "indentStart,indentFirstLine,spaceBelow"}} for a, b in bullets]
reqs += [{"updateParagraphStyle": {"range": {"startIndex": a, "endIndex": b},
          "paragraphStyle": {"spaceAbove": pt(8), "spaceBelow": pt(2), "keepWithNext": True}, "fields": "spaceAbove,spaceBelow,keepWithNext"}}
         for a, b in labels]
reqs += [{"updateTextStyle": {"range": {"startIndex": a, "endIndex": b}, "textStyle": {"bold": True},
          "fields": "bold"}} for a, b in bold]
print(json.dumps({"revisionId": doc.get("revisionId"), "requests": reqs}, separators=(",", ":")))
