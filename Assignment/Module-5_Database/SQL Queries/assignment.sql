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

select first_name as employee_name from employee where first_name = "tom";

-- 4. Get FIRST_NAME, Joining Date, and Salary from employee table.

select first_name, joining_date, salary from employee;

-- 5. Get all employee details from the employee table order by First_Name Ascending and Salary descending? 

select * from employee order by first_name asc;
select * from employee order by first_name desc;

-- 6. Get employee details from employee table whose first name contains ‘J’. 

select * from employee where first_name like "j%"; 
 
-- 7. Get department wise maximum salary from employee table order by salary ascending? 


-- 9. Select first_name, incentive amount from employee and incentives table for those employees who have incentives and incentive amount greater than 3000 


-- 10. Create After Insert trigger on Employee table which insert records in viewtable 


-- 11. Create table given below: Salesperson and Customer.

create table sales_person (
	sno int primary key,
    sname varchar(20)not null,
    city varchar(20) not null,
    comm float not null);
    
insert into sales_person values 
	(1001, "peel", "london", 0.12),
	(1002, "serres", "san jose", 0.13),
    (1004, "motika", "london", 0.11),
	(1007, "rafkin", "barelona", 0.15),
    (1003, "axerlrod", "new york", 0.10);
    
select * from sales_person;

create table customer (
	cno int primary key,
    cname varchar(20),
    city varchar(20),
    rating int not null,
    sno int,
    foreign key (sno) references sales_person(sno));
    
insert into customer values
	(201, "hoffman", "london", 100, 1001),
    (202, "giovanne", "rome", 200, 1003),
    (203, "liu", "san jose", 300, 1002),
    (204, "grass", "barcelona", 100, 1002),
    (206, "clemens", "london", 300, 1007),
    (207, "pereira", "rome", 100, 1004);
    
select * from customer;

-- 12. Retrieve the below data from above table 

-- 13. All orders for more than $1000.



    
    