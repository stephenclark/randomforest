#!/Users/stephenkennedy-clark/anaconda/bin/python2.7
import pandas as pd
import numpy as np
import pymysql
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split



# Get the data
dbconn = pymysql.connect(host='localhost', port=3306, user='root', passwd='!muviaiEtk1?Z', db='mq_random_forest')


sql= "SELECT table1.VAR1,  table1.VAR2, table1.VAR3, table2.VAR4, table2.VAR5, table2.VAR6, \
              table2.VAR7, table2.VAR8, table2.VAR9, table2.VAR10, table1.OUTCOME \
        FROM table1 JOIN table2 ON table1.ID = table2.ID;"

df = pd.read_sql(sql, dbconn)
dbconn.close()

# Clean the data (no need for dummies in this case)
df = df.replace({'L':1})
df = df.replace({'N':2})
df = df.replace({'H':3})


# split the data
X_train, X_test = train_test_split(df, test_size = 0.5)
y_train = X_train.pop('OUTCOME')
y_test = X_test.pop('OUTCOME')

# Creata a random forest object with defaults 
clf = RandomForestClassifier()
clf.fit(X_train, y_train)
cv_scores = cross_val_score(clf, X_train, y_train)
# Print results
print('Accuracy scores:', cv_scores)
print('Mean of score:', np.mean(cv_scores))
print('Variance of scores:', np.var(cv_scores))

#Lets see how good our model is
predictions = clf.predict(X_test)

print "training set" , len(y_train)
print "test set" , len(y_test)
pd.crosstab(predictions, y_test.as_matrix(), rownames=['Actual'], colnames=['Predicted'])

#Feature Importance
list(zip(X_train, clf.feature_importances_))

# lets look at some sample test data:

a = [[67,2,0,1,3,1,3,2,1,2]] # 1
b = [[86,0,0,2,2,2,2,2,2,2]] # 1
c = [[30,0,27,2,2,2,2,2,2,2]] # 0
d = [[84,0,0,2,3,2,2,2,2,2]] # 1
     
print 'predicted:', clf.predict(a), 'expecting 1', 'with probability of :', clf.predict_proba(a)[0,clf.predict(a)] 
print 'predicted:', clf.predict(b), 'expecting 1', 'with probability of :', clf.predict_proba(b)[0,clf.predict(b)] 
print 'predicted:', clf.predict(c), 'expecting 0', 'with probability of :', clf.predict_proba(c)[0,clf.predict(c)] 
print 'predicted:', clf.predict(d), 'expecting 1', 'with probability of :', clf.predict_proba(d)[0,clf.predict(d)] 