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
    (4, 'Marketing', 5),
    (5, 'Sales', 8),
    (6, 'IT', 9);

-- inner join:
-- syntax:
-- select column_name from table1(primary key table) inner join table2(foreign key table) where table1.primary key col =table2.foreign key col;
select employee.eid, name, age, dept_name from employee inner join department on employee.eid = department.eid order by employee.eid;

-- left join
-- syntax: select column_name from table1(PK) left join table2(FK) where table1.col=table2.col;
select employee.eid, name, dept_name from employee left join department on employee.eid = department.eid order by employee.eid;

-- right join
-- syntax: select column_name from table1(PK) right join table2(FK) where table1.col=table2.col;
select employee.eid, name, dept_name from employee right join department on employee.eid = department.eid order by employee.eid;

-- full outer join
select employee.eid, name, dept_name from employee left join department on employee.eid = department.eid
union
select employee.eid, name, dept_name from employee right join department on employee.eid = department.eid;

-- self join
-- syntax : select col as name ,col_name from table1 t1,table t2 where table1.col=table2.col;

select e.eid, name, dept_name from employee e,department d where e.eid = d.eid;

select e.eid as employee_id, name, age, salary, dept_name as department from employee e,department d where e.eid = d.eid;

--  cross join
-- syntax :
select * from  employee cross join department;



