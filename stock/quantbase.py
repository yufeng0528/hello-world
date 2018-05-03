#!/usr/bin/python
# -*- coding:utf-8 -*-

import pymongo
import datetime
import time
from setting import settings
import random


def print_marker(marker):
    strTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S');
    print (marker + strTime)
    
    
def sleep_random():
    x = random.randint(3, 7)
    time.sleep(x)
    
    
def get_mongo_table_instance(tablename):
    mongo_client = pymongo.MongoClient(settings['MONGO_SERVER'], settings['MONGO_PORT'])
    db = mongo_client[settings['MONGO_DB']]
    db.authenticate(settings['MONGO_DB_USER'], settings['MONGO_DB_PSW'])
    table = db[tablename]
    return table

    
def get_years_split():
    beginYear = settings['BEGIN_YEAR']
    curYear = datetime.datetime.now().year;
    curMonth = datetime.datetime.now().month
    
    ret = []
    
    for year in range(beginYear, curYear + 1):
        if (year == curYear):
            if (curMonth >= 4):
                ret.append(str(year) + '.1')
            if (curMonth >= 7):
                ret.append(str(year) + '.2')
            if (curMonth >= 10):
                ret.append(str(year) + '.3')
        else:
            ret.append(str(year) + '.1')
            ret.append(str(year) + '.2')
            ret.append(str(year) + '.3')
            ret.append(str(year) + '.4')
            
    return ret   
            

def gen_random_charactor_str(size):
    seed = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' 
    strret = ''
    
    for i in range(0, size):
        x = random.randint(0, len(seed) - 1)
        c = seed[x]
        strret = strret + c
        
    return strret
    
    