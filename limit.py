import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# import warnings
# warnings.filterwarnings('ignore')  #不发出警告

# 数列 x/(x+1) 的极限
# axhline(y=0.0, c="r", ls="--", lw=2)
# 水平参考线，y=0，红色，虚线，宽度2

#函数的极限
if 0:
    x  = np.arange(50)
    y = x/(x+1)

    plt.scatter(x,y,marker = '.')
    plt.plot(x,y)

    plt.axvline(0,color='cyan',linestyle='--',alpha = 0.8)
    plt.axhline(0,color='cyan',linestyle='--',alpha = 0.8)

    plt.show()

    pass

if 0:
    x = np.linspace(-2,2,num=100)
    y = x**2 -1

    plt.scatter(x,y,marker = '.')
    plt.plot(x,y)

    plt.axvline(0,color='cyan',linestyle='--')
    plt.axhline(0,color='cyan',linestyle='--')

    #极限值
    plt.axhline(-1,color='red',linestyle = '--')
    plt.show()
    pass

if 1:
    x = np.arange(1,50)
    y = (2*x+1)/x

    plt.scatter(x,y,marker = '.')
    plt.plot(x,y)

    plt.axhline(2,color='red',linestyle='--') 

    plt.show()
    pass