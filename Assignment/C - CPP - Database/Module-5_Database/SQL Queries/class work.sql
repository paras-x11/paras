create database classWork;

use classWork;

CREATE TABLE student (
    s_id INT PRIMARY KEY,
    first_name VARCHAR(20),
    last_name VARCHAR(20),
    email VARCHAR(50),
    birth_date DATE,
    start_date DATE
);

INSERT INTO student VALUES 
(1, 'paras', 'rana', 'parasrana@gmail.com', '2004-02-11', '2024-06-14'),
(2, 'rohit', 'koli', 'rohitkoli@gmail.com', '2003-11-09', '2022-07-11'),
(3, 'anjana', 'lad', 'anjanalad@gmail.com', '2000-06-10', '2021-06-14'),
(4, 'pavan', 'rana', 'pavanrana@gmail.com', '2005-07-24', '2023-01-01'),
(5, 'roshan', 'patel', 'roshanpatel@gmail.com', '1999-10-22', '2021-06-14'),
(6, 'maria', 'jones', 'mariajones@gmail.com', '2001-01-01', '2023-01-01'),
(7, 'anjali', 'avasthi', 'anjaliavasthi@gmail.com', '2002-12-01', '2021-01-01'),
(8, 'rajkishor', 'sharma', 'rajkishorsharma@gmail.com', '2006-01-20', '2020-02-15'),
(9, 'yug', 'jariwala', 'yugjariwala@gmail.com', '2004-03-25', '2020-02-15');

CREATE TABLE lecturer (
    l_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    degree VARCHAR(50),
    email VARCHAR(50)
);

INSERT INTO lecturer VALUES 
(1, 'Amit', 'Sharma', 'PhD in Physics', 'amit.sharma@college.com'),
(2, 'Priya', 'Singh', 'MSc in Mathematics', 'priya.singh@college.com'),
(3, 'Rajiv', 'Kumar', 'PhD in Computer Science', 'rajiv.kumar@college.com'),
(4, 'Sara', 'Patel', 'MSc in Chemistry', 'sara.patel@college.com'),
(5, 'Nikhil', 'Verma', 'PhD in Economics', 'nikhil.verma@college.com'),
(6, 'Anita', 'Desai', 'MSc in Biology', 'anita.desai@college.com');

CREATE TABLE academic_semester (
    a_id INT PRIMARY KEY,
    calendar_year INT,
    term VARCHAR(20),
    start_date DATE,
    end_date DATE
);

INSERT INTO academic_semester VALUES 
(1, 2021, 'Sem 1', '2021-01-15', '2021-05-20'),
(2, 2021, 'Sem 2', '2021-08-25', '2021-12-15'),
(3, 2022, 'Sem 3', '2022-01-14', '2022-05-19'),
(4, 2022, 'Sem 4', '2022-08-23', '2022-12-14'),
(5, 2023, 'Sem 5', '2023-01-13', '2023-05-18'),
(6, 2023, 'Sem 6', '2023-08-22', '2023-12-13'),
(7, 2024, 'Sem 3', '2024-01-12', '2024-05-17'),
(8, 2024, 'Sem 5', '2024-08-21', '2024-12-12'),
(9, 2020, 'Sem 1', '2020-01-10', '2020-05-15'),
(10, 2020, 'Sem 2', '2020-08-20', '2020-12-10');

create table course_edition (
    c_id int primary key,
    s_id int, l_id int, a_id int,
    foreign key (s_id) references student(s_id),
    foreign key (l_id) references lecturer(l_id),
    foreign key (a_id) references academic_semester(a_id));
    
INSERT INTO course_edition (c_id, s_id, l_id, a_id) VALUES
(1, 1, 1, 1),  -- Student with s_id=1 is taking a course with lecturer l_id=1 in academic semester a_id=1 (Sem 1)
(2, 2, 2, 2),  -- Student with s_id=2 is taking a course with lecturer l_id=2 in academic semester a_id=2 (Sem 2)
(3, 3, 3, 3),  -- Student with s_id=3 is taking a course with lecturer l_id=3 in academic semester a_id=3 (Sem 3)
(4, 4, 4, 4),  -- Student with s_id=4 is taking a course with lecturer l_id=4 in academic semester a_id=4 (Sem 4)
(5, 5, 5, 5),  -- Student with s_id=5 is taking a course with lecturer l_id=5 in academic semester a_id=5 (Sem 5)
(6, 6, 6, 6),  -- Student with s_id=6 is taking a course with lecturer l_id=6 in academic semester a_id=6 (Sem 6)
(7, 7, 1, 2),  -- Student with s_id=7 is taking a course with lecturer l_id=1 in academic semester a_id=2 (Sem 2)
(8, 8, 2, 3),  -- Student with s_id=8 is taking a course with lecturer l_id=2 in academic semester a_id=3 (Sem 3)
(9, 9, 3, 4);  -- Student with s_id=9 is taking a course with lecturer l_id=3 in academic semester a_id=4 (Sem 4)

select * from student;

select * from lecturer;

select * from academic_semester;

select * from course_edition;


-- List All Students

select * from student;


-- All Student Names

select first_name, last_name from student;


-- select the email for the lecturer with the ID of 5 from the database.

select email from lecturer where l_id = 5;

-- Select all data for any student whose last name is 'Lad".

select * from student where last_name = "lad";

-- Select the first and last names of students whose last name starts with the letter D.

select first_name, last_name from student where last_name like 'd%';

-- Select all data for academic semesters where these two conditions are met the year is 2020 and the term is sem 2.

select * from academic_semester where calendar_year = "2020" and term = "sem 2";

-- Select the last name and the birthdate for students born in or after 2003 and sort them by last name in descending (Z to A) order.

select last_name, birth_date from student where year(birth_date) >= 2003 order by last_name desc;

-- Select the first name, last name, and birthdate for students born between 2003 and 2004 from the database.

select first_name, last_name, birth_date from student where year(birth_date) between 2003 and 2004;

-- Select the start date for all students and show how many students have the same start date.

select start_date, count(*) from student group by(start_date); 

-- Find start dates on which there were more than 1 students. Display the start date and the number of students that started on this date.

select start_date, count(*) from student group by(start_date) having count(*) > 1; 

-- For every lecturer, find out how many courses they teach in each academic semester. 
-- Display the first and last name of the lecturer, the calendar year, the term, and count the courses taught by the lecturer in this semester.

SELECT l.first_name, l.last_name, a.calendar_year, a.term, COUNT(ce.c_id) AS course_count
FROM lecturer l
JOIN course_edition ce ON l.l_id = ce.l_id
JOIN academic_semester a ON ce.a_id = a.a_id
GROUP BY l.l_id, a.a_id;









    


