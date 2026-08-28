CREATE DATABASE IF NOT EXISTS vendas_automotivas;

USE DATABASE vendas_automotivas;

CREATE SCHEMA IF NOT EXISTS vendas;

USE SCHEMA vendas;

CREATE TABLE IF NOT EXISTS vendas_automotivas (
    sale_id INT PRIMARY KEY,
    date DATE,
    dealerhip VARCHAR(100),
    brand VARCHAR(50),
    model VARCHAR(100),
    color VARCHAR(30),
    price DECIMAL(10, 2),
    city VARCHAR(100) 
);

