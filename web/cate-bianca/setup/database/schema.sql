SET GLOBAL event_scheduler = ON;
USE db;

CREATE TABLE users (
username char(20),
password char(20)
);

INSERT INTO users VALUES('admin','efe53c758291e58f1f1c');
