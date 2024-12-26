create table travel_form (id int primary key auto_increment, name varchar(20), age int, gender varchar(10), phone_no varchar(10), payment_mode varchar(20), food_service varchar(3)); 

select * from travel_form;

drop table travel_form;

insert into travel_form (name, age, gender, phone_no, payment_mode, food_service) values ("paras", 20, "male", "9898009898", "cash", "yes");

delete from travel_form where id = 3;