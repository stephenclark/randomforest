#!/bin/bash
echo "get the things we need"
yum update -y
#pip install --upgrade pip

yum -y install  mysql mysql-server git
pip install Flask
pip install flask-mysqldb

echo "start the required services"
service mysqld start
chkconfig mysqld on

echo "move to home and clone repo"
cd /home/ec2-user/
git clone https://github.com/stephenclark/randomforest.git 

echo "setup the database" 
mysqladmin -u root password veryrandompassword
mysql  -u root -pveryrandompassword < randomforest/create_db.SQL


#start the website. Should be listening on port 80
python randomforest/app.py
