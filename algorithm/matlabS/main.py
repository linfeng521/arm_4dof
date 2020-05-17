# from . import arm
import arm
from numpy import pi
import util
import trajectory
from pprint import pprint
mearm = arm.Arm4Link(L=[68,105,97,110])
stedy_pos = [pi/2 ,pi/3, pi/2 ,-pi/2]
postion = mearm.forward_kinematics(stedy_pos)
degree = mearm.inv_kin(0,-126.7,262)

print('逆解后的角度',util.rad2deg(degree))
commands = trajectory.command_list(stedy_pos,degree,5,10)
pprint(commands)