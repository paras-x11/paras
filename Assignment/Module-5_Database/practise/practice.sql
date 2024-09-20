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

-- Function 1:

delimiter //
create function cube_of(num int) returns int deterministic
begin
	declare cube1 int;
    set cube1 = num*num*num;
	return cube1;
end //
delimiter ;

select cube_of(6) as cube6;

-- func find_age of employee:
delimiter //
create function find_age(employee_name varchar(20)) returns int deterministic
begin
	declare ages int;
    select age into ages from employee where name=employee_name;
    return ages;
end //
delimiter ;

select find_age("paras") as age;

-- func get_joining_date from employee;
delimiter //
create function get_joining_date(employee_name varchar(20)) returns date deterministic
begin
	declare joining_date date;
    select join_date into joining_date from employee where name=employee_name;
    return joining_date;
end //
delimiter ;

select get_joining_date("vikas"); 

-- func get total marks from marks:
delimiter //
create function get_total(student_name varchar(20)) returns int deterministic
begin
	declare num int;
    select total into num from marks where stud_name = student_name;
    return num;
end //
delimiter ;

select get_total("tom") as total;

-- func to get age from dob of employee;

delimiter //
create function get_age(date_of_birth date) returns int deterministic
begin
	declare age int;
    declare y int;
    select curdate() into age from employee where date_of_birth = dob;
    set y = year(age) - year(date_of_birth);
    return y;
end //
delimiter ;

select get_age('1995-07-08');

-- procedure syntax:
-- DELIMITER //
-- CREATE PROCEDURE procedure_name ( [IN|OUT|INOUT] parameter_name parameter_datatype)
-- BEGIN
    -- SQL statements to be executed
-- END //
-- DELIMITER;
 -- To run procedure : call procedure_name(parameter);

-- procedure without parameter.
delimiter $$
create procedure p1()
begin
	select * from course;
end $$
delimiter ;

-- call procedure 
call p1();


-- creating procedure without parameter:
DELIMITER //

CREATE PROCEDURE Show_All_Employee()
BEGIN
    SELECT * FROM employee;
END //

DELIMITER ;

call Show_All_Employee;

-- in for input, out for output for run select query

-- procedure to find age of student eith in parameter:

delimiter //
create procedure student_age(in sid int)
begin
	select age from students where sid = Stud_id;
end //
delimiter ;

call student_age(10);

-- proedure to increase salary :
delimiter //
create procedure increment(in emp_id int, inout esalary int)
begin
	select salary into esalary from employee where emp_id = eid;
	update employee set salary = salary + 1000 where emp_id = eid;
end //
delimiter ;

call increment(1,@esalary);
select @esalary as salary;           -- in for input, out for output for run select query.

-- trigger syntax:

-- CREATE TRIGGER trigger_name
-- {BEFORE | AFTER} {INSERT | UPDATE | DELETE}
-- ON table_name
-- [FOR EACH ROW]
-- [WHEN (condition)]
-- BEGIN
--     -- SQL statements to execute when the trigger is fired
-- END;


CREATE TABLE student2 (
    no INT,
    name VARCHAR(20),
    age INT,
    city varchar(20),
    gender VARCHAR(20)
);

INSERT INTO student2 (no, name, age, city, gender) VALUES
(1, 'Alice', 20, 'Ahmedabad', 'Female'),
(2, 'Bob', 21, 'Surat', 'Male'),
(3, 'Charlie', 22, 'Vadodara', 'Male'),
(4, 'Diana', 19, 'Rajkot', 'Female'),
(5, 'Ethan', 20, 'Bhavnagar', 'Male'),
(6, 'Fiona', 21, 'Jamnagar', 'Female'),
(7, 'George', 22, 'Junagadh', 'Male'),
(8, 'Hannah', 20, 'Gandhinagar', 'Female'),
(9, 'Ian', 19, 'Anand', 'Male'),
(10, 'Jasmine', 21, 'Navsari', 'Female');

truncate table student2;
-- for delete all records of table : 'truncate'

-- trigger to set on insert where new city if added surat should be update to local

delimiter //
create trigger update_city
BEFORE insert on student2 for each row
BEGIN
    if new.city="surat" then set new.city="local";
    end if;
