import cv2
import numpy as np

# Temporary numbers. We will replace them in Step 3 after measuring.
BLUR_T = 442.1
DARK_T = 26.8
BRIGHT_T = 80.5
CONTRAST_T = 34.3

def check_quality(pil_img):
    g = np.array(pil_img.convert("L").resize((224, 224)))
    blur = cv2.Laplacian(g, cv2.CV_64F).var()
    br = float(g.mean())
    ct = float(g.std())
    warn, score = [], 1.0
    if blur < BLUR_T:
        warn.append("Image appears blurry")
        score -= 0.35
    if br < DARK_T:
        warn.append("Image appears too dark")
        score -= 0.25
    if br > BRIGHT_T:
        warn.append("Image appears overexposed")
        score -= 0.25
    if ct < CONTRAST_T:
        warn.append("Low contrast")
        score -= 0.25
    return {"score": max(score, 0.1), "blur": blur, "brightness": br,
            "contrast": ct, "warnings": warn}