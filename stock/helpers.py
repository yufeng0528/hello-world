# coding:utf8
import json
import os
import re

import requests

STOCK_CODE_PATH = 'stock_codes.conf'


def update_stock_codes():
    """获取所有股票 ID 到 all_stock_code 目录下"""
    all_stock_codes_url = 'http://www.shdjt.com/js/lib/astock.js'
    grep_stock_codes = re.compile('~(\d+)`')
    response = requests.get(all_stock_codes_url)
    all_stock_codes = grep_stock_codes.findall(response.text)
    with open(stock_code_path(), 'w') as f:
        f.write(json.dumps(dict(stock=all_stock_codes)))


def get_stock_codes(realtime=False):
    """获取所有股票 ID 到 all_stock_code 目录下"""
    if realtime:
        all_stock_codes_url = 'http://www.shdjt.com/js/lib/astock.js'
        grep_stock_codes = re.compile('~(\d+)`')
        response = requests.get(all_stock_codes_url)
        stock_codes = grep_stock_codes.findall(response.text)
        with open(stock_code_path(), 'w') as f:
            f.write(json.dumps(dict(stock=stock_codes)))
        return stock_codes
    else:
        with open(stock_code_path()) as f:
            return json.load(f)['stock']


def stock_code_path():
    return os.path.join(os.path.dirname(__file__), STOCK_CODE_PATH)


def get_stock_type(stock_code):
    """判断股票ID对应的证券市场
    匹配规则
    ['50', '51', '60', '90', '110'] 为 sh
    ['00', '13', '18', '15', '16', '18', '20', '30', '39', '115'] 为 sz
    ['5', '6', '9'] 开头的为 sh， 其余为 sz
    :param stock_code:股票ID, 若以 'sz', 'sh' 开头直接返回对应类型，否则使用内置规则判断
    :return 'sh' or 'sz'"""
    if stock_code.startswith(('sh', 'sz')):
        return stock_code[:2]
    if stock_code.startswith(('50', '51', '60', '90', '110', '113', '132', '204')):
        return 'sh'
    if stock_code.startswith(('00', '13', '18', '15', '16', '18', '20', '30', '39', '115', '1318')):
        return 'sz'
    if stock_code.startswith(('5', '6', '9', '7')):
        return 'sh'
    return 'sz'
