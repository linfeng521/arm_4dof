import numpy as np


# 提供了常见函数工具包的接受数组参数版本
def meround(a, deci=2):
    '''

    :param a: list,
    :param deci:
    :return:
    '''
    return [round(i, deci) for i in a]


def rad2deg(rads):
    return meround([np.rad2deg(rad) for rad in rads],0)


def deg2rad(degs):
    return meround([np.deg2rad(deg) for deg in degs],0)
