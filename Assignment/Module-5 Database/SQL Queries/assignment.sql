use module5;

-- 1. Create Table Name : Student and Exam 
create table student(
	roll_no int primary key not null,
    name varchar(20) not null,
    branch varchar(30));
    
insert into student values
	(1, "jay", "computer sciene"),
    (2, "suhani", "electronic and com"),
    (3, "kriti", "electronic and com");

create table exam(
	roll_no int not null,
    s_code varchar(10)  not null,
    marks int not null,
    p_code varchar(5),
	foreign key(roll_no) references student(roll_no)    
    );
    
insert into exam values
	(1, "cs11", 50, "cs"),
    (1, "cs12", 60, "cs"),
    (2, "ec101", 66, "ec"),
    (2, "ec102", 70, "ec"),
    (3, "ec101", 45, "ec"),
    (3, "ec102", 50, "ec");

select * from student;

select * from exam;

desc student;

desc exam;


-- 2. Create table given below: Employee and IncentiveTable 
create table employee(
	e_id int primary key not null,
    first_name varchar(20),
    last_name varchar(20),
    salary int,
    joining_date datetime,
    department varchar(10));

insert into employee values
	(1, "john", "abraham", 1000000, "2013-01-01 12:00:00", "banking"),
    (2, "michael", "clarke", 800000, "2013-01-01 12:00:00", "insurance"),
    (3, "roy", "thomas", 700000, "2013-02-01 12:00:00", "banking"),
    (4, "tom", "jose", 600000, "2013-02-01 12:00:00", "insurance"),
    (5, "jerry", "pinto", 650000, "2013-02-01 12:00:00", "insurance"),
    (6, "philip", "mathew", 750000, "2013-01-01 12:00:00", "service"),
    (7, "testname1", "123", 650000, "2013-01-01 12:00:00", "service"),
    (8, "testname2", "456", 600000, "2013-02-01 12:00:00", "insurance");
    
select * from employee;

create table incentive(
	emp_ref_id int primary key,
    incentive_date date,
    incentive_amount int);

alter table incentive drop primary key;

ALTER TABLE incentive 
ADD CONSTRAINT fk_incentive 
FOREIGN KEY (emp_ref_id) 
REFERENCES employee(e_id);

desc incentive;
    
insert into incentive values
		(1, "2013-02-01", 5000),
        (2, "2013-02-01", 3000),
        (3, "2013-02-01", 4000),
        (1, "2013-01-01", 4500),
        (2, "2013-01-01", 3500);
        
select * from incentive;

-- 3. Get First_Name from employee table using Tom name “Employee Name”.
select * from 
 

    
    