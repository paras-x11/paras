create database practice;

use practice;

show databases;

show tables;

desc student;

-- student: 
create table student (no int, name varchar(20), age int, dob date, gender varchar(20));
CREATE TABLE student (
    no INT,
    name VARCHAR(20),
    age INT,
    dob DATE,
    gender VARCHAR(20)
);

drop table student;

drop database new;

describe student;

alter table student add column mobile_no varchar(20) after name;

alter table student drop column mobile_no;

insert into student values(2, 'pavan', '9824009482', 25, '1999-11-04', 'male');

INSERT INTO student (no, name, age, dob, gender) 
VALUES (1, 'paras', 20, '2004-02-11', 'male');

select * from student;

delete from student where no='1'; 

ALTER TABLE student
ADD CONSTRAINT pk_student_no PRIMARY KEY (no);


-- employee:

CREATE TABLE employee (
    eid INT PRIMARY KEY,
    name VARCHAR(20) UNIQUE,
    age INT,
    join_date DATE,
    salary INT,
    mobile_no VARCHAR(10) UNIQUE,
    CHECK (age > 21)
);

alter table employee add column city varchar(10) after age;

insert into employee (eid,name,age,join_date,mobile_no) values (1, "paras", 22, "2014-01-10", "9898060000");

update employee set city = "surat" where eid = 1;

select * from employee;

update employee set age = 24 where age = 22;

update employee set salary = 30000 where age = 22;

UPDATE employee SET `join_date` = '2012-01-10' WHERE (`eid` = '1');

insert into employee values
	(2, "rahul", 28, "valsad", "2014-06-01", 50000, "9922778800"),
    (3, "pavan", 35, "ahmedabad", "2007-06-01", 90000, "9998669852"),
    (4, "vikas", 30, "vapi", "2020-06-01", 40000, "9824009482"),
	(5, "raj", 30, "baroda", "2016-01-10", 70000, "9909898099");

delete from employee where eid = 1;

-- for rename the table
rename table employee to emp_details;

select eid, name, salary from emp_details where salary > 25000;

alter table emp_details add column city varchar(10) not null after name;

rename table emp_details to employee;

update employee set city = "surat" where eid = 1;

update employee set city = "ahmedabad" where eid = 2;

update employee set city = "baroda" where eid = 3;

update employee set city = "valsad" where eid = 4;

update employee set city = "vapi" where eid = 5;

select eid, name, salary from employee where city = "surat";

-- limit
select * from employee limit 3;

select * from employee where age>30 limit 4;

select * from employee limit 2 offset 2;

select * from employee where age>25 limit 2 offset 3;

-- like keyword: wild cards -> _ %
select * from employee where name like "p%";

select * from employee where city like "_h%";

select * from employee where name like "%a%";

select * from employee where name like "_a_";

select * from employee where name like "_a__%";

-- aggregate func: count, sum, avg, min, max

select count(eid) as total_record from employee;
select count(name) as total_record from employee;

select sum(eid) from employee;

select avg(salary) from employee;

select min(salary) from employee;

select max(salary) from employee;

-- asc / desc

select * from employee order by city asc;

select * from employee order by name asc;

select * from employee order by city desc;

select * from employee order by name desc;

