import glob
from PIL import Image
import quality

def measure(pattern):
    return [quality.check_quality(Image.open(p)) for p in glob.glob(pattern)]

def get(rows, key):
    return [r[key] for r in rows]

def middle(low, high, name):
    if low >= high:
        print(f"WARNING: {name}: good and bad images overlap ({low:.1f} vs {high:.1f}). Tell me about this.")
    return (low + high) / 2

normal = measure("data/normal/*")
bad = {k: measure(f"data/degraded/*_{k}.png") for k in ["blur", "dark", "bright", "lowcon"]}

if not normal or not all(bad.values()):
    print("Missing images! Check data/normal and data/degraded.")
    raise SystemExit

blur_t     = middle(max(get(bad["blur"], "blur")),            min(get(normal, "blur")),       "BLUR_T")
dark_t     = middle(max(get(bad["dark"], "brightness")),      min(get(normal, "brightness")), "DARK_T")
bright_t   = middle(max(get(normal, "brightness")),           min(get(bad["bright"], "brightness")), "BRIGHT_T")
contrast_t = middle(max(get(bad["lowcon"], "contrast")),      min(get(normal, "contrast")),   "CONTRAST_T")

print("\nCopy these 4 lines into quality.py (replace the old 4 numbers):\n")
print(f"BLUR_T = {blur_t:.1f}")
print(f"DARK_T = {dark_t:.1f}")
print(f"BRIGHT_T = {bright_t:.1f}")
print(f"CONTRAST_T = {contrast_t:.1f}")

# Test these numbers right now
quality.BLUR_T, quality.DARK_T = blur_t, dark_t
quality.BRIGHT_T, quality.CONTRAST_T = bright_t, contrast_t

flagged = sum(1 for r in measure("data/normal/*") if r["warnings"])
print(f"\nNormal images wrongly flagged: {flagged} of {len(normal)}  (want 0)")
for k, rows in bad.items():
    caught = sum(1 for r in measure(f"data/degraded/*_{k}.png") if r["warnings"])
    print(f"{k:7} images caught: {caught} of {len(rows)}  (want all)")