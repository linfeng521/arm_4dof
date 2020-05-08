import numpy as np
from numpy import pi,cos,sin

class Arm(object):
    def __init__(self,q = None,q0=None, L=None):
        # initial joint angles
        self.q = [.3,.3, .3, 0] if q is None else q
        # some default arm positions
        self.q0 = np.array([np.pi / 4, np.pi / 4,np.pi / 4, np.pi / 4]) if q0 is None else q0
        # arm segment lengths
        self.L = np.array([1, 1, 1,1]) if L is None else L
        self.max_angles = [np.pi, np.pi, np.pi / 4, np.pi / 4]
        self.min_angles = [0, 0, -np.pi / 4,-np.pi / 4]

    def me_round(self,x):
        return np.round(x, decimals=3)

    def forward_kinematics(self,q=None):
        if q is None:
            q = self.q
        # 根据舵机角度正向解出目标坐标
        x = (self.L[1] * cos(q[1]) + self.L[2] * cos(q[1] + q[2]) + self.L[3] * cos(q[1] + q[2] + q[3])) * cos(q[0])
        y = (self.L[1] * cos(q[1]) + self.L[2] * cos(q[1] + q[2]) + self.L[3] * cos(q[1] + q[2] + q[3])) * sin(q[0])
        z = self.L[1] * sin(q[1]) + self.L[2] * sin(q[1] + q[2]) + self.L[3] * sin(q[1] + q[2] + q[3])+self.L[0]
        return list(map(self.me_round, (x, y, z)))

    def inverse_kinematics(self,pos):
        # POS 手腕坐标位置
        # theta1
        theta1 = np.arctan2(pos[1],pos[0])
        # # 转换坐标平面
        # if theta1 == pi/2:
        #     x = pos[1]
        # else:
        #     x = pos[0]/np.cos(theta1)

        r1 = np.sqrt(pos[0]**2+pos[1]**2)
        r2 = pos[3]-self.L[0]
        r3 = np.sqrt(r1**2+r2**2)
        fai1 = np.arctan2(r2,r1)
        fai2 = np.arccos()
        # 手腕坐标（x,l4)
        z = pos[2]+self.L[3]
        # theta2
        alpha = np.arctan2(z-self.L[0],x)
        d = np.sqrt(x**2+(z-self.L[0])*2)
        cos_theta2a = (self.L[1]**2+d**2-self.L[2]**2)/(2*self.L[1]*d)
        # a_sin_theta1a = np.sqrt(1 - cos_theta1a ** 2)
        # b_sin_theta1a = -a_sin_theta1a
        # a_theta1a = np.arctan2(a_sin_theta1a, cos_theta1a)
        # b_theta1a = np.arctan2(b_sin_theta1a, cos_theta1a)
        theta2a = np.arccos(cos_theta2a)
        theta2 = theta2a+alpha
        # theta3
        cos_theta3 = (d**2 - self.L[1]**2-self.L[2]**2)/(2*self.L[1]*self.L[2])
        theta3 = np.arccos(cos_theta3)
        # theta3
        theta4 = pi/2-theta3+theta2
        q = [np.arctan(np.tan(i)) for i in [theta1,theta2,theta3,theta4]]
        deg =  [theta*180/pi for theta in q]
        return q,deg

if __name__ == '__main__':
    arm = Arm(L=[1,1,1,1])
    q = [ 1.1071 ,   0.4964   ,-1.0327 ,  -0.7704]
    pos = arm.forward_kinematics(q)
    print('顺运动学x,y,z\t'+str(pos))
    # q,deg = arm.inverse_kinematics(pos)
    # print('逆运动学q1 q2 q3 a4\t'+str(deg))
    # valid_pos = arm.forward_kinematics(q)
    # print('验证顺
    # 运动学x,y,z'+str(valid_pos))