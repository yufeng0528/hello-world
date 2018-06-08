#!/usr/bin/python
# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import math


def fun1():
    x = np.arange(0, 10, 0.1)

    y = x * 2

    plt.title(u"一元一次函数")
    plt.plot(x, y)

    plt.show()


def fun2():
    x = np.arange(-10, 10, 0.1)

    y = x ** 2 + 2 * x + 1

    plt.title(u"一元二次函数")
    plt.plot(x, y)
    plt.show()


def fun3():
    x = np.arange(0, 10, 0.1)

    y = 2 ** x

    plt.title(u"指数函数")
    plt.plot(x, y)
    plt.show()


def fun4():
    x = np.arange(0, 10, 0.1)

    e = math.e

    y = e ** x

    plt.title(u"自然对数函数")
    plt.plot(x, y)
    plt.show()


def fun5():
    x = np.linspace(-np.pi, np.pi, 100)

    y = np.sin(x)

    plt.title(u"正弦函数")
    plt.plot(x, y)
    plt.show()


if __name__ == "__main__":
    fun1()
    fun2()
    fun3()
    fun4()
    fun5()
