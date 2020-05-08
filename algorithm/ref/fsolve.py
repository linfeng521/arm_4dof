from scipy.optimize import fsolve
from scipy.optimize import root
import numpy as np

# 非齐次方程
def func(x):
    return x ** 4 - x - 5
x_root = root(func, 0)
x_fsolve = fsolve(func, 0)
print(x_root.x)
print(x_fsolve)
print(x_fsolve[0]**4-x_fsolve[0])

def f2(x):
    return np.array([3*x[0]+2*x[1]-3,x[0]-2*x[1]-5])


sol2_root = root(f2,[0,0])
print(sol2_root)