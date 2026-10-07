import numpy as np
from src import model, gradcam, quality, notes

TUMOURS = ["glioma", "meningioma", "pituitary"]

def band(c): return "High" if c >= 0.75 else "Moderate" if c >= 0.40 else "Low"

def build_report(img, note_text):
    q = quality.check_quality(img)
    probs = model.predict(img)
    findings = []
    for cls in TUMOURS:
        p = probs[cls]
        if p < 0.15:                      # model sees nothing, skip
            continue
        g = gradcam.explain(img, cls)
        quotes = notes.extract(note_text, cls)
        # region only counts if the heatmap is focused (not smeared over the whole image)
        region_ok = g["box"] is not None and g["area_frac"] < 0.5
        # EVIDENCE GATE
        if not region_ok and not quotes:
            continue
        conf = p * (0.7 + 0.3 * q["score"])               # poor image lowers confidence
        conf = min(conf + 0.04 * min(len(quotes), 3), 0.97) if p >= 0.4 else conf  # notes help a little, never rescue a weak image score
        findings.append({"condition": cls, "confidence": round(conf, 2), "band": band(conf),
                         "region": g if region_ok else None,
                         "note_evidence": [x["quote"] for x in quotes]})
    findings.sort(key=lambda f: -f["confidence"])
    mismatch = None
    if probs["notumor"] > 0.6 and notes.red_flags(note_text):
        mismatch = "Image shows no clear tumour, but notes contain concerning symptoms. Clinical correlation advised."
    return {"quality": q, "probs": probs, "findings": findings, "mismatch": mismatch,
            "disclaimer": "Decision-support only. Not a diagnosis. Confirm with radiologist review."}