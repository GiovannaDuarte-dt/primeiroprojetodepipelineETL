CREATE DATABASE bancodedadosvendas;
Create SCHEMA IF NOT EXISTS schemx_vendas;

Create TABLE IF NOT EXISTS schemx_vendas.vendas_ficticias_table (
    sale_id INT NOT NULL PRIMARY KEY,
    date DATE NOT NULL,
    dealership VARCHAR(100) NOT NULL,
    brand VARCHAR(50) NOT NULL,
    model VARCHAR(50) NOT NULL,
    color VARCHAR(30) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    city VARCHAR(50) NOT NULL 
);  

SELECT current_database();

SELECT COUNT(*) FROM "schemx_vendas"."vendas_ficticias_table";

SELECT * FROM "schemx_vendas"."vendas_ficticias_table" LIMIT 10;

SELECT current_database(), current_schema();