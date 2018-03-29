#!/usr/bin/python
# -*- coding:utf-8 -*-
import tushare as ts


def test():
    df = ts.get_hist_data("510050")
    print(df)


if __name__ == "__main__":
    test()
