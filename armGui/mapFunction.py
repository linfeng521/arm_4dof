
# 映射字典
di = {
    'waist': {0: 10, 90: 90, 180: 170},
    'shoulder': {0: 18, 90: 90, 180: 170},
    'elbow': {0: 10, 90: 90, 180: 180},
    'wrist': {0: 0, 90: 70, 180: 150},
}

body = ['waist','shoulder','elbow', 'wrist']
# 将 N 区间上的数映射到 O 区间
'''
计算出O区间长度除以N区间长度，得出N区间上单位长度对应于O区间上的大小，
再将N区间上每个数减去N区间最小值后乘以单位区间对应的长度，
最后加上O区间的最小值，实现投射到N区间上。
'''


def map_value(Nmax, Nmin, Omax, Omin, Nx):
    return ((Omax - Omin) / (Nmax - Nmin)) * (Nx - Nmin) + Omin


def actually(bodyId, idea_degree):
    m = di[body[bodyId]]
    if idea_degree <= 90:
        actually_degree =  map_value(90, 0, m.get(90), m.get(0), idea_degree)
    else:
        actually_degree = map_value(180, 90, m.get(180), m.get(90), idea_degree)
    return round(actually_degree)

# 线性回归问题解决
def grip(length):
    return round((76.98 - int(length)) / 0.75)

if __name__ == '__main__':
    print(actually(1, 90))
    print(grip(22))
