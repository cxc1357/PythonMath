import numpy as np
from numpy.core.fromnumeric import reshape
import pandas as pd
import matplotlib.pyplot as plt

# 导数与斜率
if 0:
    def f(x):
        return x**2
    
    plt.figure(figsize=(12,6))
    n = np.linspace(-10 , 10 , num = 50)

    plt.plot(n,f(n))
    plt.xlim(-10,10)

    plt.plot([2,5],[4,25],color='r')

    x_m = 2
    for i in range(1,5):
        plt.plot([x_m,x_m+i],[f(x_m),f(x_m+i)],color = 'r')

    plt.show()
    pass

# 求导数
if 0:
    def f(x):
        return x ** 2

    def ds(x,d):
        y1 = f(x)
        y2 = f(x+d)
        return (y2-y1)/d

    for i in np.linspace(1,0,num=1000,endpoint=False):
        ret = ds(2,i)
        print("当2偏{:3f}个单位时，直线斜率是{:.3f}".format(i,ret)) 
    pass   

# 画图
if 0:
    def f(x):
        return x**2
    
    n = np.linspace(-10,10,num=50)
    plt.plot(n,f(n))

    plt.scatter(2,4)
    plt.plot(n,4*n-4)

    plt.show()
    pass

# 函数单调性，凹凸性
if 0:
    def f1(x):
        return 2*x**3 - 9*x**2 + 12*x -3
    x = np.linspace(-10,10,num=100)
    plt.plot(x,f1(x))
    
    plt.axvline(0,color = 'gray',linestyle='--',alpha =0.8)
    plt.axvline(0,color = 'gray',linestyle='--',alpha =0.8)

    plt.show()
    pass
    

# 二分法
if 0:
    def f(x):
        return x**3 + 1.1*x**2 + 0.9*x -1.4
    x = np.linspace(-10,10,num=100)
    plt.plot(x,f(x))
    plt.axvline(0,color = 'cyan',linestyle='--')
    plt.axhline(0,color = 'cyan',linestyle='--')
    res_ls=[0,1]
    for i in range(10):
        mid = (res_ls[0] + res_ls[1])/2
        if f(mid)*f(0) < 0:
            res_ls[1] = mid
        else:
            res_ls[0] = mid
        print("第{}次循环，此时区间为{}!".format(i+1,res_ls))
    pass

# 切线法
if 1:
    def f(x):
        return x**3 + 1.1*x**2 + 0.9*x -1.4
    
    plt.xlim([0,1])
    plt.ylim([f(0),f(1)])

    x = np.linspace(0,1,num=100)
    plt.axvline(0,color='cyan',linestyle='--')
    plt.axhline(0,color='cyan',linestyle='--')
    plt.plot(x,f(x))

    res = 1
    def f_1(x):
        return 3*x**2 + 2.2*x + 0.9

    for i in range(3):
        p_Pre = res
        # x = x0 - f(x0)/f'(x0)
        res = res - f(res)/f_1(res)
        print("第{}次循环的估计值为{}".format(i+1,res))
        # plot([x0,x1],[y0,y1])
        plt.plot([p_Pre,res],[f(p_Pre),0])
    pass
    plt.show()


