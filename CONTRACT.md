# CONTRACT

This file says what each function takes IN and gives OUT.
Everyone must follow this so our code fits together.

- model.predict(image_path) -> {"label": str, "confidence": float}
- gradcam.make_heatmap(image_path) -> str  (path to the heatmap picture)
- quality.check_quality(image_path) -> {"ok": bool, "message": str}
- notes.extract_from_notes(note_text) -> {"symptoms": list, "summary": str}
- fusion.combine(image_result, notes_result) -> dict
- report.build_report(fused_result) -> str
