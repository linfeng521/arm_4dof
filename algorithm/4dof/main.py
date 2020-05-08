from numpy import cos, sin, pi
import numpy as np


def me_round(x):
    return np.round(x, decimals=3)


def forward_kinematics(theta1, theta2, theta3, theta4, l1, l2, l3):
    # 根据舵机角度正向解出目标坐标
    x = (l1 * cos(theta2) + l2 * cos(theta2 + theta3) + l3 * cos(theta2 + theta3 + theta4)) * cos(theta1)
    y = (l1 * cos(theta2) + l2 * cos(theta2 + theta3) + l3 * cos(theta2 + theta3 + theta4)) * sin(theta1)
    z = l1 * sin(theta2) + l2 * sin(theta2 + theta3) + l3 * sin(theta2 + theta3 + theta4)
    return list(map(me_round, (x, y, z)))

def inverse_kinematics(x,y,z,l1,l2,l3):
	theta1 = 0
	theta2 = 0
	theta3 = 0
	theta4 = 0
	theta1 = np.arctan2(y,x)
	print(theta1*180/pi)

	a = x / cos(theta1)
	# 如果x为0，需要交换x，y
	if x == 0:
		a = y
	b = z
	for i in range(2):
		print(a,b)
		theta2 = pi/4
		# 求解theta4
		kesai = np.arctan2(b,a)
		d = np.sqrt(a**2 + b**2)
		D = (d**2 + l1**2 - 2 * d*l1*cos(pi/2 - theta2 - kesai) - l2**2 -l3**2 ) / (2 * l2*l3)
		print('----0')
		print(D)
		theta4 = np.arccos(D)
		print(theta4*180/pi)
		# C = (a-l1*sin(theta2))**2 + (b-l1*cos(theta2))**2
		# # cos
		# D = (l2**2+l3**2-C)/2*l2*l3
		# print('D valaue')
		# print(D)
		# S1 = np.sqrt(1 - D ** 2)
		# S2 = -S1
		# a_theta4 = pi - np.arctan2(S1, D)
		# b_theta4 = pi - np.arctan2(S2, D)


		print('theta4')
		# print(a_theta4*180/pi,b_theta4*180/pi)

	# for (theta2 = -90; theta2 < 90; theta2++) // 先确定theta2的值，并且把theta2从-90°到90°都取一遍，算出所有有可能的解
	# {
	# 	theta2 *= RAD2ANG; // 弧度转换
	# theta4 = acos(
	# 	(pow(a, 2) + pow(b, 2) + pow(L1, 2) - pow(L2, 2) - pow(L3, 2) - 2 * a * L1 * sin(theta2) - 2 * b * L1 * cos(theta2)) / (
	# 				2 * L2 * L3));
	# // 确定theta2的角度后，就可以求出theta4的角度。
	# m = L2 * sin(theta2) + L3 * sin(theta2) * cos(theta4) + L3 * cos(theta2) * sin(theta4);
	# n = L2 * cos(theta2) + L3 * cos(theta2) * cos(theta4) - L3 * sin(theta2) * sin(theta4);
	# t = a - L1 * sin(theta2);
	# p = pow(pow(n, 2) + pow(m, 2), 0.5);
	# q = asin(m / p);
	# theta3 = asin(t / p) - q;
	# // 接着就可以求出theta3的角度。
	# // 求出4个角度后，我们先验算一遍这4个角度求出的值（x1, y1, z1）和我们的目标坐标（x, y, z）是否一致
	# x1 = (L1 * sin(theta2) + L2 * sin(theta2 + theta3) + L3 * sin(theta2 + theta3 + theta4)) * cos(theta1);
	# y1 = (L1 * sin(theta2) + L2 * sin(theta2 + theta3) + L3 * sin(theta2 + theta3 + theta4)) * sin(theta1);
	# z1 = L1 * cos(theta2) + L2 * cos(theta2 + theta3) + L3 * cos(theta2 + theta3 + theta4);
	# theta2 = ANG2RAD(theta2);
	# theta3 = ANG2RAD(theta3);
	# theta4 = ANG2RAD(theta4);
	# // 输出误差小于1cm的解，并输出该解的正向解目标
	# if (x1 < (x + 1) & & x1 > (x - 1) & & y1 < (y + 1) & & y1 > (y - 1) & & z1 < (z + 1) & & z1 > (z - 1))
	# {
	# 	printf("theta2:%f,theta3:%f,theta4:%f,x:%f,y:%f,z:%f\r\n", theta2, theta3, theta4, x1, y1, z1);
	# }
	# }

if __name__ == '__main__':
	# inverse_kinematics(-0.0, -1.414, 2.414)
	print(forward_kinematics(0, 0,  pi / 2, pi /2, 1, 1, 1))
	inverse_kinematics(-0.755,2.816,-0.252,1,1,1)