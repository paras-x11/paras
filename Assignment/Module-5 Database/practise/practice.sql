create database module5;

use module5;

show databases;

show tables;

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

insert into employee (eid,name,age,join_date,mobile_no) values (1, "paras", 22, "2014-01-10", "9898060000");

update employee set age = 24 where eid = 2;

select * from employee;

update employee set age = 24 where age = 22;

update employee set age = 24 where salary = 25000;

UPDATE employee SET `join_date` = '2012-01-10' WHERE (`eid` = '1');

insert into employee values(5, "raj", 30, "2016-01-10", 70000, "9909898099"), (4, "vikas", 30, "2020-06-01", 40000, "9824009482");

delete from employee where eid = 1;





