from PIL import Image
import pytesseract
import argparse
import cv2
import os

ap = argparse.ArgumentParser()
ap.add_argument('-i','--image',required=True,help='Path to image')
ap.add_argument('-p','--preprocess',type=str,default='thresh')
args = vars(ap.parse_args())
#load image and convert to greyscale
image = cv2.imread(args['image'])
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
if args['preprocess'] == 'thresh':
    gray = cv2.threshold(gray,0,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
elif args['preprocess'] == 'blur':
    gray = cv2.medianBlur(gray,3)
filename = '{}.png'.format(os.getpid())
cv2.imwrite(filename,gray)
text = pytesseract.image_to_string(Image.open(filename))
os.remove(filename)
print(text)
cv2.imshow("Original",image)
cv2.imshow("Gray",gray)
cv2.waitKey(0)
