import re

KW = {
    "glioma":     ["seizure", "headache", "confusion", "memory", "personality", "weakness", "speech", "nausea", "vomiting"],
    "meningioma": ["headache", "vision", "visual", "seizure", "hearing", "smell", "weakness", "numbness"],
    "pituitary":  ["visual field", "vision", "hormone", "prolactin", "amenorrh", "galactorrh", "acromegal", "cushing", "fatigue", "double vision"],
}
RED = sorted({k for v in KW.values() for k in v})

def extract(note, cls):
    out = []
    for s in re.split(r"(?<=[.;\n])\s*", note):
        for k in KW.get(cls, []):
            if k in s.lower():
                out.append({"quote": s.strip(), "keyword": k})
                break
    return [o for o in out if o["quote"] in note]

def red_flags(note):
    return [k for k in RED if k in note.lower()]