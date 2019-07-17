-- creates the database hbtn_0d_usa 
-- and the table cities
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
	id NOT NULL UNIQUE AUTO INCREMENT PRIMARY KEY,
	name VARCHAR(256) NOT NULL,
);
