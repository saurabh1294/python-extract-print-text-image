from PIL import Image
from pytesseract import image_to_string
print(image_to_string(Image.open('png-logo-text.png')))
print(image_to_string(Image.open('shadow.png'), lang='eng'))
print(image_to_string(Image.open('download.png')))
print(image_to_string(Image.open('example_01.png')))
print(image_to_string(Image.open('example_02.png')))
print(image_to_string(Image.open('example_03.png')))