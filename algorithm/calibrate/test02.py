import cv2
import numpy as np
T = np.zeros((1,3), np.float32)
a = (0.2,0.4,0.8)
print (a)
R = cv2.Rodrigues(a)

print (R[0])
while True:
    cv2.imshow('tmp', np.zeros(shape=(1000, 1000, 3), dtype=np.uint8))
    a = cv2.waitKey(0)
    print(a)
# v3 = (R[0][2,1],R[0][0,2],R[0][1,0])
# print (v3)
# c = cv2.Rodrigues(v3)
# print (c[0])
# b = cv2.Rodrigues(R[0])
# print (b[0])
# p = (-2.100418,-2.167796,0.27330)