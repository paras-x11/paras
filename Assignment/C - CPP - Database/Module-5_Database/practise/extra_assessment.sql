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
    
select * from product;

-- ● Write sql query to find the items whose prices are higher than or equal 250rs. Order the result by product price in descending, then product name in ascending. 
--   Return pro_name and pro_price

select * from product where pro_price >= 250 order by pro_price desc;

select * from product where pro_price >= 250 order by pro_name asc;

SELECT pro_name, pro_price FROM product WHERE pro_price >= 250 ORDER BY pro_price DESC, pro_name ASC;


-- ● Write a sql query to find the cheapest item. Return pro_name and pro_price. 

select pro_name, pro_price from product where pro_price <= (select min(pro_price) from product);

SELECT pro_name, pro_price FROM product WHERE pro_price = (SELECT MIN(pro_price) FROM product);


-- ● Write the sql query to calculate the average price of the items for each company. Return average price and company code. 

SELECT pro_com AS company_code, AVG(pro_price) AS average_price FROM product GROUP BY pro_com;



-- ● Write the sql query to find the average total for all the product mention in the table  

SELECT AVG(pro_price) AS average_price FROM product;
