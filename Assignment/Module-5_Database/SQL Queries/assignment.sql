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
	foreign key(roll_no) references student(roll_no));
    
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
FOREIGN KEY (emp_ref_id) REFERENCES employee(e_id);

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

SELECT * FROM employee ORDER BY first_name ASC , salary DESC;

-- 6. Get employee details from employee table whose first name contains ‘J’. 

select * from employee where first_name like "j%"; 
 
-- 7. Get department wise maximum salary from employee table order by salary ascending? 

select max(salary), department from employee group by department having max(salary) > 100000 order by max(salary);

-- 9. Select first_name, incentive amount from employee and incentives table for those employees who have incentives and incentive amount greater than 3000 

select first_name, incentive_amount from employee right join incentive on employee.e_id = incentive.emp_ref_id where incentive_amount > 3000;

-- 10. Create After Insert trigger on Employee table which insert records in view table 

create table view(
	e_id int primary key not null,
	first_name varchar(20),
	last_name varchar(20),
	salary int,
	joining_date datetime,
	department varchar(10));


delimiter //
create trigger add_view 
after insert on employee for each row
begin
	insert into view values (new.e_id, new.first_name, new.last_name, new.salary, new.joining_date, new.department);
end //
delimiter ;

insert into employee values
	(11, "naruto", "uzumaki", 1000000, "2013-01-01 12:00:00", "banking"),
	(12, "gojo", "saturo", 800000, "2013-01-01 12:00:00", "insurance"),
	(13, "kakashi", "hatake", 700000, "2013-02-01 12:00:00", "banking");

select * from employee;

select * from view;

-- 11. Create table given below: Salesperson and Customer.

-- tables: sales_person -> customer

create table sales_person (
	sno int primary key,
	sname varchar(20)not null,
	city varchar(20) not null,
	comm float not null);
    
insert into sales_person values
	(1001, "peel", "london", 0.12),
	(1002, "serres", "san jose", 0.13),
	(1004, "motika", "london", 0.11),
	(1007, "rafkin", "barcelona", 0.15),
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
-- question related data is not available in table.

-- 14. Names and cities of all salespeople in London with commission above 0.12 

select sname, city from sales_person where city = 'london' and comm > 0.12 ;

-- 15. All salespeople either in Barcelona or in London 

select * from sales_person where city = 'london' or city = 'barcelona';

-- 16. All salespeople with commission between 0.10 and 0.12. (Boundary valuesshould be excluded). 

select * from sales_person where comm > 0.10 and comm < 0.12;

-- 17. All customers excluding those with rating <= 100 unless they are located in Rome 

select * from customer where city = 'rome' and rating <= 100 or city <> 'rome' and rating > 100;

-- 18.  Write a SQL statement that displays all the information about all salespeople 

select * from sales_person;

-- tables: sales_man -> orders

create table sales_man (
	sid int primary key,
	name varchar(20)not null,
	city varchar(20) not null,
	commision float not null);
    
insert into sales_man values
	(5001, "james hoog", "new york", 0.15),
	(5002, "nail knite", "paris", 0.13),
	(5005, "pit alex", "london", 0.11),	
	(5006, "mc lyon", "paris", 0.14),
	(5007, "paul adam", "rome", 0.13),
	(5003, "lauson hen", "san jose", 0.12);
    
    
create table orders (
	order_no int primary key,
	purchase_amt float not null,
	order_date date,
	customer_id int not null,
	sid int,
	foreign key (sid) references sales_man(sid));

INSERT INTO orders VALUES 
    (70001, 150.5,   '2012-10-05', 3005, 5002),
    (70009, 270.65, '2012-09-05', 3001, 5005),
    (70002, 65.26,   '2012-10-05', 3002, 5001),
    (70004, 110.5,   '2012-08-05', 3009, 5003),
    (70007, 948.5,   '2012-09-05', 3005, 5002),
    (70005, 2400.6, '2012-07-05', 3007, 5001),
    (70008, 5760   , '2012-09-05', 3002, 5001),
    (70010, 1983.43, '2012-10-05', 3004, 5006),
    (70003, 2480.4, '2012-10-05', 3009, 5003),
    (70012, 250.45, '2012-06-05', 3008, 5002),
    (70011, 75.29,   '2012-08-05', 3003, 5007),
    (70013, 3045.6, '2012-04-05', 3002, 5001);

select * from product;

-- 19.  From the following table, write a SQL query to find orders that are delivered by a salesperson with ID. 5001. Return ord_no, ord_date, purch_amt. 

select order_no, order_date, purchase_amt from orders where sid = 5001;

select * from sales_man left join orders on sales_man.sid = orders.sid where orders.sid = 5001;


-- table: product

create table product (
	pro_id int primary key,
	pro_name varchar(20) not null,
	pro_price int,
	pro_com int);
    
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

-- 20. From the following table, write a SQL query to select a range of products whose price is in the range Rs.200 to Rs.600. Begin and end values 
--     are included. Return pro_id, pro_name, pro_price, and pro_com. 

 select pro_id, pro_name, pro_price, pro_com as commision from product where pro_price between 200 and 600;
  
 
-- 21. From the following table, write a SQL query to calculate the average price for a manufacturer code of 16. Return avg. 
-- no manufacturer code avaialable ?????
 
SELECT AVG(pro_price) FROM product WHERE pro_com = 16;



-- 22. From the following table, write a SQL query to display the pro_name as 'Item Name' and pro_priceas 'Price in Rs.' 
 
select pro_name as Item_Name, pro_price as Price_in_rs from product;
 
-- 23. From the following table, write a SQL query to find the items whose prices are higher than or equal to $250. Order the result by product price in 
--     descending, then product name in ascending. Return pro_name and pro_price.

SELECT pro_name, pro_price FROM product WHERE pro_price >= 250 ORDER BY pro_price DESC, pro_name ASC;

-- select pro_name, pro_price from product where pro_price >= 250 order by pro_price desc;

-- select pro_name, pro_price from product where pro_price >= 250 order by pro_name asc;


-- 24. From the following table, write a SQL query to calculate average price of the items for each company. Return average price and companycode. 

-- there is no data available about company.
    
SELECT pro_com AS Manufacturer_Code, AVG(pro_price) AS Avg_Price FROM product GROUP BY pro_com;

    