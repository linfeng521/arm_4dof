import numpy as np
import cv2 as cv
'''
图像的灰度化、图像的二值化、图像轮廓的提取以及中心点的生成。
'''

font = cv.FONT_HERSHEY_TRIPLEX  # 定义字体
while True:
    img = cv.imread('src/img.png')
    img_gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)

    ret, binary = cv.threshold(img_gray, 127, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    # 形态学闭运算(消除黑洞)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    binary_closing = cv.morphologyEx(binary, cv.MORPH_CLOSE, kernel)

    # 检索轮廓: 第二个参数表示轮廓的检索模式, 第三个参数method为轮廓的近似办法
    contours, hierarchy = cv.findContours(binary_closing, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    cv.imshow('close',binary_closing)

    # 遍历全部轮廓
    for i, contour in enumerate(contours):
        # 轮廓面积
        area = cv.contourArea(contour)
        # 几何矩
        mm = cv.moments(contour)
        # 获得中心矩(质心坐标)
        if mm['m00']:
            cx = int(mm['m10'] / mm['m00'])
            cy = int(mm['m01'] / mm['m00'])
        else:
            continue

        """
        circle(img, center, radius, color[, thickness[, lineType[, shift]]]) -> img
        #在原图img上绘制圆（圆心np.int(cx), np.int(cy)）
        半径 3 ,颜色(0,255,0)绿,线宽2（如果为负数则填充）
        """
        # 绘制中心点
        cv.circle(img, (np.int(cx), np.int(cy)), 3, (0, 0, 0), -1)
        cv.putText(img,"({},{})".format(cx,cy),(cx-50,cy-20),font,0.7, (0,0,0), 1)
        '''
        # 轮廓外接矩形面积
        x, y, w, h = cv.boundingRect(contour)
        cv.rectangle(img, (x, y), (x + w, y + h), (127, 127, 255), 2)
        '''
        # 拟合多边形
        approxCurve = cv.approxPolyDP(contour, 10, True)
        # 画轮廓多边形拟合数目>6的图形轮廓为红色
        if approxCurve.shape[0] > 6:
            # 绘制轮廓: 第二个参数是轮廓本身，在Python中是一个list。第三个绘制轮廓list中的哪条轮廓，如果是-1，则绘制其中的所有轮廓。
            cv.drawContours(img, contours, i, (0, 0, 255), 2)
        # 画轮廓多边形拟合数目=4的图形轮廓为绿色
        elif approxCurve.shape[0] == 4:
            cv.drawContours(img, contours, i, (0, 255, 0), 2)
        # 画轮廓多边形拟合数目=3的图形轮廓为蓝
        elif approxCurve.shape[0] == 3:
            cv.drawContours(img, contours, i, (255, 0, 0), 2)
        # 画其余数目的轮廓多边形拟合的图形轮廓为黄色
        else:
            cv.drawContours(img, contours, i, (0, 255, 255), 2)
    cv.imshow('input_image', img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()
