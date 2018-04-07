#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import connect
import utils

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
    obj = utils.sentence_to_frequency_dict(all_message)

    cursor.execute(
        'insert into data_statistics (user_id, value, create_time, type) values (0, %s, %s, 0)',
        (utils.dict_to_json_str(obj), utils.get_now_timestamp())
    )
    conn.commit()

    print('type0 complete!')
    # 关闭Cursor:
    cursor.close()
    # 连接不能关闭
    # conn.close()


if __name__ == '__main__':
    run()


