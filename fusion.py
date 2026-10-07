import numpy as np

def build_report(img, note_text):
    """FAKE version. Returns made-up data in the agreed format."""
    # Make a fake heatmap picture: grey square with a red area and a green box
    overlay = np.full((224, 224, 3), 100, dtype=np.uint8)
    overlay[60:140, 70:150] = [220, 60, 60]
    overlay[60:63, 70:150] = [0, 255, 0]
    overlay[137:140, 70:150] = [0, 255, 0]
    overlay[60:140, 70:73] = [0, 255, 0]
    overlay[60:140, 147:150] = [0, 255, 0]

    quotes = []
    if "headache" in note_text.lower():
        quotes = ["progressive headaches"]

    return {
        "quality": {"score": 0.9, "blur": 120.0, "brightness": 90.0,
                    "contrast": 50.0, "warnings": []},
        "probs": {"glioma": 0.05, "meningioma": 0.86, "notumor": 0.05, "pituitary": 0.04},
        "findings": [
            {"condition": "meningioma", "confidence": 0.86, "band": "High",
             "region": {"overlay": overlay, "box": [70, 60, 150, 140], "area_frac": 0.12},
             "note_evidence": quotes},
        ],
        "mismatch": None,
        "disclaimer": "Decision-support only. Not a diagnosis. Confirm with radiologist review.",
    }