END //
delimiter ;

INSERT INTO student2 (no, name, age, city, gender) VALUES
(1, 'Alice', 20, 'Ahmedabad', 'Female'),
(2, 'Bob', 21, 'Surat', 'Male'),
(3, 'Charlie', 22, 'Vadodara', 'Male');

select * from student2;

CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Age INT,
    City VARCHAR(50),
    RegistrationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO Users (UserID, FirstName, LastName, Age, City) VALUES
(1, 'Naruto', 'Uzumaki', 25, 'Konoha'),
(2, 'Sasuke', 'Uchiha', 25, 'Konoha'),
(3, 'Sakura', 'Haruno', 25, 'Konoha'),
(4, 'Gojo', 'Satoru', 34, 'Tokyo'),
(5, 'Yuuji', 'Itadori', 24, 'Tokyo'),
(6, 'Tanjirou', 'Kamado', 16, 'Kanao'),
(7, 'Nezuko', 'Kamado', 16, 'Kanao'),
(8, 'Luffy', 'Monkey', 24, 'Loguetown'),
(9, 'Zoro', 'Roronoa', 24, 'Loguetown'),
(10, 'Sanji', 'Vinsmoke', 23, 'Baratie'),
(11, 'Nami', 'Strawhat', 22, 'Cocoyasi Village'),
(12, 'Kakashi', 'Hatake', 39, 'Konoha'),
(13, 'Hinata', 'Hyuga', 25, 'Konoha'),
(14, 'Shikamaru', 'Nara', 25, 'Konoha'),
(15, 'Inosuke', 'Hashibira', 16, 'Kanao'),
(16, 'Zenitsu', 'Agatsuma', 16, 'Kanao'),
(17, 'Mikasa', 'Ackerman', 21, 'Shiganshina District'),
(18, 'Eren', 'Yeager', 24, 'Shiganshina District'),
(19, 'Yusuke', 'Urameshi', 28, 'Tokyo'),
(20, 'Kurama', 'Kurama', 28, 'Tokyo'),
(21, 'Hikari', 'Kashima', 23, 'Tokyo'),
(22, 'Kageyama', 'Tobio', 22, 'Tokyo'),
(23, 'Kiba', 'Inuzuka', 25, 'Konoha'),
(24, 'Tenten', 'TenTen', 25, 'Konoha'),
(25, 'Temari', 'Sabaku', 25, 'Sunagakure'),
(26, 'Gaara', 'Sabaku', 25, 'Sunagakure'),
(27, 'Yoshino', 'Kashiwagi', 24, 'Tokyo'),
(28, 'Kuroko', 'Tetsuya', 25, 'Tokyo'),
(29, 'Kiyoko', 'Shimizu', 22, 'Tokyo'),
(30, 'Hinata', 'Shouyou', 21, 'Tokyo');


CREATE TABLE deleted_users (
    UserID INT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Age INT,
    City VARCHAR(50)
);


-- trigger for move deleted data to another table

delimiter //
create trigger move_data_to_deleted_user
after delete on users for each row
begin 
	insert into deleted_users values(old.userid, old.firstname, old.lastname, old.age, old.city);
end //
delimiter ;

delete from users where userid = 22;

-- Insert all data from deleted_users back into Users
INSERT INTO Users (UserID, FirstName, LastName, Age, City)
SELECT UserID, FirstName, LastName, Age, City
FROM deleted_users;


delete from users where userid in (27, 28, 29);

-- Insert specific records from deleted_users to Users
INSERT INTO Users (UserID, FirstName, LastName, Age, City)
SELECT UserID, FirstName, LastName, Age, City
FROM deleted_users
WHERE UserID IN (27, 28, 29);  -- Replace with the specific UserID values you want to restore

-- Remove the restored records from deleted_users
DELETE FROM deleted_users WHERE UserID IN (27, 28, 29);  -- Replace with the specific UserID values you restored

-- Insert specific records with conflict handling
-- if record alredy existed it dont insert and record is not existing its inserted
INSERT INTO Users (UserID, FirstName, LastName, Age, City)
SELECT UserID, FirstName, LastName, Age, City
FROM deleted_users
WHERE UserID IN (27,28,29,30)  -- Adjust UserIDs as needed
ON DUPLICATE KEY UPDATE
    FirstName = VALUES(FirstName),
    LastName = VALUES(LastName),
    Age = VALUES(Age),
    City = VALUES(City);


