#!/usr/bin/python
# -*- coding:utf-8 -*-
from apscheduler.schedulers.blocking import BlockingScheduler
import datetime
from stock_today_all import *
from stock_history import *
import logging


logging.basicConfig()
sched = BlockingScheduler()


@sched.scheduled_job('cron', day_of_week='mon-fri', hour='9-16', minute='0-59', second='*/30')
def stock_runtime_job():
    print datetime.datetime.now()
    print("stock_runtime_job start>>>")
    get_today_all()
    print("stock_runtime_job end<<<")


@sched.scheduled_job('cron', day_of_week='mon-fri', hour='17', minute='5')
def stock_history_job():
    print datetime.datetime.now()
    print("stock_history_job start>>>")
    get_last_day()
    print("stock_history_job end<<<")

sched.start()

