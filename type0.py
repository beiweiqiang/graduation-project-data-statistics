#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import connect
import jieba
from collections import Counter
import utils
import json

conn = connect.conn


def run():
    # 运行查询:
    cursor = conn.cursor()
    cursor.execute('select message_content from user_chatting_history')
    values = cursor.fetchall()
    all_message = []
    for i in values:
        all_message.append(i[0])

    # 统计词频
    c = Counter()
    for i in all_message:
        seg_list = jieba.cut(i)
        for x in seg_list:
            if len(x) > 1:
                c[x] += 1

    obj = {}
    for (k, v) in c.most_common():
        obj[k] = v
    print(obj)

    cursor = conn.cursor()
    cursor.execute(
        'insert into data_statistics (user_id, value, create_time, type) values (0, %s, %s, 0)',
        (json.dumps(obj, ensure_ascii=False), utils.get_now_timestamp())
    )
    conn.commit()

    # 关闭Cursor和Connection:
    cursor.close()
    conn.close()


if __name__ == '__main__':
    run()


