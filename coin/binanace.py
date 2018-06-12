#!/usr/bin/python
#-*- coding:utf-8 -*-
from binance.client import Client
from binance.enums import *

client = Client('',
                '')
# get market depth
depth = client.get_order_book(symbol='BTCUSDT')
print 'bids 买:---'
for item in depth.get('bids'):  # 买
    print item
print 'asks 卖:---'
for item in depth.get('asks'):  # 卖
    print item


# 成交
print '最近成交:---'
trades = client.get_recent_trades(symbol='BTCUSDT', limit=10)
for item in trades:
    print item

print '历史成交:---'
his_trades = client.get_historical_trades(symbol='BTCUSDT', limit=10, fromId=28457)
for item in his_trades:
    print item
print '下一页----'
his_trades = client.get_historical_trades(symbol='BTCUSDT', limit=10, fromId=28467)
for item in his_trades:
    print item

print '聚集成交---- 只能一小时内  2018-06-11 00:00:00~2018-06-11 01:00:00'
agg_trades = client.get_aggregate_trades(symbol='BTCUSDT', startTime=1528646400000, endTime=1528650000000)
for item in agg_trades:
    print item


print 'k线  1分钟-------   2018-06-11 00:00:00~2018-06-11 01:00:00'
k_lines = client.get_klines(symbol='BTCUSDT', interval=KLINE_INTERVAL_1MINUTE, startTime=1528646400000, endTime=1528650000000)
for item in k_lines:
    print item


print '历史k线  可以查询更多时间，就是上述方法的一个优化'
k_lines = client.get_historical_klines(symbol='BTCUSDT', interval=KLINE_INTERVAL_1MINUTE, start_str='1528646400000', end_str='1528650000000')
for item in k_lines:
    print item

print '24小时内价格---'
price_24hr = client.get_ticker(symbol='BTCUSDT')
print price_24hr


print ''
print '所有币对实时价格---'
price_all = client.get_all_tickers()
for item in price_all[:100]:
    print item

print ''
print '所有最佳报价----'
price_best = client.get_orderbook_tickers()
for item in price_best[:50]:
    print item
