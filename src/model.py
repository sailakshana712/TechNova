CLASSES = ["glioma", "meningioma", "notumor", "pituitary"]

def predict(pil_img) -> dict:
    """STUB: fake answer. Real model comes later."""
    return {"glioma": 0.05, "meningioma": 0.86, "notumor": 0.04, "pituitary": 0.05}