truncate table deleted_users;

select * from users;
select * from deleted_users;

-- table for keeping old records after updating the records:
CREATE TABLE EmployeeUpdateLog (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    eid INT,
    old_name VARCHAR(20),
    new_name VARCHAR(20),
    old_dob DATE,
    new_dob DATE,
    old_city VARCHAR(10),
    new_city VARCHAR(10),
    old_join_date DATE,
    new_join_date DATE,
    old_salary INT,
    new_salary INT,
    old_mobile_no VARCHAR(10),
    new_mobile_no VARCHAR(10),
    update_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- trigger for saving old data after updating employee
DELIMITER //
CREATE TRIGGER after_employee_update
AFTER UPDATE ON employee FOR EACH ROW
BEGIN
    INSERT INTO EmployeeUpdateLog (
        eid, old_name, new_name, old_dob, new_dob, old_city, new_city,
        old_join_date, new_join_date, old_salary, new_salary,
        old_mobile_no, new_mobile_no, update_time
    )
    VALUES (
        OLD.eid, OLD.name, NEW.name, OLD.dob, NEW.dob, OLD.city, NEW.city,
        OLD.join_date, NEW.join_date, OLD.salary, NEW.salary,
        OLD.mobile_no, NEW.mobile_no, NOW()
    );
END //
DELIMITER ;


UPDATE employee SET name = 'parash', city = 'mumbai' WHERE eid = 1;

SELECT * FROM EmployeeUpdateLog;

-- TCl: Savepoint, Rollback, commit

-- for delete savepoint:
RELEASE SAVEPOINT savepoint_name;

SELECT * FROM student2;

savepoint s;

insert into student2 values (4, "Maki", 25, "Tokyo", "Female"),
							(5, "Nobara", 23, "Navsari", "Female");
                            
savepoint s1;

update student2 set city = "Tokyo" where no = 5;

-- commit;
-- in MySQL, when you issue a COMMIT statement, all savepoints that were set within the current transaction are automatically released and deleted.
-- This means that after a COMMIT, you can no longer roll back to any of the savepoints that were created during that transaction.

savepoint s2;

delete from student2 where no = 5;

savepoint s3;

rollback to s;

rollback to s1;

rollback to s2;

rollback to s3;

delete from student2 where no in (4,5);

release savepoint s;

-- cursor:
SELECT * FROM practice.employee;

create table employee_backup(
	eid int primary key,
	name varchar(50),
	city varchar(50),
	salary int,
    mobile_no varchar(10));
    
DELIMITER //

CREATE PROCEDURE transfer_to_backup()
BEGIN
    -- Declare variables to hold the column values
    DECLARE done INT DEFAULT FALSE;
    DECLARE var_eid INT;
    DECLARE var_name VARCHAR(100);
    declare var_city varchar(50);
    DECLARE var_salary INT;
	declare var_mob_no varchar(10);
    
    -- Declare a cursor to select the desired fields
    DECLARE employee_cursor CURSOR FOR
        SELECT eid, name, city, salary, mobile_no FROM employee;

    -- Declare a CONTINUE HANDLER for the end of the cursor
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    -- Open the cursor
    OPEN employee_cursor;

    -- Fetch rows from the cursor
    read_loop: LOOP
        FETCH employee_cursor INTO var_eid, var_name, var_city, var_salary, var_mob_no;
        IF done THEN
            LEAVE read_loop;
        END IF;

        -- Insert the selected data into the backup table
        INSERT INTO employee_backup (eid, name, city, salary, mobile_no)
        VALUES (var_eid, var_name, var_city, var_salary, var_mob_no);
    END LOOP;

    -- Close the cursor
    CLOSE employee_cursor;
END //

DELIMITER ;

drop procedure transfer_to_backup;

call transfer_to_backup;

insert into employee values (11, "suhani", "2000-01-01", "banglore", "2024-01-01", 22000, "9529927278");

truncate employee_backup;

select * from employee_backup;
    


    

















































