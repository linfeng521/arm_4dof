import numpy as np
import cv2
import glob



def resize():
    files = glob.glob("img/*.jpg")
    for file in files:
        img = cv2.imread(file)
        img02 = cv2.resize(img,None,fx=0.2,fy=0.2,interpolation=cv2.INTER_AREA)
        cv2.imwrite(file,img02)

def shot():
    i = 0
    cap = cv2.VideoCapture(0)
    # 当视频对象初始化完成之后，isOpened()返回true
    while cap.isOpened():
        ret, frame = cap.read()
        retval = cv2.waitKey(10)
        if retval & 0xFF == ord('q'):
            break
        elif retval & 0xFF == ord('s'):
            i = i+1
            cv2.imwrite('img{}.jpg'.format(i),frame)
        else:
            cv2.imshow('frame', frame)
    cap.release()

if __name__ == '__main__':
    shot()
cv2.destroyAllWindows()
