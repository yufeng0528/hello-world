#!/usr/bin/python
# -*- coding:utf-8 -*-
import tushare as ts
import pymongo
import json
from setting import settings

def test():
    df = ts.get_hist_data("510050")
    print(df)


def init_history(code=None, start=None, end=None):
    """
    初始化数据，直接存入
    :param code: 股票代码
    :param start:开始时间，单位日
    :param end:结束时间，单位日
    :return:
    """
    df = ts.get_k_data(code=code, start=start, end=end, ktype="D", autype="hfq", index=False, retry_count=3, pause=0.001)
    data = json.loads(df.to_json(orient='records'))

    mongo_client = pymongo.MongoClient(settings['MONGO_SERVER'], settings['MONGO_PORT'])
    db = mongo_client[settings['MONGO_DB']]
    table = db[settings['MONGO_TABLE_STOCK_INFO']]
    table.insert(data)
    print code,  "from", start, "to", end, "存入数据库"


def get_one(index=0):
    mongo_client = pymongo.MongoClient(settings['MONGO_SERVER'], settings['MONGO_PORT'])
    db = mongo_client[settings['MONGO_DB']]
    table = db[settings['MONGO_TABLE_STOCK_BASIC']]
    row = table.find().limit(1).skip(index)
    print row.get("code")


if __name__ == "__main__":
    # init_history('600100', '2009-01-01', '2009-02-01')
    get_one(0)
