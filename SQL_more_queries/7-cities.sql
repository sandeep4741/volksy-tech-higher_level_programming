-- create database and
-- create table if not exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
        id INT unique AUTO_INCREMENT NOT NULL,
	state_id INT NOT null FOREIGN KEY(state_id) REFERENCES states(id),
        name VARCHAR(256) NOT NULL,
        PRIMARY KEY(id)
);

