#!/usr/bin/env python
from __future__ import print_function

import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='veryrandompassword', db='mq_random_forest')

cur = conn.cursor()

cur.execute("SELECT table1.VAR1,  table1.VAR2, table1.VAR3, table2.VAR4, \
                table2.VAR5, table2.VAR6, table2.VAR7, table2.VAR8, table2.VAR9, \
                table2.VAR10, table1.OUTCOME \
            FROM table1 JOIN table2 ON table1.ID = table2.ID;")

print(cur.description)

print()

for row in cur:
    print(row)

cur.close()
conn.close()