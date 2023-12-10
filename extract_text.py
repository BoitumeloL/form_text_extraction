from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'


# Open an image file
image_path = 'form.png'
img = Image.open(image_path)

# Use Tesseract OCR to extract text
text = pytesseract.image_to_string(img)

# Print the extracted text
#print(text)

# Example: Post-process Tesseract output to extract table rows
lines = text.split('\n')
table_data = [line.split('\t') for line in lines]

# Print the extracted table data
for row in table_data:
    print(row)
