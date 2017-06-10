drop table if exists products;
create table products (
  id text primary key autoincrement,
  shop_id integer not null,
  title text not null,
  popularity text not null,
  quantity real not null
);

drop table if exists shops;
create table shops (
  id text primary key autoincrement,
  name text not null,
  lat real not null,
  lng real not null
);

drop table if exists taggings;
create table taggings (
  id text primary key autoincrement,
  shop_id integer not null,
  tag_id integer not null
);

drop table if exists tags;
create table tags (
  id text primary key autoincrement,
  tag text not null
);

