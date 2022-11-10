pip install pillow
pip install pypng
pip install pyqrcode




import pyqrcode
import png
from PIL import Image
link = input("Enter anything to create QR: ")
qr_code = pyqrcode.create(link)
qr_code.png("QRCode.png", scale=5) # yaha pe brackets pe QRCode.png ki jagah jo naam rakhna hai rakh sakte hai