import Arm
from numpy import pi
import numpy as np
def me_round(x):
    return np.round(x, decimals=3)
arm = Arm.Arm3Link(L=[1,1,1])
print(list(map(me_round,arm.get_xy([pi/3, pi/4 ,pi/2]))))
a = arm.inv_kin([-0.725, 1.573])
print(list(map(me_round,arm.get_xy(a))))
print(a)
tan = list(map(np.tan,a))
p = list(map(np.arctan,tan))
print(list(i*180/pi for i in p))
