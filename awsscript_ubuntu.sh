#!/bin/bash
echo "apt-get update"
apt-get update
cd /home/ubuntu

echo "apt-get install python-pip"
apt-get  -y install python
apt-get  -y install python-setuptools
apt-get  -y install python-pip
pip install --upgrade pip

echo "install flask numpy pymysql pandas etc "
# create swap space bc numpy and scipy will run out of memory 
sudo /bin/dd if=/dev/zero of=/var/swap.1 bs=1M count=1024
sudo /sbin/mkswap /var/swap.1
sudo /sbin/swapon /var/swap.1

pip  install flask numpy pymysql pandas scikit-learn sklearn scipy

sudo swapoff /var/swap.1
sudo rm /var/swap.1


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


