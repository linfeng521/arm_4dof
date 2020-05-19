import numpy as np
import cv2
import glob

files = glob.glob("img/*.jpg")

for file in files:
    img = cv2.imread(file)
    img02 = cv2.resize(img,None,fx=0.2,fy=0.2,interpolation=cv2.INTER_AREA)
    cv2.imwrite(file,img02)

cv2.destroyAllWindows()
