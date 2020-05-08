from numpy import cos, sin, pi
import numpy as np


def me_round(x):
    return np.round(x, decimals=3)


def forward_kinematics(theta1, theta2, theta3, theta4, l1, l2, l3):
	# 根据舵机角度正向解出目标坐标
	x = l1 * cos(theta1) + l2 * cos(theta1 + theta2) + l3 * cos(theta1 + theta2 + theta3)
	y = l1 * sin(theta1) + l2 * sin(theta1 + theta2) + l3 * sin(theta1 + theta2 + theta3)
	return list(map(me_round, (x, y)))

def inverse_kinematics(x,y,z,l1,l2,l3):
	theta1 = 0
	theta2 = 0
	theta3 = 0

if __name__ == '__main__':
	# inverse_kinematics(-0.0, -1.414, 2.414)
	print(forward_kinematics(0, 0,  pi / 2, pi /2, 1, 1, 1))
	inverse_kinematics(-0.755,2.816,-0.252,1,1,1)