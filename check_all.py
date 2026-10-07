import glob, os
from PIL import Image
from src.model import predict

right = 0
files = sorted(glob.glob("samples/*"))
for f in files:
    true = os.path.basename(f).split("_")[0]
    probs = predict(Image.open(f))
    guess = max(probs, key=probs.get)
    right += (guess == true)
    print(f"{os.path.basename(f):22} true={true:11} guess={guess:11} {probs[guess]:.0%}")
print(f"\n{right} / {len(files)} correct")