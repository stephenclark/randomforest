#!/bin/bash
# get the things we need 
yum update -y
yum -y install  mysql mysql-server git
pip install Flask

# start the required services 
service mysqld start
chkconfig mysqld on

git clone https://github.com/stephenclark/randomforest.git 

#aws s3 cp s3://mq-random-forest/table1.csv /home/ec2-user/table1.csv
#aws s3 cp s3://mq-random-forest/table2.csv /home/ec2-user/table2.csv
#aws s3 cp s3://mq-random-forest/create_db.SQL /home/ec2-user/create_db.SQL
#aws s3 cp s3://mq-random-forest/templates/form.html /home/ec2-user/templates/form.html

# setup the database
mysqladmin -u root password veryrandompassword
mysql  -u root -pveryrandompassword < create_db.SQL


#start the website. Should be listening on port 80
python randomforest/app.py
