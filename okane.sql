create table stock (
  id integer primary key
  ,code varchar(20)
  ,name varchar(255)
  ,is_index tinyint
);

create table price (
  id integer primary key
  ,stock_id integer
  ,`date` date
  ,open decimal(10, 4)
  ,close decimal(10, 4)
  ,high decimal(10, 4)
  ,low decimal(10, 4)
  ,volume decimal(20, 2)
);
