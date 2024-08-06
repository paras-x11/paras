create database module5;

use new;

show databases;

show tables;

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

