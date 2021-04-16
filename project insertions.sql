select * from users;
select * from user_has;
select * from stocks;
select * from transactions;
desc transactions;
alter table transactions AUTO_INCREMENT=10000;
insert into Stocks(sector_id,stock_name,quantity,pps) values(02,"soham Tech",15000,10000);
insert into sector(sector_id,sector_name,mkt_cap) values(01,"entertainment",10000);
insert into sector(sector_id,sector_name,mkt_cap) values(02,"Technology",100000);
insert into user_has(user_id,stock_id,quantity) values(1014,04,600);
select stock_id,user_id,quantity from user_has uh where user_id = 1014;
select s.stock_id,s.stock_name,s.pps,uh.quantity from stocks s  Inner join user_has uh on uh.stock_id = s.stock_id
where (s.stock_id, uh.user_id) in 
(select stock_id,user_id from user_has where user_id = 1014);
desc transactions;
alter table transactions add trans_qty numeric(10);