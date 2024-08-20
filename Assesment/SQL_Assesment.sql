use module5;

-- tables -> City,  Customer,  Country

create table country (
	country_id int primary key,
    country_name varchar(20),
    country_name_eng varchar(20),
    country_code varchar(10));

create table city (
	city_id int primary key,
    city_name varchar(20) ,
    lat int,
    longtitude int,
    country_id int,
    foreign key (country_id) references country(country_id));

create table customers(
	customer_id int primary key,
    customer_name varchar(20),
    city_id int,
    customer_address varchar(20),
    next_call_date date,
    ts_inserted timestamp,
    foreign key (city_id) references city(city_id));
    
    
    
    
    
    
    
    