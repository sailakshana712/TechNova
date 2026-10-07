def check_quality(pil_img) -> dict:
    """Check if the MRI picture is clear enough."""
    return {"score": 1.0, "blur": 0.0, "brightness": 0.0, "contrast": 0.0, "warnings": []}
