#!/usr/bin/python
# -*- coding:utf-8 -*-
import tushare as ts
import pymongo
import json
import datetime
from setting import settings
import quantbase


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
    if len(data) == 0:
        print code, "from", start, "to", end, "没有数据"
        return

    table = quantbase.get_mongo_table_instance(settings['MONGO_TABLE_HISTORY'])
    table.insert(data)
    print code,  "from", start, "to", end, "存入数据库"


def get_one(index=0):
    mongo_client = pymongo.MongoClient(settings['MONGO_SERVER'], settings['MONGO_PORT'])
    db = mongo_client[settings['MONGO_DB']]
    db.authenticate(settings['MONGO_DB_USER'], settings['MONGO_DB_PSW'])
    table = db[settings['MONGO_TABLE_STOCK_BASIC']]
    table = quantbase.get_mongo_table_instance(settings['MONGO_TABLE_HISTORY'])
    row = table.find().limit(1).skip(index)[0]
    return row.get("code"), row.get("timeToMarket")


def get_last_day():
    mongo_client = pymongo.MongoClient(settings['MONGO_SERVER'], settings['MONGO_PORT'])
    db = mongo_client[settings['MONGO_DB']]
    db.authenticate(settings['MONGO_DB_USER'], settings['MONGO_DB_PSW'])
    table = db[settings['MONGO_TABLE_STOCK_BASIC']]
    rows = table.find()
    for row in rows:
        stock_code = row.get("code")
        today = datetime.date.today()
        init_history(stock_code, str(today), str(today))


if __name__ == "__main__":
    # init_history('600100', '2009-01-01', '2009-02-01')

    get_last_day()

    # stock_code, date_int = get_one(0)
    # year_start = date_int/10000
    # year_max = 2019
    # for year in range(year_start, year_max):
    #     # print str(year) + '-01-01', str(year) + '-12-31'
    #     init_history(stock_code, str(year) + '-01-01', str(year) + '-12-31')

