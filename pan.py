# -*- coding: utf-8 -*-
"""
Created on Sun May  5 12:28:09 2019

@author: Parashar
"""
#import cv2

#img = cv2.imread('C:\\Users\\Parashar\\Pictures\\Fest\\IMG_6129.JPG')
#img.show(img)

from PIL import Image,ImageFilter
from pytesseract import image_to_string
import pytesseract as pyt

img_path = 'C:/Users/Parashar/Downloads/New Doc 2018-12-22 10.46.48.jpg'
im = Image.open(img_path).convert('L')
im = im.filter(ImageFilter.BLUR)
im.save('greyscale.png')
im.show()

pyt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
image_details = {}
details = image_to_string(im)
image_details['Name']=details.split('\n')[4]
image_details["Father's Name"]=details.split('\n')[5]
image_details['Date of Birth']=details.split('\n')[6]
image_details['PAN number']=details.split('\n')[10]
print(image_details)
