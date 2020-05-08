from numpy import *
import numpy as np
import utils


def inverse_kinematics(x,y,l1,l2):
    solve = []
    # theta2存在两个解
    D = (x**2 + y**2 - l1**2 - l2**2)/(2*l1*l2)
    S1 = np.sqrt(1-D**2)
    S2 = -S1
    a_theta2 = arctan2(S1,D)
    b_theta2 = arctan2(S2,D)
    # 计算theta1
    kesi = np.arctan2(y,x)
    a_theta1 = kesi - arcsin(l2*sin(pi-a_theta2)/np.sqrt(x**2 + y**2 ))
    b_theta1 = kesi - arcsin(l2*sin(pi-b_theta2)/np.sqrt(x**2 + y**2 ))
    solve.append((utils.rad2deg(a_theta1),utils.rad2deg(a_theta2)))
    solve.append((utils.rad2deg(b_theta1),utils.rad2deg(b_theta2)))
    return solve


def forward_kinematics(theta1, theta2, l1, l2):
    '''
    正向运动学
    :param theta1: q1
    :param theta2: q2
    :param elbow: 肘的长度
    :param wrist: 手掌的长度
    :return:
    '''
    x = l1*cos(theta1)+l2*cos(theta1+theta2)
    y = l1*sin(theta1)+l2*sin(theta1+theta2)
    # 保留两位小数
    x = np.round(x,decimals=2)
    y = np.round(y,decimals=2)
    return x,y

if __name__ == '__main__':
    print(forward_kinematics(pi, -pi / 2, 2, 3))
    print(inverse_kinematics(-2,3,2,3))