#!/bin/bash
# get the things we need 
yum update -y
yum -y install  mysql mysql-server
pip install Flask

# start the required services 
service mysqld start
chkconfig mysqld on


# go out to github and get the site - for now just use s3

mkdir templates

aws s3 cp s3://mq-random-forest/index.html /var/www/html
aws s3 cp s3://mq-random-forest/table1.csv /home/ec2-user/table1.csv
aws s3 cp s3://mq-random-forest/table2.csv /home/ec2-user/table2.csv
aws s3 cp s3://mq-random-forest/create_db.SQL /home/ec2-user/create_db.SQL
aws s3 cp s3://mq-random-forest/templates/form.html /home/ec2-user/templates/form.html

# setup the database
mysqladmin -u root password veryrandompassword
mysql  -u root -pveryrandompassword < create_db.SQL


# set up flask and start the website.
pip install Flask




# start flask 
echo "from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'flask is working !!!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug = True)" > app.py
python app.py



#mysqladmin -u root -pveryrandompassword create mq_random_forest
# mysql -h mq-random-forest.c7vffwba7rx2.ap-southeast-2.rds.amazonaws.com -P 3306 -u randomForestUser -pveryrandompassword < create_db.SQL
# sudo rm create_db.SQL  table1.csv  table2.csv
#sudo yum install httpd -y
#sudo service httpd start
#sudo chkconfig httpd on
#sudo cd /var/www/html
# assuming region is ap-southeast-2a
#sudo aws s3 cp s3://mq-random-forest/index.html /var/www/html

