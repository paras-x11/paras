use practice;

create table students(
    Stud_id int Primary Key,
    stud_name varchar(20) not null,
    class varchar(10) check(class in('FY','SY','TY')),
    city varchar(10) check(city in('Surat','Mumbai','Delhi')),
    age int check(age<20));


insert into students values
    (1, 'Pavan', 'TY', 'Delhi', 19),
    (2, 'Riya', 'FY', 'Mumbai', 18),
    (3, 'Amit', 'SY', 'Surat', 17),
    (4, 'Neha', 'TY', 'Mumbai', 19),
    (5, 'Rohan', 'SY', 'Delhi', 18),
    (6, 'Isha', 'FY', 'Surat', 16),
    (7, 'Arjun', 'SY', 'Mumbai', 17),
    (8, 'Priya', 'TY', 'Surat', 19),
    (9, 'Karan', 'FY', 'Delhi', 18),
    (10, 'Meera', 'SY', 'Mumbai', 17);

create table Marks(
    stud_id int Primary key,
    stud_name varchar(20) not null,
    subject1 int check(subject1>=0),
    subject2 int check(subject2>=0),
    subject3 int check(subject3>=0),
    total int default 0,
    per int default 0,
    result varchar(10) check(result in('Dist','First','Second','Pass','Fail')) );

insert into marks(stud_id, stud_name, subject1, subject2, subject3) values
    (1, 'Tom', 45, 89, 76),
    (2, 'Sarah', 55, 72, 81),
    (3, 'Jack', 67, 83, 78),
    (4, 'Emily', 88, 91, 95),
    (5, 'Jake', 43, 64, 58),
    (6, 'Olivia', 90, 87, 92),
    (7, 'Liam', 78, 65, 71),
    (8, 'Sophia', 49, 85, 79),
    (9, 'Mia', 62, 73, 68),
    (10, 'Ethan', 81, 77, 85);


-- 2)
update marks set total=subject1+subject2+subject3;

-- 3)
UPDATE MARKS SET PER=(subject1+subject2+subject3)*100/300;

select * from marks;

-- 4)
UPDATE MARKS
SET RESULT=
CASE 
  WHEN PER>70 THEN 'Dist'
  WHEN PER>60 THEN 'First'
  WHEN PER>50 THEN 'Second'
  WHEN PER>35 THEN 'Pass'
  ELSE 'Fail'
END;

-- 5)
SELECT STUD_NAME FROM STUDENTS WHERE CLASS='FY';

-- 6)
SELECT STUD_NAME, PER FROM MARKS WHERE RESULT<>'DIST';

-- 7)
SELECT DISTINCT(S.STUD_NAME),M.PER,S.CLASS FROM STUDENTS S, MARKS M ORDER BY PER;

-- 8)
SELECT MAX(SUBJECT1) FROM MARKS;

-- 9)
SELECT MIN(SUBJECT2) FROM MARKS;

-- 10)
select stud_name from marks where subject1>60 and subject2>60;

-- 11)
select stud_name from marks where subject1<35 and subject2<35 and subject3<35;

-- 12)
select avg(subject3) from marks;

-- 13)
select stud_name,per from marks where per between 45 and 65;

-- 14)
select count(*) from marks where subject2>60;

-- 15)
select count(*) from marks where subject3>60;

-- 16)
select stud_name from students where class='FY';

-- 17)
select stud_name from students where class='FY' OR class='SY';

-- 18)
SELECT STUD_NAME FROM STUDENTS WHERE STUD_NAME LIKE 'A%';

-- 19)
SELECT COUNT(*) FROM STUDENTS WHERE AGE<18;

-- 20)
SELECT STUD_NAME, AGE FROM STUDENTS ORDER BY AGE;

-- 21)
select stud_name from students where class='TY' OR class='SY';

-- 22)
select stud_name, CLASS, AGE from students where class<>'TY';

-- 23)
select stud_name from students where AGE between 16 and 20;
