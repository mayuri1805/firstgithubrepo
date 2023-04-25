# import image
import openpyxl
from openpyxl.drawing.image import Image

path = "C:\Users\Asus\OneDrive\Documents\imagelogo.xl.xlsx"

workbook = openpyxl.load_workbook(path)
sheet = workbook["Sheet 1"]

img = Image('Logo.png')

# adjusting height
img.height = 140

# adjusting width
img.width = 140

sheet.add_image(img, 'F7')
workbook.save(path)