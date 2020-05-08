import numpy as np
from numpy import pi, cos, sin


def forward_kinematics(a1, a2, a3, theta1, theta2, theta3):
    # 根据舵机角度正向解出目标坐标
    x = (a2 * cos(theta2) + a3 * cos(theta2 + theta3)) * cos(theta1)
    y = (a2 * cos(theta2) + a3 * cos(theta2 + theta3)) * sin(theta1)
    z = (a2 * sin(theta2) + a3 * sin(theta2 + theta3)) + a1
    return x, y, z


def inverse_kinematics(a1, a2, a3, x, y, z):
    # POS 手腕坐标位置即末端执行器坐标
    # theta1
    theta1 = np.arctan2(y, x)
    r1 = np.sqrt(x ** 2 + y ** 2)
    r2 = z - a1
    r3 = np.sqrt(r1 ** 2 + r2 ** 2)
    fai1 = np.arctan2(r2, r1)
    cos_fai2 = (a2 ** 2 + r3 ** 2 - a3 ** 2) / (2 * a2 * r3)
    sin_fai2 = np.sqrt(1 - cos_fai2 ** 2)
    a_fai2 = np.arctan2(sin_fai2, cos_fai2)
    b_fai2 = np.arctan2(sin_fai2, -cos_fai2)
    fai3 = np.arccos((a2 ** 2 + a3 ** 2 - r3 ** 2) / (2 * a2 * a3))
    theta21 = fai1 + a_fai2
    theta22 = fai1 + b_fai2
    theta3 = pi - fai3
    return theta1, theta21,theta22, theta3


def rad2deg(a):
    for i in a:
        print(round(i * 180 / pi))


a = inverse_kinematics(1, 1, 1, -1, 0, 2)
rad2deg(a)

postion = forward_kinematics(1,1,1,0,pi/2,pi/2)
for i in postion:
    print(round(i))