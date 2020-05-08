import numpy as np
from numpy import pi
class Arm(object):
    def __init__(self,q = None,q0=None, L=None):
        # initial joint angles
        self.q = [.3, .3, 0] if q is None else q
        # some default arm positions
        self.q0 = np.array([np.pi / 4, np.pi / 4, np.pi / 4]) if q0 is None else q0
        # arm segment lengths
        self.L = np.array([1, 1, 1]) if L is None else L
        self.max_angles = [np.pi, np.pi, np.pi / 4]
        self.min_angles = [0, 0, -np.pi / 4]

    def forward_kinematics(self,q=None):
        if q is None:
            q = self.q
        x = self.L[0] * np.cos(q[0]) + \
            self.L[1] * np.cos(q[0] + q[1]) + \
            self.L[2] * np.cos(np.sum(q))
        y = self.L[0] * np.sin(q[0]) + \
            self.L[1] * np.sin(q[0] + q[1]) + \
            self.L[2] * np.sin(np.sum(q))
        return [x, y]

    def inverse_kinematics(self,pos):
        y = pos[1]-self.L[2]
        x = pos[0]
        # theta1
        alpha = np.arctan2(y,x)

        d = np.sqrt(x**2+y*2)
        cos_theta1a = (self.L[0]**2+d**2-self.L[1]**2)/(2*self.L[0]*d)
        # a_sin_theta1a = np.sqrt(1 - cos_theta1a ** 2)
        # b_sin_theta1a = -a_sin_theta1a
        # a_theta1a = np.arctan2(a_sin_theta1a, cos_theta1a)
        # b_theta1a = np.arctan2(b_sin_theta1a, cos_theta1a)
        theta1a = np.arccos(cos_theta1a)
        theta1 = theta1a+alpha
        # theta2
        cos_theta2 = (d**2 - self.L[0]**2-self.L[1]**2)/(2*self.L[0]*self.L[1])
        theta2 = np.arccos(cos_theta2)
        # theta3
        theta3 = pi/2+theta2-theta1
        q = [np.arctan(np.tan(i)) for i in [theta1,theta2,theta3]]
        deg =  [theta*180/pi for theta in q]
        return q,deg

if __name__ == '__main__':
    arm = Arm(L=[1,1,1])
    q = [ pi/2,-pi/2,pi/2]
    pos = arm.forward_kinematics(q)
    print(pos)
    # print(pos)
    q,deg = arm.inverse_kinematics(pos)
    print(arm.forward_kinematics(q))
    print(deg)