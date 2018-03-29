#!/usr/bin/python
# -*- coding:utf-8 -*-
import tushare as ts
import pymongo
import json
from setting import settings


def init_stock_code():
    """
    基本面数据
    :return:
    """
    df = ts.get_stock_basics()

    data = json.loads(df.to_json(orient='records'))
    mongo_client = pymongo.MongoClient(settings['MONGO_SERVER'], settings['MONGO_PORT'])
    db = mongo_client[settings['MONGO_DB']]
    table = db[settings['MONGO_TABLE_STOCK_BASIC']]
    table.insert(data)
    print "股票代码存入数据库"


if __name__ == "__main__":
    init_stock_code()
