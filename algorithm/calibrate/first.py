import numpy as np
import cv2 as cv
import glob
np.set_printoptions(precision=3,suppress=True)
# termination criteria
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((9*6,3), np.float32)
objp[:,:2] = np.mgrid[0:6,0:9].T.reshape(-1,2)
## 储存棋盘格角点的世界坐标和图像坐标对
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.
images = glob.glob('img/*.jpg')
i = 0
for fname in images:
    img = cv.imread(fname)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # # 找到棋盘格角点
    ret, corners = cv.findChessboardCorners(gray, (9,6), None)
    # If found, add object points, image points (after refining them)
    if ret == True:
        objpoints.append(objp)
        corners2 = cv.cornerSubPix(gray,corners, (11,11), (-1,-1), criteria)
        imgpoints.append(corners)
        # # 将角点在图像上显示
        cv.drawChessboardCorners(img, (9,6), corners2, ret)
        cv.imshow('findCorners', img)
        cv.waitKey(1)
cv.destroyAllWindows()

ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

'''
mtx 内参数矩阵
dist 畸变系数
rvecs 旋转向量
tvecs 平移向量
'''

print('内参数矩阵:',mtx)
print(" 畸变系数",dist)
print(" 旋转向量",rvecs)
print(" 平移向量",tvecs)

# np.array(mtx).dot()