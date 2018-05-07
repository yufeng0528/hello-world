#!/usr/bin/python
# -*- coding:utf-8 -*-
import tushare as ts
import pymongo
import json
import datetime
from setting import settings
import quantbase


def get_today_all():
    """
    当前全市场实时数据，每五分钟取一次
    """
    df = ts.get_today_all()
    data = json.loads(df.to_json(orient='records'))

    table = quantbase.get_mongo_table_instance(settings['MONGO_TABLE_STOCK_TODAY_ALL'])
    for item in data:
        print item.get("code"), ".. save"
        table.update({"code":item.get("code")}, item, True)
    print datetime.datetime.now().ctime(), "当天实时数据存入数据库"


def get_day_all():
    """
    当前全市场实时数据，每五分钟取一次
    """
    df = ts.get_day_all()
    data = json.loads(df.to_json(orient='records'))

    table = quantbase.get_mongo_table_instance("stock_day_all")
    for item in data:
        print item.get("code"), ".. save"
        table.update({"code":item.get("code")}, item, True)
    print datetime.datetime.now().ctime(), "当天实时数据存入数据库"


if __name__ == "__main__":
    get_day_all()

