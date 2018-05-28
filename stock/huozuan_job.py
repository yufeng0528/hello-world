#!/usr/bin/python
# -*- coding:utf-8 -*-
from apscheduler.schedulers.background import BackgroundScheduler
import datetime
from stock_today_all import *
from stock_history import *
from stock_code import *
import logging
import time


log = logging.getLogger('apscheduler.executors.default')
log.setLevel(logging.INFO)  # DEBUG

fmt = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
h = logging.StreamHandler()
h.setFormatter(fmt)
log.addHandler(h)
sched = BackgroundScheduler()
sched.daemonic = True


@sched.scheduled_job('cron', day_of_week='mon-fri', hour='10,11,13,14', minute='*/5')
def stock_runtime_job():
    get_today_all_sina()


@sched.scheduled_job('cron', day_of_week='mon-fri', hour='9', minute='30-59/5')
def stock_runtime_job():
    get_today_all_sina()


@sched.scheduled_job('cron', day_of_week='mon-fri', hour='15', minute='5')
def stock_runtime_job():
    get_today_all_sina()


@sched.scheduled_job('cron', day_of_week='mon-fri', hour='15', minute='35')
def stock_history_job():
    get_last_day()


@sched.scheduled_job('cron', day_of_week='mon-fri', hour='15', minute='35')
def stock_history_job():
    init_stock_code()


sched.start()

while True:
    time.sleep(10)

