def combine(image_result: dict, notes_result: dict) -> dict:
    """Mix the image answer and the notes answer together."""
    return {"image": image_result, "notes": notes_result}
