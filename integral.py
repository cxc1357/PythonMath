import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 定积分
if 1:
    def f(x):
        return x**2
    
    x = np.linspace(-1,2)
    plt.plot(x,f(x))
    plt.axhline(0,color='cyan',linestyle='--')
    plt.axvline(0,color='cyan',linestyle='--')
    plt.axvline(1,color='cyan',linestyle='--')

    # 默认分50份
    x1 = np.linspace(0,1)
    # 覆盖区域,上限，下限
    plt.fill_between(x1,0,f(x1),color='k',alpha=0.4)
    plt.show()

    # 积分计算区域面积
    # 注意区分[-1],[:-1]和[::-1]，分别代表取最后一个元素，取最后一个元素之前的元素，倒序
    area = 0
    
    # 输出前49项
    for i in range(len(x1))[:-1]:
        mid_idx = (x1[i] + x1[i+1])/2
        area += (x1[i+1]-x1[i])*f(mid_idx)
    print(area)
    pass


