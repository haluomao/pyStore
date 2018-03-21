#!/usr/bin/python
# -*- coding: utf-8 -*-
# author: felix

import pymysql.cursors


def insert():
    conn = pymysql.connect(host='localhost', port=3306, user='tester',
                           password='123456', db='aaa', charset='utf8',
                           cursorclass=pymysql.cursors.DictCursor)

    cursor = conn.cursor()

    sql = "INSERT INTO `test`(`content`) VALUES ('test')"
    cursor.execute(sql)

    conn.commit()
    print "insert OK."


def select():
    conn = pymysql.connect(host='localhost', port=3306, user='tester',
                           password='123456', db='aaa', charset='utf8',
                           cursorclass=pymysql.cursors.DictCursor)

    cursor = conn.cursor()

    sql = "SELECT `id`, `content` FROM `test`"
    cursor.execute(sql)
    result = cursor.fetchone()
    print(result)

    result = cursor.fetchall()
    for data in result:
        print(data)

    conn.close()


if __name__ == '__main__':
    insert()
    select()
