use practice;

create table department(
	dept_id int primary key,
	dept_name varchar(10),
	emp_id int,
	foreign key (emp_id) references employee(eid));
    
select * from department;
   
desc department;
    
insert into department values
	(1, "HR", 1),
	(2, "Accounting", 2),
	(3, "Service", 3);
    
insert into department values
	(4, "finance", 1),
	(5, "s/w", 2),
	(6, "Service", 1);
    
update department set dept_name="devlopment" where dept_id=6;

update department set emp_id=5 where dept_name="finance";

update department set emp_id=4 where dept_name="s/w";

use module5;

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
    
-- for drop column 
alter table incentive drop column emp_ref_id ; 

-- for drop primary key
alter table incentive drop primary key;

-- constraint name for deleting partiaular constraint
ALTER TABLE incentive ADD constraint fk_incentive FOREIGN KEY (emp_ref_id) REFERENCES employee(e_id);

-- if constraint name is not given u need to find the constraint name that is given by default:
SELECT 
    constraint_name 
FROM 
    information_schema.key_column_usage 
WHERE 
    table_name = 'incentive' 
    AND column_name = 'emp_ref_id';

-- deleting particular foreign key with constraint name
alter table incentive drop constraint fk_incentive;


desc incentive;
    
insert into incentive values
	(1, "2013-02-01", 5000),
        (2, "2013-02-01", 3000),
        (3, "2013-02-01", 4000),
        (1, "2013-01-01", 4500),
        (2, "2013-01-01", 3500);
        
select * from incentive;

    
    
    
    
    
    
    
    

    
    
    