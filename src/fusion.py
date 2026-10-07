def build_report(pil_img, note_text: str) -> dict:
    """Mix the picture result and the notes result into one report."""
    return {"quality": {}, "findings": [], "disclaimer": "Doctor-assist tool, not a diagnosis."}
