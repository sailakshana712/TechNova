import glob
from PIL import Image
import quality

for p in glob.glob("data/normal/*"):
    r = quality.check_quality(Image.open(p))
    if r["warnings"]:
        print(p)
        print("  warnings:", r["warnings"])
        print("  blur=%.1f  brightness=%.1f  contrast=%.1f" % (r["blur"], r["brightness"], r["contrast"]))