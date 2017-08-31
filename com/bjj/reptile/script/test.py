#-*-coding:utf-8-*-
import pytesseract
from PIL import Image
import sys
reload(sys)
sys.setdefaultencoding('utf-8')





image = Image.open('C:\\Users\\ShineMo-177\\Desktop\\log\\20170831135855 .png')
code = pytesseract.image_to_string(image)
print code.decode('utf-8')




