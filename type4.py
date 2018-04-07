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
            'select distinct from_who from user_chatting_history where user_id=%s and message_type=0',
            (i,)
        )
        from_who_list = utils.tuple_to_list(cursor.fetchall())
        obj = {}
        for n in from_who_list:
            cursor.execute(
                'select message_content from user_chatting_history where user_id=%s and message_type=0 and from_who=%s',
                (i, n)
            )
            message_list = utils.tuple_to_list(cursor.fetchall())
            frequency = utils.sentence_to_frequency_dict(message_list)
            obj[n] = frequency
        result_list.append(obj)
    print(result_list)

    for index, i in enumerate(user_ids):
        cursor.execute(
            'insert into data_statistics (user_id, value, create_time, type) values (%s, %s, %s, 4)',
            (i, utils.dict_to_json_str(result_list[index]), utils.get_now_timestamp())
        )
    conn.commit()

    print('type4 complete!')
    # 关闭Cursor:
    cursor.close()
    # 连接不能关闭
    # conn.close()


if __name__ == '__main__':
    run()


