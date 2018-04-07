#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import datetime
import jieba
from collections import Counter
import json

ts = time.time()


# 获取当前时间戳
def get_now_timestamp():
    return datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')


# 将只有一项的 tuple 的 list集合, 去 tuple 变成纯 list
def tuple_to_list(l):
    array = []
    for i in l:
        array.append(i[0])
    return array


# list 里面包含 tuple, 每个tuple, 第一个元素作为k, 第二个元素作为v
def tuple_to_map(l):
    obj = {}
    for (k, v) in l:
        obj[k] = v
    return obj


# 输入一句话, 输出一个dict 词频Map
def sentence_to_frequency_dict(s):
    # 统计词频
    c = Counter()

    if type(s) == list:
        for i in s:
            seg_list = jieba.cut(i)
            for x in seg_list:
                if len(x) > 1:
                    c[x] += 1
    else:
        seg_list = jieba.cut(s)
        for x in seg_list:
            if len(x) > 1:
                c[x] += 1
    obj = {}
    for (k, v) in c.most_common():
        obj[k] = v
    return obj


# dict 转换为 json 字符串
def dict_to_json_str(obj):
    return json.dumps(obj, ensure_ascii=False)


if __name__ == '__main__':
    print(get_now_timestamp())
    sentence_to_frequency_dict("测试")
    sentence_to_frequency_dict(["测试1", "测试33"])
