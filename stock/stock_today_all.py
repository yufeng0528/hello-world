#!/usr/bin/python
# -*- coding:utf-8 -*-
import tushare as ts
import pymongo
import json
import datetime
from setting import settings
import quantbase
from sina import Sina
import helpers


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

    # dg = ts.get_k_data(stock, ktype='5', start=date, end='2017-12-31', autype='qfq')


def get_today_all_sina():
    """
    当前全市场实时数据，每五分钟取一次
    """
    table = quantbase.get_mongo_table_instance(settings['MONGO_TABLE_STOCK_CODE'])
    code_list = table.find({"ipodate":{"$ne":"-"}}, {"scode":-1})
    sina = Sina()

    stock_codes = [code.get("scode") for code in code_list]
    stock_codes = sina.gen_stock_list(stock_codes)

    table = quantbase.get_mongo_table_instance(settings['MONGO_TABLE_STOCK_TODAY_ALL'])
    stock_day_data = sina.get_stock_data(stock_codes)
    for item in stock_day_data:
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
    get_today_all_sina()

