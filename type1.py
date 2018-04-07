#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import connect
import utils

conn = connect.conn


def run():
    # 运行查询:
    cursor = conn.cursor()
    cursor.execute('select distinct user_id from user_chatting_history')
    values = cursor.fetchall()
    user_ids = []
    for i in values:
        user_ids.append(i[0])

    all_user_message = []
    for i in user_ids:
        cursor.execute('select message_content from user_chatting_history where user_id=%s and message_type=0', (i,))
        message_list = utils.tuple_to_list(cursor.fetchall())
        all_user_message.append(message_list)

    frequency_list = []
    for i in all_user_message:
        frequency_list.append(utils.sentence_to_frequency_dict(i))

    for index, i in enumerate(user_ids):
        cursor.execute(
            'insert into data_statistics (user_id, value, create_time, type) values (%s, %s, %s, 1)',
            (i, utils.dict_to_json_str(frequency_list[index]), utils.get_now_timestamp())
        )
    conn.commit()

    print('type1 complete!')
    # 关闭Cursor:
    cursor.close()
    # 连接不能关闭
    # conn.close()


if __name__ == '__main__':
    run()


