from PIL import Image 
from urllib.request import urlopen

url = "https://guide-images.cdn.ifixit.com/igi/TFgdpPMaImoBKvpm.huge"
img = Image.open(urlopen(url))
img.show()