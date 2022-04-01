import cv2
import pytesseract
from pytesseract import Output
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread('invoice-sample.jpg')
imageFile = 'C:/Users/lawre/Downloads/panda_receipt_ex.jpg'
img = cv2.imread(imageFile)
d = pytesseract.image_to_data(img, output_type=Output.DICT)
print(d.keys())
print(d.items())
n_boxes = len(d['text'])
custom_config = r'--oem 3 --psm 6 outputbase digits'
print(pytesseract.image_to_string(img, config=custom_config))
z = pytesseract.image_to_string(img, config=custom_config)
z1 = z.split()
for i in z1:
    if len(i) > 14:
        coupon = i

c = coupon.replace("-", " ")
print(c)