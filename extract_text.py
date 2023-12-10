from PIL import Image
from pytesseract import Output
import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'


# # Open an image file
image_path = 'form.png'
img = Image.open(image_path)

_config = r'--psm 11 --oem 3'

# Use Tesseract OCR to extract text
# text = pytesseract.image_to_string((img), config=_config)

# Print the extracted text
#print(text)

# # Example: Post-process Tesseract output to extract table rows
# lines = text.split('\n')
# table_data = [line.split('\t') for line in lines]

# #Print the extracted table data
# for row in table_data:
#    print(row)

# Example: Extract bounding boxes from an image
pic = cv2.imread('form.png')
height, width, _ = pic.shape
# boxes = pytesseract.image_to_boxes(pic, config=_config)
# for box in boxes.splitlines():
#     box = box .split(' ')
#     #draw a rectangle around each character
#     img = cv2.rectangle(pic, (int(box[1]), height - int(box[2])), (int(box[3]), height - int(box[4])), (0, 255, 0), 2)

data = pytesseract.image_to_data(pic, config=_config, output_type=Output.DICT)
# print(data['text'], "/n") 

amount_boxes = len(data['text'])
for i in range(amount_boxes):
    if float(data['conf'][i]) > 30:
        (x, y, width, height) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
        pic = cv2.rectangle(pic, (x, y), (x + width, y + height), (0, 255, 0), 2)
        pic = cv2.putText(pic, data['text'][i], (x, y+height+20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2,cv2.LINE_AA)
cv2.imshow('pic', pic)
cv2.waitKey(0)