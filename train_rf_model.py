#!/usr/bin/python
"""Creates and saves a random forrest using Pickel"""

import pandas as pd
import numpy as np
import pymysql
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


# Get the data
dbconn = pymysql.connect(host='localhost', port=3306, user='root', passwd='veryrandompassword', db='mq_random_forest')


sql = "SELECT table1.VAR1,  table1.VAR2, table1.VAR3, table2.VAR4, table2.VAR5, table2.VAR6, \
              table2.VAR7, table2.VAR8, table2.VAR9, table2.VAR10, table1.OUTCOME \
        FROM table1 JOIN table2 ON table1.ID = table2.ID;"

df = pd.read_sql(sql, dbconn)
dbconn.close()

# Clean the data (no need for dummies in this case)
df=df.replace({'L': 1})
df=df.replace({'N': 2})
df=df.replace({'H': 3})

# split the data into test and train
X_train, X_test=train_test_split(df, test_size = 0.9)
y_train=X_train.pop('OUTCOME')
y_test=X_test.pop('OUTCOME')

# Creata a random forest object with defaults 
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

# save the model to disk
filename='finalized_model.sav'
pickle.dump(clf, open(filename, 'wb'))

#straight away lets get the model back again and test it all worked
clf = pickle.load(open(filename, 'rb'))
