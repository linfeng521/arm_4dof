from numpy import cos, sin, pi
import numpy as np
import scipy.optimize


class Arm4Link:

    def __init__(self, q=None, q0=None, L=None):
        """Set up the basic parameters of the arm.
        All lists are in order [blow , shoulder, elbow, wrist].

        q : np.array
            the initial joint angles of the arm
        q0 : np.array
            the default (resting state) joint configuration
        self.L : np.array
            the arm segment lengths
        """
        # initial joint angles
        self.q = [1.57, 1.05, 1.57, -1.57] if q is None else q
        # some default arm positions
        self.q0 = np.array([1.57, 1.05, 1.57, -1.57]) if q0 is None else q0
        # arm segment lengths
        self.L = np.array([1, 1, 1, 1]) if L is None else L

        self.max_angles = [np.pi, np.pi, np.pi / 4]
        self.min_angles = [0, 0, -np.pi / 4]

    def forward_kinematics(self, q=None):
        if q is None:
            q = self.q
        x = cos(q[0]) * (self.L[2] * cos(q[1] + q[2]) + self.L[1] * cos(q[1]) + self.L[3] * cos(
            q[1] + q[2] + q[3]))
        y = sin(q[0]) * (self.L[2] * cos(q[1] + q[2]) + self.L[1] * cos(q[1]) + self.L[3] * cos(
            q[1] + q[2] + q[3]))
        z = self.L[0] + self.L[2] * sin(q[1] + q[2]) + self.L[1] * sin(q[1]) + self.L[3] * sin(
            q[1] + q[2] + q[3])
        return [x, y, z]

    def inv_kin(self, x, y, z):

        '''
        :param x y z: 末端执行器到达的位置坐标
        :return: 优化函数(即目标函数)thea1,theat2,theta3,theta4
        '''

        def distance_to_default(q, *args):
            weight = [1.3, 1.5, 1, 1]
            return np.sqrt(np.sum([(qi - q0i) ** 2 * wi for qi, q0i, wi in zip(q, self.q0, weight)]))

        def constraint(q, x, y, z):
            return np.array(self.forward_kinematics(q)) - np.array([x, y, z])

        return scipy.optimize.fmin_slsqp(
            func=distance_to_default,
            x0=self.q,
            f_eqcons=constraint,
            args=(x, y, z),
            iprint=-1,
        bounds=[(0,pi),(0,pi),(0,pi),(0,pi/2)])  # iprint=0 suppresses output


def test():
    arm = Arm4Link()

    # set of desired (x,y) hand positions
    x = np.arange(-.75, .75, .05)
    y = np.arange(.25, .75, .05)

    # threshold for printing out information, to find trouble spots
    thresh = .025

    count = 0
    total_error = 0
    # test it across the range of specified x and y values
    for xi in range(len(x)):
        for yi in range(len(y)):
            # test the inv_kin function on a range of different targets
            xy = [x[xi], y[yi]]
            # run the inv_kin function, get the optimal joint angles
            q = arm.inv_kin(xy=xy)
            print(q)
            print('---test----')
            # find the (x,y) position of the hand given these angles
            actual_xy = arm.get_xy(q)
            print('---actural--')
            print(actual_xy)
            # calculate the root squared error
            error = np.sqrt(np.sum((np.array(xy) - np.array(actual_xy)) ** 2))
            # total the error
            total_error += np.nan_to_num(error)

            # if the error was high, print out more information
            if np.sum(error) > thresh:
                print('-------------------------')
                print('Initial joint angles', arm.q)
                print('Final joint angles: ', q)
                print('Desired hand position: ', xy)
                print('Actual hand position: ', actual_xy)
                print('Error: ', error)
                print('-------------------------')

            count += 1

    print('\n---------Results---------')
    print('Total number of trials: ', count)
    print('Total error: ', total_error)
    print('-------------------------')


if __name__ == '__main__':
    arm = Arm4Link()
    arm.q = [pi / 6, pi / 6, pi / 6, pi / 7]
    a = arm.forward_kinematics()
    b = [np.round(i, decimals=3) for i in a]
    print('正向运动学到达的位置: ', b)
    print('理论到达idea degree', [np.round(i, decimals=3) for i in arm.q])
    print("逆向运动学求解的度数", [np.round(i, decimals=3) for i in arm.inv_kin(a[0], a[1], a[2])])
