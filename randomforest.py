#!/usr/bin/python

import pymysql
import mysql.connector

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='mq_random_forest_user',
                             password='veryrandompassword',
                             db='mq_random_forest',
                             #charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT table1.VAR1,  table1.VAR2, table1.VAR3, table2.VAR4, \
        table2.VAR5, table2.VAR6, table2.VAR7, table2.VAR8, table2.VAR9, \
        table2.VAR10, table1.OUTCOME \
        FROM table1 JOIN table2 ON table1.ID = table2.ID;"
        cursor.execute(sql)
        result = cursor.fetchall()
        #result = cursor.fetchone()
        print(result)
finally:
    connection.close()