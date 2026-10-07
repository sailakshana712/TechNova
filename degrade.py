import cv2
import glob
import os
import numpy as np

os.makedirs("data/degraded", exist_ok=True)

for path in glob.glob("data/normal/*"):
    img = cv2.imread(path)
    if img is None:
        continue
    name = os.path.splitext(os.path.basename(path))[0]
    m = img.mean()
    versions = {
        "blur":   cv2.GaussianBlur(img, (0, 0), 4),
        "dark":   np.clip(img * 0.35, 0, 255),
        "bright": np.clip(img * 1.8 + 40, 0, 255),
        "lowcon": np.clip((img - m) * 0.25 + m, 0, 255),
        "noise":  np.clip(img + np.random.normal(0, 40, img.shape), 0, 255),
    }
    for kind, v in versions.items():
        cv2.imwrite(f"data/degraded/{name}_{kind}.png", v.astype(np.uint8))

print("done")