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
    # 所有用户的 id
    user_ids = utils.tuple_to_list(values)

    result_list = []
    for i in user_ids:
        cursor.execute(
            'select distinct group_name from user_chatting_history where user_id=%s and message_type=1',
            (i,)
        )
        group_name_list = utils.tuple_to_list(cursor.fetchall())
        obj = {}
        for g in group_name_list:
            cursor.execute(
                'select message_content from user_chatting_history where user_id=%s and message_type=1 and group_name=%s',
                (i, g)
            )
            message_list = utils.tuple_to_list(cursor.fetchall())
            frequency = utils.sentence_to_frequency_dict(message_list)
            obj[g] = frequency
        result_list.append(obj)

    for index, i in enumerate(user_ids):
        cursor.execute(
            'insert into data_statistics (user_id, value, create_time, type) values (%s, %s, %s, 5)',
            (i, utils.dict_to_json_str(result_list[index]), utils.get_now_timestamp())
        )
    conn.commit()

    print('type5 complete!')
    # 关闭Cursor:
    cursor.close()
    # 连接不能关闭
    # conn.close()


if __name__ == '__main__':
    run()


