import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image
qr=pyqrcode.create("welcome to testing")
qr.png("testcode.png",scale =8)
d=decode(Image.open("testcode.png"))
print(d[0].data.decode("ascii"))
