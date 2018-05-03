#!/usr/bin/python
# -*- coding:utf-8 -*-
from apscheduler.schedulers.blocking import BlockingScheduler
import datetime
from stock_today_all import *

sched = BlockingScheduler()


@sched.scheduled_job('cron', day_of_week='mon-fri', hour='9-16', minute='0-59', second='*/15')
def stock_runtime_job():
    print datetime.datetime.now()
    print("stock_runtime_job start>>>")
    get_today_all()
    print("stock_runtime_job end<<<")


sched.start()

