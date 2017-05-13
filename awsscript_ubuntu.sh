#!/bin/bash
echo "apt-get update"
apt-get update
cd /home/ubuntu

echo "apt-get install python-pip"
apt-get  -y install python
apt-get  -y install python-setuptools
apt-get  -y install python-pip
pip install --upgrade pip

echo "install flask numpy pymysql pandas"
pip  install flask numpy pymysql pandas

echo "mysql"
debconf-set-selections <<< 'mysql-server mysql-server/root_password password veryrandompassword'
debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password veryrandompassword'
apt-get -y install mysql-server

echo "Clone Repo and set up website"
git clone https://github.com/stephenclark/randomforest.git
mysql  -u root -pveryrandompassword < randomforest/create_db.SQL

# Copy startup logs to home to make for easy debugging
cp /var/log/cloud-init-output.log . 

#start the website. Should be listening on port 80
python randomforest/app.py


