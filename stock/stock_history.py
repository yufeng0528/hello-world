#!/usr/bin/python
# -*- coding:utf-8 -*-
import tushare as ts
import pymongo
import json
from setting import settings

def test():
    df = ts.get_hist_data("510050")
    print(df)


def get_history(code=None, start=None, end=None):
    df = ts.get_k_data(code=code, start=start, end=end, ktype="D", autype="hfq", index=False, retry_count=3, pause=0.001)
    data = json.loads(df.to_json(orient='records'))
    print data

    mongo_client = pymongo.MongoClient(settings['MONGO_SERVER'], settings['MONGO_PORT'])
    db = mongo_client[settings['MONGO_DB']]
    table = db[settings['MONGO_TABLE']]
    table.insert(data)
    print code,  "from", start, "to", end, "存入数据库"


if __name__ == "__main__":
    get_history('600100', '2009-01-01', '2009-02-01')