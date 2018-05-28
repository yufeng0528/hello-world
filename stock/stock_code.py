#!/usr/bin/python
# -*- coding:utf-8 -*-
import tushare as ts
import pymongo
import json
import quantbase
from setting import settings


def init_stock_code():
    """
    基本面数据
    :return:
    """
    df = ts.get_stock_basics()
    # 重设索引
    data = json.loads(df.reset_index().to_json(orient='records'))
    # f = file('log3.txt', "wb")
    # f.write(json.dumps(data))
    # f.close()

    # print data
    # df.to_csv(path_or_buf='d/log.txt')

    table = quantbase.get_mongo_table_instance(settings['MONGO_TABLE_STOCK_BASIC'])
    for stock in data:
        table.update({"code": stock.get("code")}, stock, True)

    print "股票代码存入数据库"


if __name__ == "__main__":
    init_stock_code()
