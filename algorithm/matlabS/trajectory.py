import numpy as np

'''
Trajectory planning
latex: q_i(t)=a_{i0}+a_{i1}(t)+a_{i2}(t^2)+a_{i3}(t^3)
满足边界条件: 
    q(0)=q0,q(tf)=qf
    初始位置速度为0 :diff(q(0))=0
    末端位置关节加速度为0: diff(diff(q(tf))=0
'''

# return [[a10 a11 a12 a13],[a20,a21,a22,a23]

def run(q0s, qfs, tf):
    '''
    :param q0s: 关节空间四自由度初始角度[pi/2 pi/2 pi/4 pi/4]
    :param qfs: 关节空间四自由度最终角度[pi/2 pi/2 pi/4 pi/4]
    :param tf: 经过时间长度
    :return: maritx[4][4] [[a10 a11 a12 a13],[a20,a21,a22,a23]
            qi(t)=ai0 + ai1*t + ai2*(t^2) + ai3* t^3
    '''
    ai = []
    for q0, qf in zip(q0s, qfs):
        bi = []
        bi.append(q0)
        bi.append(0)
        bi.append(3 * (qf - q0) / tf ** 2)
        bi.append(-2 * (qf - q0) / tf ** 3)
        ai.append(bi)
    return np.array(ai)

def command_list(q0s, qfs, tf,nums=50):
    step = tf/nums
    array = run(q0s, qfs, tf)
    commands = []
    for i in range(nums):
        t = step*i
        commands.append(array.dot([1,t,t**2,t**3]).tolist())
    return commands

# 位移曲线
# 速度曲线
# 加速度曲线
# 经过matlab仿真符合边界条件,故方程成立
if __name__ == '__main__':
    a = run([0, 1, 1, 0], [3, 3, 4, 3], 10)
    print(a)
