#!/usr/bin/python
# -*- coding:utf-8 -*-
import urllib2
import pymongo
import json

# http请求
def get_data_from_server(strurl, bKeepResposeOriginal=False):
    if strurl is None or len(strurl) == 0:
        return None

    strresponse = None
    header = {"User-Agent": "finbtc/1.9.0 (iPhone; iOS 11.4; Scale/3.00)",
               "device": "39D337E6-8804-4A02-8357-B41A212E8810",
               "X-App-Info" : "1.9.0/appstore/ios",
               "token": "c7fb7b63f909497eaac0c834404519f3"}

    try:
        request = urllib2.Request(url=strurl, headers=header)
        response = urllib2.urlopen(request, timeout=60)
        if response is not None:
            strresponse = response.read()
    except Exception, e:
        print Exception, ":", e
        print 'error when scrawling: ', strurl

    if strresponse is None or len(strresponse) == 0:
        return None

    return strresponse

def save(coin_info):
    mongo_client = pymongo.MongoClient('127.0.0.1', 27017)
    db = mongo_client['coin']
    db.authenticate('root1', '123456')
    table = db['coin_info']
    table.update({'cid': code_info.get('cid')}, code_info, upsert=True)


if __name__ == "__main__":
    for i in range(1, 3000):
        info = get_data_from_server("https://api.finbtc.net/app//coin/detail/jk?coinId=" + str(i))
        print info
        info = json.loads(info)
        code_info = info.get('data')
        code_info['cid'] = i;
        save(code_info)