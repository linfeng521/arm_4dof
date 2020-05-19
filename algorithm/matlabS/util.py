import numpy as np


# 提供了常见函数工具包的接受数组参数版本
def meround(a, deci=2):
    '''
    :param a: list,
    '''
    return [round(i, deci) for i in a]


def rad2deg(rads):
    return meround([np.rad2deg(rad) for rad in rads],0)


def deg2rad(degs):
    return meround([np.deg2rad(deg) for deg in degs],0)

# 转换二维rad矩阵到deg矩阵
def rad2degS(radss):
    '''

    :param radss: 2nd ndarry rad
    :return: 2nd ndarry degree
    '''
    result = []
    for rads in radss:
        result.append(rad2deg(rads))
    return result
