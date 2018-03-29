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
    table = db[settings['MONGO_TABLE_HISTORY']]
    table.insert(data)
    print code,  "from", start, "to", end, "存入数据库"


def get_one(index=0):
    mongo_client = pymongo.MongoClient(settings['MONGO_SERVER'], settings['MONGO_PORT'])
    db = mongo_client[settings['MONGO_DB']]
    table = db[settings['MONGO_TABLE_STOCK_BASIC']]
    row = table.find().limit(1).skip(index)[0]
    return row.get("code"), row.get("timeToMarket")


if __name__ == "__main__":
    # init_history('600100', '2009-01-01', '2009-02-01')
    stock_code, date_int = get_one(0)
    year_start = date_int/10000
    year_max = 2019
    for year in range(year_start, year_max):
        # print str(year) + '-01-01', str(year) + '-12-31'
        init_history(stock_code, str(year) + '-01-01', str(year) + '-12-31')

