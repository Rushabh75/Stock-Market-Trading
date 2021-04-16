create database project;

select user_name,password from users where user_name = 's' and password = 's';

select * from users;
drop table users;
CREATE TABLE Users
(
user_id INT AUTO_INCREMENt PRIMARY KEY,
user_name varchar(50) NOT NULL unique,
contact_no1 numeric(50),
contact_no2 numeric(50),
address varchar(50),
password varchar(10),
pan_no numeric(20) unique,
email_id varchar(50)
);

drop table Stocks;
CREATE TABLE Stocks(
stock_id INT auto_increment PRIMARY KEY,
sector_id INT,
constraint fk_sector FOREIGN KEY (sector_id) REFERENCES Sector(sector_id) on update cascade on delete cascade,
stock_name varchar(50) NOT NULL,
quantity numeric(20),
pps numeric(10,2)
);



drop table Sector;
CREATE TABLE Sector(
sector_id INT auto_increment PRIMARY KEY,
sector_name varchar(20) UNIQUE,
mkt_cap numeric(10)
);


drop table transactions;
create table transactions( 
trans_id INT auto_increment primary key,
tran_time timestamp, 
trans_price numeric(10), 
stock_id INT,
user_id INT,
type char(2),
trans_qty numeric(10),
constraint fk_stock3 Foreign Key (stock_id) references Stocks(stock_id) on update cascade on delete cascade,
constraint fk_user4 Foreign Key (user_id) references users(user_id) on update cascade on delete cascade
);
alter table transactions AUTO_INCREMENT=10000;


select @@datadir;


drop table User_has;
desc user_has;
create table user_has(
user_id INT,
constraint fk_user3 Foreign Key (user_id) references Users(user_id) on update cascade on delete cascade,
stock_id INT,
constraint fk_stock4 Foreign Key (stock_id) references Stocks(stock_id) on update cascade on delete cascade,
quantity numeric(10)
);
ALTER TABLE user_has ADD PRIMARY KEY (user_id,stock_id);

desc user_has;
