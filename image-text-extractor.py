from PIL import Image, ImageEnhance, ImageFilter
import pytesseract
path = 'example_03.png'	# - > Your Image Location
img = Image.open(path)
img = img.convert('RGB')
pix = img.load()
for y in range(img.size[1]):
	for x in range(img.size[0]):
		if pix[x, y][0] < 102 or pix[x, y][1] < 102 or pix[x, y][2] < 102:
			pix[x, y] = (0, 0, 0, 255)
else :
	pix[x, y] = (255, 255, 255, 255)
img.save('temp.png')
text = pytesseract.image_to_string(Image.open('temp.jpeg'))# os.remove('temp.jpg')
print(text)# print image_to_string(Image.open('find.jpg'))