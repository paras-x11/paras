create database practice;

create database backup;

use practice;

show databases;

show tables;

desc student;

ALTER TABLE old_table_name RENAME new_table_name;

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

-- product:
create table product (
    p_id int primary key,
    p_name varchar(20) not null,
    p_price int,
    p_com int);
    
insert into product values
    (101, 'mother board', 3200, 15),
    (102, 'key board', 450, 16),
    (103, 'zip drive', 250, 14),
    (104, 'speaker', 550, 16),
    (105, 'monitor', 5000, 11),
    (106, 'dvd drive', 900, 12),
    (107, 'cd drive', 800, 12),
    (108, 'printer', 2600, 13),
    (109, 'refill cartridge', 350, 13),
    (110, 'mouse', 250, 12);
    
select * from product;

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

CREATE TABLE department (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(30),
    eid INT,
    FOREIGN KEY (eid) REFERENCES employee(eid)
);

INSERT INTO department (dept_id, dept_name, eid) VALUES
(1, 'Human Resources', 1),
(2, 'Finance', 2),
(3, 'Engineering', 3),
(4, 'Marketing', 4),
(5, 'Sales', 5),
(6, 'Customer Support', 6),
(7, 'Research and Development', 7),
(8, 'IT', 8),
(9, 'Legal', 9),
(10, 'Operations', 10);

delete from department where dept_id = 10;  -- 9

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
	

insert into employee values
    (6, "vina", 26, "surat", "2014-09-01", 20000, "9922598800"),
    (7, "jiya", 34, "ahmedabad", "2015-02-14", 85000, "9994869852"),
    (8, "yug", 32, "valsad", "2017-03-11", 45000, "9824119482"),
    (9, "sujal", 30, "baroda", "2018-01-10", 75000, "9909458099");

-- and or not

select * from employee where salary<30000 and city="surat";

select * from employee where salary>30000 or city="valsad";

select * from employee where not salary>30000 and city="surat";

select * from employee where not salary<30000 and city="valsad";

-- how to test for null values: is null / is not null

insert into employee (eid,name,age,join_date,mobile_no) values (10, "vikram", 40, "2010-10-10", "9898066666");

update employee set salary=120000 where eid = 10;

select * from employee where city is null;

select * from employee where city is not null;

-- in operator: multiple or

select * from employee where city in ('vapi','surat','ahmedabad');

select * from employee where city not in ('vapi','surat','ahmedabad');

-- between:  and

select * from employee where age between 20 and 30;

select * from employee where age not between 20 and 30;

select * from employee where age between 20 and 30 and city in('surat', 'vapi');

select * from employee where age between 20 and 30 and city not in('surat', 'vapi');

-- concat_ws : concatnation with specific delemeter

SELECT CONCAT_WS("-", "SQL", "Tutorial", "is", "fun!") AS ConcatenatedString;

SELECT CONCAT_WS(", ", eid, name, city, age) AS info FROM employee;









