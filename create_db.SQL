-- Create Database Script for MQ Software developer position
-- created: May 8 2017
-- Author: Stephen Kennedy-Clark
-- Creates the database, database user and imports data
--
--
-- PRIMARY KEY ( ID )
-- randomForestUser
-- mq_random_forest_user

-- DROP USER  'randomForestUser'@'localhost';
-- DROP DATABASE IF EXISTS mq_random_forest;

CREATE DATABASE  mq_random_forest;
CREATE USER 'randomForestUser'@'localhost' IDENTIFIED BY 'veryrandompassword';
GRANT ALL ON mq_random_forest.* TO 'randomForestUser'@'localhost';
FLUSH PRIVILEGES;

USE mq_random_forest;

-- DROP TABLE table1; -- will throw error 1051 if not exists script will continue, error can be ignored
CREATE TABLE table1 (
    ID  INT, 
    VAR1 INT,
    VAR2 INT,
    VAR3 INT ,
    OUTCOME INT,
    PRIMARY KEY ( ID )
); 

-- DROP TABLE table2; -- will throw error 1051 if not exists script will continue, error can be ignored
CREATE TABLE table2 (
    ID INT,
    VAR4 VARCHAR(1),
    VAR5 VARCHAR(1),
    VAR6 VARCHAR(1),
    VAR7 VARCHAR(1),
    VAR8 VARCHAR(1),
    VAR9 VARCHAR(1),
    VAR10 VARCHAR(1),
    PRIMARY KEY ( ID )
);

 
LOAD DATA LOCAL INFILE '/home/ec2-user/table1.csv'
INTO TABLE table1
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;


LOAD DATA LOCAL INFILE '/home/ec2-user/table2.csv'
INTO TABLE table2
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;