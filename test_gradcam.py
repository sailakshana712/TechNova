import sys
from PIL import Image
import matplotlib.pyplot as plt
from src.model import predict
from src.gradcam import explain

img = Image.open(sys.argv[1])
probs = predict(img)
top = max(probs, key=probs.get)
print(probs, "->", top)

out = explain(img, top)
print("box:", out["box"], "area_frac:", out["area_frac"])

fig, ax = plt.subplots(1, 2, figsize=(8, 4))
ax[0].imshow(img.convert("RGB").resize((224, 224))); ax[0].set_title("Original")
ax[1].imshow(out["overlay"]); ax[1].set_title(f"{top} ({probs[top]:.0%})")
for a in ax: a.axis("off")
plt.savefig("example.png", dpi=150, bbox_inches="tight")
print("saved example.png")