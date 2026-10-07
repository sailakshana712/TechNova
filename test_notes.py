import glob
from notes import extract, red_flags

for path in sorted(glob.glob("data/notes/*.txt")):
    with open(path, encoding="utf-8") as f:
        note = f.read()
    print("\n==", path)
    print("  red flags:", red_flags(note))
    for cls in ["glioma", "meningioma", "pituitary"]:
        found = extract(note, cls)
        print(f"  {cls}: {[x['keyword'] for x in found]}")
        for x in found:
            assert x["quote"] in note, "Quote not found in note!"

print("\nAll quotes verified.")