#!/usr/bin/python
# -*- coding:utf-8 -*-
import tushare as ts
import pymongo
import json
import datetime
from setting import settings


def get_today_all():
    """
    当前全市场实时数据，每五分钟取一次
    """
    df = ts.get_today_all()
    data = json.loads(df.to_json(orient='records'))

    mongo_client = pymongo.MongoClient(settings['MONGO_SERVER'], settings['MONGO_PORT'])
    db = mongo_client[settings['MONGO_DB']]
    table = db[settings['MONGO_TABLE_STOCK_TODAY_ALL']]
    table.insert(data)
    print datetime.datetime.now().ctime(), "当天实时数据存入数据库"


if __name__ == "__main__":
    get_today_all()

