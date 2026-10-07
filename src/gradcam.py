import numpy as np

def explain(pil_img, cls: str) -> dict:
    """STUB: fake heatmap and box (224x224 space)."""
    return {
        "overlay": np.zeros((224, 224, 3), dtype=np.uint8),
        "box": [60, 50, 150, 140],
        "area_frac": 0.2,
        "contour": None,
    }