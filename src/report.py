def build_text(report: dict) -> str:
    q = report["quality"]
    if q["warnings"] or q["score"] < 0.6:
        quality_txt = "limited (" + "; ".join(q["warnings"] or ["low score"]) + ")"
    else:
        quality_txt = "acceptable"

    lines = []
    if report["findings"]:
        for f in report["findings"]:
            line = f"Doctor, consider a possible {f['condition']} (Confidence: {f['band']}, {f['confidence']:.2f})."
            if f["region"] and f["region"]["box"]:
                line += f" Highlighted region at {f['region']['box']}."
            if f["note_evidence"]:
                quotes = ", ".join(f'"{x}"' for x in f["note_evidence"])
                line += f" Notes support: {quotes}."
            lines.append(line)
    else:
        lines.append(
            f"No tumour-like region was identified (Confidence {report['probs']['notumor']:.2f}). "
            "Please review the image independently."
        )

    if report["mismatch"]:
        lines.append(report["mismatch"])
    lines.append(f"Image quality: {quality_txt}.")
    lines.append(report["disclaimer"])
    return "\n".join(lines)