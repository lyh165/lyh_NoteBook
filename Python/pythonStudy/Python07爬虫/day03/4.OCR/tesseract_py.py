#coding=utf-8
from pytesseract import *
from PIL import Image
#打开图片
image = Image.open("tessercat3.png")
text = image_to_string(image)
print text
