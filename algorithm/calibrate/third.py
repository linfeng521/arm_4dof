import cv2
import glob
import numpy as np

#棋盘规格
cbraw = 6
cbcol = 9
objp = np.zeros((cbraw*cbcol,3), np.float32)
objp[:,:2] = np.mgrid[0:cbraw,0:cbcol].T.reshape(-1,2)

objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.

images = glob.glob("raspi/*.jpg")
for fname in images:
    img = cv2.imread(fname) #source image
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #转灰度
    ret, corners = cv2.findChessboardCorners(gray,(6,9),None)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
    corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
    objpoints.append(objp)
    imgpoints.append(corners2)
    img = cv2.drawChessboardCorners(gray,(6,9),corners2,ret)
    cv2.imshow('img',img)
    cv2.waitKey(1000)
'''
传入所有图片各自角点的三维、二维坐标，相机标定。
每张图片都有自己的旋转和平移矩阵，但是相机内参和畸变系数只有一组。
mtx，相机内参；dist，畸变系数；revcs，旋转矩阵；tvecs，平移矩阵。
'''
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1],None,None)
img = cv2.imread('raspi/img1.jpg')
#注意这里跟循环开头读取图片一样，如果图片太大要同比例缩放，不然后面优化相机内参肯定是错的。
img = cv2.resize(img,None,fx=0.5, fy=0.5, interpolation = cv2.INTER_CUBIC)
h,w = img.shape[:2]
'''
优化相机内参（camera matrix），这一步可选。
参数1表示保留所有像素点，同时可能引入黑色像素，
设为0表示尽可能裁剪不想要的像素，这是个scale，0-1都可以取。
'''
newcameramtx, roi=cv2.getOptimalNewCameraMatrix(mtx,dist,(w,h),1,(w,h))
#计算误差
tot_error = 0
for i in range(len(objpoints)):
    imgpoints2, _ = cv2.projectPoints(objpoints[i], rvecs[i], tvecs[i], mtx, dist)
    error = cv2.norm(imgpoints[i],imgpoints2, cv2.NORM_L2)/len(imgpoints2)
    tot_error += error
print('内参数矩阵',mtx)
print('内参数矩阵:',newcameramtx)
print(" 畸变系数",dist)
print(" 旋转向量",rvecs)
print(" 平移向量",tvecs)
print ("total error: ", tot_error/len(objpoints))
