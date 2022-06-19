CREATE TABLE user (id integer NOT NULL PRIMARY KEY auto_increment,
password varchar(128) NOT NULL, last_login datetime NULL, 
username varchar(150) NOT NULL UNIQUE,
 first_name varchar(150) NOT NULL, last_name varchar(150) NOT NULL,
 email varchar(254) NOT NULL, is_staff bool NOT NULL, 
 date_joined datetime NOT NULL, gender varchar(2) NOT NULL,
 phone varchar(13) NOT NULL, region varchar(30) NOT NULL, 
 city varchar(15) NOT NULL, created_at datetime NOT NULL, 
 updated_a datetime NOT NULL, user_type varchar(20) NOT NULL);


CREATE TABLE applicant (
id integer NOT NULL PRIMARY KEY auto_increment, 
education_level varchar(15) NOT NULL, 
resume varchar(100) NULL);

CREATE TABLE application (
id integer NOT NULL PRIMARY KEY auto_increment, 
resume varchar(100) NULL, created_at datetime NOT NULL, 
updated_at datetime NOT NULL, status varchar(20) NOT NULL, 
about_yourself text NULL);

CREATE TABLE company (
id integer NOT NULL PRIMARY KEY auto_increment,
 name varchar(300) NOT NULL, region varchar(30) NOT NULL,
 city varchar(15) NOT NULL, document varchar(100) NULL,
 description text NOT NULL, created_at datetime NOT NULL, 
 updated_at datetime NOT NULL, email varchar(254) NOT NULL, 
 status bool NOT NULL);

CREATE TABLE job (
id integer NOT NULL PRIMARY KEY auto_increment, 
start_date date NOT NULL, end_date date NOT NULL, 
title varchar(300) NOT NULL, description text NOT NULL, 
category varchar(40) NOT NULL, requirement text NOT NULL, 
education_level varchar(15) NOT NULL, experience text NOT NULL, 
experience_year integer NOT NULL, salary integer NOT NULL,
 type varchar(15) NOT NULL, region varchar(30) NOT NULL,
 vacancy integer NOT NULL, created_at datetime NOT NULL, 
 updated_at datetime NOT NULL, 
 company_id bigint NOT NULL REFERENCES company (id));

CREATE INDEX job_company_id_ecf13394 ON job (company_id);
