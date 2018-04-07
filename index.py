#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import type0
import type1
import type2
import type3
import type4
import type5


def job():
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    type0.run()
    type1.run()
    type2.run()
    type3.run()
    type4.run()
    type5.run()


# 定义BlockingScheduler
sched = BlockingScheduler()
sched.add_job(job, 'interval', seconds=20)
sched.start()
print('开始脚本')



