#!/usr/bin/env python
from __future__ import print_function

import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='veryrandompassword', db='mq_random_forest')

cur = conn.cursor()

cur.execute("SELECT * from table1 limit 10")

print(cur.description)

print()

for row in cur:
    print(row)

cur.close()
conn.close()