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
        group_names = utils.tuple_to_list(cursor.fetchall())
        # print(group_names)
        group_obj = {}
        for g in group_names:
            cursor.execute(
                'select from_who, count(from_who) as count from user_chatting_history where user_id=%s and message_type=1 and group_name=%s group by from_who',
                (i, g)
            )
            frequency = utils.tuple_to_map(cursor.fetchall())
            group_obj[g] = frequency
        result_list.append(group_obj)

    for index, i in enumerate(user_ids):
        cursor.execute(
            'insert into data_statistics (user_id, value, create_time, type) values (%s, %s, %s, 3)',
            (i, utils.dict_to_json_str(result_list[index]), utils.get_now_timestamp())
        )
    conn.commit()

    print('type3 complete!')
    # 关闭Cursor:
    cursor.close()
    # 连接不能关闭
    # conn.close()


if __name__ == '__main__':
    run()


