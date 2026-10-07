import glob
import streamlit as st
from PIL import Image
from src.fusion import build_report

st.set_page_config(page_title="Brain MRI Second Opinion", layout="wide")
st.title("Brain MRI Second Opinion (decision support)")
st.caption("This tool assists doctors. It does not diagnose. The clinician decides.")

# ---------- Sidebar: one-click demo ----------
st.sidebar.header("Demo cases")
samples = sorted(glob.glob("data/sample/*.jpg") + glob.glob("data/sample/*.png"))
img_choice = st.sidebar.selectbox("Sample MRI", ["(upload my own)"] + samples)
note_files = sorted(glob.glob("data/notes/*.txt"))
note_choice = st.sidebar.selectbox("Sample note", ["(type my own)"] + note_files)

default_note = ""
if note_choice != "(type my own)":
    with open(note_choice, encoding="utf-8") as fh:
        default_note = fh.read()

# ---------- Inputs ----------
uploaded = st.file_uploader("Upload MRI", type=["jpg", "jpeg", "png"])
note = st.text_area("Clinical notes", value=default_note, height=120)

img = None
if uploaded:
    img = Image.open(uploaded)
elif img_choice != "(upload my own)":
    img = Image.open(img_choice)

# ---------- Analysis ----------
if img is not None and st.button("Analyze"):
    r = build_report(img, note)

    left, right = st.columns(2)
    left.image(img, caption="Original", use_container_width=True)

    st.subheader("Image quality")
    if r["quality"]["warnings"]:
        for w in r["quality"]["warnings"]:
            st.warning(w)
    else:
        st.success("Acceptable")

    if r["mismatch"]:
        st.warning(r["mismatch"])

    for fd in r["findings"]:
        st.markdown(f"### Doctor, consider: possible **{fd['condition']}**")
        st.progress(fd["confidence"],
                    text=f"Confidence {fd['confidence']:.0%} ({fd['band']})")
        if fd["region"]:
            right.image(fd["region"]["overlay"],
                        caption=f"Region: {fd['condition']}",
                        use_container_width=True)
        for q in fd["note_evidence"]:
            st.info(f"Note evidence: “{q}”")

    if not r["findings"]:
        st.success("No tumour-like region identified. Please review independently.")

    st.caption(r["disclaimer"])