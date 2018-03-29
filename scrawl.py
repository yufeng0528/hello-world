#!/usr/bin/python
# -*- coding:utf-8 -*-
import tushare as ts
import pymongo
import json

settings={
          "MONGO_SERVER": "localhost",
          "MONGO_PORT": 27017,
          "MONGO_DB": "testdb",
          "MONGO_TABLE": "stock_history_d"
          }

def test():
    df = ts.get_hist_data("510050")
    print(df)


def get_history():
    df = ts.get_k_data(code="600100", start="2009-01-01", end="2010-01-01", ktype="D", autype="hfq", index=False, retry_count=3, pause=0.001)
    data = json.loads(df.to_json(orient='records'))

    mongo_client = pymongo.MongoClient(settings['MONGO_SERVER'], settings['MONGO_PORT'])
    db = mongo_client[settings['MONGO_DB']]
    table = db[settings['MONGO_TABLE']]
    table.insert(data)


if __name__ == "__main__":
    get_history()
