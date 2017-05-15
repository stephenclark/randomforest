# Random Forest Machine Learning implemented in Python

This application was written by Stephen Kennedy-Clark for Maquarie University

The submission consists of:

* Simple two table MySQL database.
* Python script "train_rf_model.py" that reads from the database and then trains a Random Forest Classifier against the data. It saves the trained model as a binary "finalized_model.sav".
* Flask web form that takes 10 inputs for Vars's 1->10 and runs them against the saved
Classifier. The Flask app runs on port 80.
* Also included are a bash and SQL script to stand up the application on Ubuntu linux.

## Setting up the application

The application runs on Python 2.7.

The application needs the following Python modules:

* flask
* numpy
* pymysql
* pandas
* sklearn
* scipy
* pickle (should already be included in Python)

These are most easily installed with pip.

The application requires an instance of MySQL,
it assumes:

* database name = 'mq_random_forest'
* database user = 'randomForestUser' with access to database 'mq_random_forest'
* password =  'veryrandompassword'

If you already have an instance of the Database up and running edit the credentials on
line 13. of "train_rf_model.py".

The application can be cloned from:

```bash
git clone https://github.com/stephenclark/randomforest.git
```

## Starting the application

From the application directory first run 'train_rf_model.py' to train the model
then start the flask application 'app.py'. To run the application on a port other
than port 80 edit the last line of app.py as required.

```bash
python train_rf_model.py
python app.py
```

## Setting up the application on AWS

I use the the included script 'awsscript_ubuntu.sh' to stand up an instance of the site on
an AWS ec2 Ubuntu server.

The script builds a new machine, gets the latest code from github, creates the database, runs the
training model and finally starts the website.

An instance of the code will be running at ```http://52.62.21.48``` for a few weeks.

This script assumes you have aws cli tools installed locally and an AWS account with sufficient privileges to launch an ec2 instance. I have only tested it on Ubuntu linux.

neither the --iam-instance-profile nor the --key-name are required, however you won't be able to ssh into the machine without the --key-name. You will need at least one --security-groups allowing http access to port 80 or the site will be inaccessible. from the web.

```bash
# launch the app on AWS
aws ec2 run-instances --image-id ami-96666ff5 --placement AvailabilityZone=ap-southeast-2a --count 1 --instance-type t2.micro --key-name YourEC2KeyName --user-data file:///path_to_script_/awsscript_ubuntu.sh --security-groups Web-DMZ  --iam-instance-profile Name=S3-Admin-Access

# retrieve the ip addresses of your instances
aws ec2 describe-instances | grep PublicIpAddress
```