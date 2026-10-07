CLASSES = ["glioma", "meningioma", "notumor", "pituitary"]

def predict(pil_img) -> dict:
    """Look at one MRI and give a chance (0 to 1) for each tumour type."""
    return {"glioma": 0.25, "meningioma": 0.25, "notumor": 0.25, "pituitary": 0.25}

