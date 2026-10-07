from PIL import Image
import glob
from quality import check_quality

path = glob.glob("data/normal/*")[0]
print("Testing:", path)
print(check_quality(Image.open(path)))