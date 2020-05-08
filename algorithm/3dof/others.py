from numpy import cos, sin, pi
import numpy as np


def me_round(x):
    return np.round(x, decimals=3)


def forward_kinematics(theta1, theta2, theta3, l1, l2, l3):
    # 根据舵机角度正向解出目标坐标
    x = l1 * cos(theta1) + l2*cos(theta1+theta2) + l3 * cos(theta1+theta2+theta3)
    y = l1 * sin(theta1) + l2*sin(theta1+theta2) + l3 * sin(theta1+theta2+theta3)
    return list(map(me_round, (x, y)))



if __name__ == '__main__':
	print(forward_kinematics(pi/4,pi/2,pi/4, 1, 1, 1))