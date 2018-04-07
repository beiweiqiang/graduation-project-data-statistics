#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import mysql.connector

conn = mysql.connector.connect(
    user='root',
    password='heanqi',
    host='127.0.0.1',
    database='graduation'
)

# cursor = conn.cursor()
# 创建user表:
# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 插入一行记录，注意MySQL的占位符是%s:
# cursor.execute('insert into user (id, name) values (%s, %s)', ('1', 'Michael'))
# print('rowcount =', cursor.rowcount)
# 提交事务:
# conn.commit()
# cursor.close()

# 运行查询:
# cursor = conn.cursor()
# cursor.execute('select distinct user_id from `user_chatting_history`')
# values = cursor.fetchall()
# print(values)
# 关闭Cursor和Connection:
# cursor.close()
# conn.close()

