import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

# 幂函数
# linespace：生成x1,x2间的N点行线性矢量

if 0:
    x = np.linspace(-np.pi,2*np.pi,num = 50)
    y = x**2

    plt.scatter(x,y,marker='.')
    plt.plot(x,y)

    plt.axvline(0 , color='cyan' , linestyle='--' , alpha = 0.8)
    plt.axhline(0 , color = 'cyan' , linestyle='--', alpha = 0.8)

    plt.show()

# 指数函数

if 0:
    x = np.linspace(-np.pi,2*np.pi,num = 50)
    y = 2**x

    plt.scatter(x,y,marker='.')
    plt.plot(x,y)

    plt.axvline(0 , color='cyan' , linestyle='--' , alpha = 0.8)
    plt.axhline(0 , color = 'cyan' , linestyle='--', alpha = 0.8)

    plt.show()

# 对数函数

if 0:
    x = np.linspace(-np.pi,2*np.pi,num = 50)
    y = np.log2(x)

    plt.scatter(x,y,marker='.')
    plt.plot(x,y)

    plt.axvline(0 , color='cyan' , linestyle='--' , alpha = 0.8)
    plt.axhline(0 , color = 'cyan' , linestyle='--', alpha = 0.8)

    plt.show()

# 三角函数

if 0:
    x = np.linspace(-np.pi,2*np.pi,num = 50)
    y = np.sin(x)

    plt.scatter(x,y,marker='.')
    plt.plot(x,y)

    plt.axvline(0 , color='cyan' , linestyle='--' , alpha = 0.8)
    plt.axhline(0 , color = 'cyan' , linestyle='--', alpha = 0.8)

    plt.show()

# 反三角函数

if 1:
    x = np.linspace(-np.pi,2*np.pi,num = 100)
    y = np.arccos(x)

    plt.scatter(x,y,marker='.')
    plt.plot(x,y)

    plt.axvline(0 , color='cyan' , linestyle='--' , alpha = 0.8)
    plt.axhline(0 , color = 'cyan' , linestyle='--', alpha = 0.8)

    plt.show()