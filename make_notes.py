import os

os.makedirs("data/notes", exist_ok=True)

notes = {
    "01_glioma.txt": "45F, progressive headaches for 3 weeks. New-onset seizure. Reports memory problems and some confusion.",
    "02_meningioma.txt": "62F, slow worsening headache over months. Noticed vision changes in the left eye and numbness in the face.",
    "03_pituitary.txt": "34F, irregular periods with amenorrhea for 6 months. Reports galactorrhea and fatigue. Visual field loss on exam.",
    "04_irrelevant_ankle.txt": "Routine check, sprained ankle. Swelling reduced with ice. Advised rest.",
    "05_irrelevant_checkup.txt": "Annual checkup. Blood pressure normal. No complaints. Flu shot given.",
    "06_contradict.txt": "58M, severe headache, seizure, vomiting, confusion, weakness, double vision, memory loss.",
    "07_empty.txt": "",
    "08_messy.txt": "56m c/o HA x2wk, ?vis blurring, hx HTN. pt c/o N/V. no fx. ?seizure vs syncope",
}

for filename, text in notes.items():
    with open(os.path.join("data/notes", filename), "w", encoding="utf-8") as f:
        f.write(text)

print("created", len(notes), "notes")