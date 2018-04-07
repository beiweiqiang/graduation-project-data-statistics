#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import type0
import type1


def job():
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    type0.run()
    type1.run()


# 定义BlockingScheduler
sched = BlockingScheduler()
sched.add_job(job, 'interval', seconds=10)
sched.start()



