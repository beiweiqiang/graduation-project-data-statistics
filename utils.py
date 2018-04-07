#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import datetime

ts = time.time()


def get_now_timestamp():
    return datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')


if __name__ == '__main__':
    print(get_now_timestamp())
