import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'E:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image

#img = Image.open('maya-angelou-famous-quote.png')
#img = Image.open('submit.png')
img = Image.open('iphone.webp')
#img = Image.open('code.png')
text = tess.image_to_string(img)

print(text)