#!/usr/bin/python
# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import math


def fun1():
    np.random.seed(1000)
    y = np.random.standard_normal(10)
    print "y = %s" % y
    x = range(len(y))
    print "x=%s" % x
    plt.plot(y)
    plt.show()


# 操纵坐标轴和增加网格及标签的函数
def fun2():
    np.random.seed(1000)
    y = np.random.standard_normal(10)
    print "y = %s" % y
    plt.plot(y.cumsum())
    plt.grid(True)  # 增加格点
    plt.axis('tight')  # 坐标轴适应数据量 axis 设置坐标轴
    plt.show()


# plt.xlim 和 plt.ylim 设置每个坐标轴的最小值和最大值
def fun3():
    np.random.seed(1000)
    y = np.random.standard_normal(20)
    plt.plot(y.cumsum())
    plt.grid(True)  ##增加格点
    plt.xlim(-1, 20)
    plt.ylim(np.min(y.cumsum()) - 1, np.max(y.cumsum()) + 1)

    plt.show()


# 添加标题和标签 plt.title, plt.xlabe, plt.ylabel 离散点, 线
def fun4():
    np.random.seed(1000)
    y = np.random.standard_normal(20)

    plt.figure(figsize=(7, 4))  # 画布大小
    plt.plot(y.cumsum(), 'b', lw=1.5)  # 蓝色的线
    plt.plot(y.cumsum(), 'ro')  # 离散的点
    plt.grid(True)
    plt.axis('tight')
    plt.xlabel('index')
    plt.ylabel('value')
    plt.title('A simple Plot')
    plt.show()


# 两个数据集绘图
def fun5():
    np.random.seed(2000)
    y = np.random.standard_normal((10, 2))
    print y
    plt.figure(figsize=(7, 5))
    plt.plot(y, lw=1.5)
    plt.plot(y, 'ro')
    plt.grid(True)
    plt.axis('tight')
    plt.xlabel('index')
    plt.ylabel('value')
    plt.title('A simple plot1')
    plt.show()


# 添加图例 plt.legend(loc = 0)
def fun6():
    np.random.seed(2000)
    y = np.random.standard_normal((10, 2))
    plt.figure(figsize=(7, 5))
    plt.plot(y[:, 0], lw=1.5, label='1st')
    plt.plot(y[:, 1], lw=1.5, label='2st')
    plt.plot(y, 'ro')
    plt.grid(True)
    plt.legend(loc=0)  # 图例位置自动
    plt.axis('tight')
    plt.xlabel('index')
    plt.ylabel('value')
    plt.title('A simple plot')
    plt.show()


# 使用2个 Y轴(左右)fig, ax1 = plt.subplots() ax2 = ax1.twinx()
def fun7():
    np.random.seed(2000)
    y = np.random.standard_normal((10, 2))

    fig, ax1 = plt.subplots()  # 关键代码1 plt first data set using first (left) axis

    plt.plot(y[:, 0], lw=1.5, label='1st')

    plt.plot(y[:, 0], 'ro')
    plt.grid(True)
    plt.legend(loc=0)  # 图例位置自动
    plt.axis('tight')
    plt.xlabel('index')
    plt.ylabel('value')
    plt.title('A simple plot')

    ax2 = ax1.twinx()  # 关键代码2  plt second data set using second(right) axis
    plt.plot(y[:, 1], 'g', lw=1.5, label='2nd')
    plt.plot(y[:, 1], 'ro')
    plt.legend(loc=0)
    plt.ylabel('value 2nd')
    plt.show()


# 使用两个子图(上下,左右)plt.subplot(211)
def fun8():
    np.random.seed(2000)
    y = np.random.standard_normal((10, 2))

    plt.figure(figsize=(7, 5))
    plt.subplot(211)  # 两行一列,第一个图
    plt.plot(y[:, 0], lw=1.5, label='1st')
    plt.plot(y[:, 0], 'ro')
    plt.grid(True)
    plt.legend(loc=0)  # 图例位置自动
    plt.axis('tight')
    plt.ylabel('value')
    plt.title('A simple plot')

    plt.subplot(212)  # 两行一列.第二个图
    plt.plot(y[:, 1], 'g', lw=1.5, label='2nd')
    plt.plot(y[:, 1], 'ro')
    plt.grid(True)
    plt.legend(loc=0)
    plt.xlabel('index')
    plt.ylabel('value 2nd')
    plt.axis('tight')
    plt.show()


# 左右子图
def fun9():
    np.random.seed(2000)
    y = np.random.standard_normal((10, 2))

    plt.figure(figsize=(10, 5))
    plt.subplot(121)  # 两行一列,第一个图
    plt.plot(y[:, 0], lw=1.5, label='1st')
    plt.plot(y[:, 0], 'ro')
    plt.grid(True)
    plt.legend(loc=0)  # 图例位置自动
    plt.axis('tight')
    plt.xlabel('index')
    plt.ylabel('value')
    plt.title('1st Data Set')

    plt.subplot(122)
    plt.bar(np.arange(len(y)), y[:, 1], width=0.5, color='g', label='2nc')
    plt.grid(True)
    plt.legend(loc=0)
    plt.axis('tight')
    plt.xlabel('index')
    plt.title('2nd Data Set')
    plt.show()

# 散点图 scatter
def fun10():
    np.random.seed(2000)
    y = np.random.standard_normal((1000, 2))
    plt.figure(figsize=(7, 5))
    plt.scatter(y[:, 0], y[:, 1], marker='o')
    plt.grid(True)
    plt.xlabel('1st')
    plt.ylabel('2nd')
    plt.title('Scatter Plot')
    plt.show()

if __name__ == "__main__":
    # fun1()
    # fun2()
    # fun3()
    # fun4()
    # fun5()
    # fun6()  https://www.cnblogs.com/chaoren399/p/5792168.html
    fun10()
