import glob, os
from PIL import Image
import matplotlib.pyplot as plt
from src.model import predict
from src.gradcam import explain

os.makedirs("assets", exist_ok=True)
for f in sorted(glob.glob("samples/*")):
    name = os.path.splitext(os.path.basename(f))[0]
    true = name.split("_")[0]
    if true == "notumor":
        continue                      # no tumour, so the heatmap means nothing
    img = Image.open(f)
    probs = predict(img)
    guess = max(probs, key=probs.get)
    out = explain(img, guess)
    tag = "correct" if guess == true else "wrong"

    fig, ax = plt.subplots(1, 2, figsize=(8, 4))
    ax[0].imshow(img.convert("RGB").resize((224, 224))); ax[0].set_title(f"True: {true}")
    ax[1].imshow(out["overlay"]); ax[1].set_title(f"Predicted: {guess} ({probs[guess]:.0%})")
    for a in ax: a.axis("off")
    plt.savefig(f"assets/{tag}_{name}.png", dpi=120, bbox_inches="tight")
    plt.close()
print("done, look in the assets folder")