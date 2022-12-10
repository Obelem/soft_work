-- Prepares a MySQL server for the project.
DROP DATABASE IF EXISTS soft_work_db;
CREATE DATABASE IF NOT EXISTS soft_work_db;
DROP USER IF EXISTS soft_dev;
CREATE USER IF NOT EXISTS 'soft_dev'@'localhost' IDENTIFIED BY 'pwd';
GRANT ALL PRIVILEGES ON soft_work_db . * TO 'soft_dev'@'localhost';
GRANT SELECT ON performance_schema . * TO 'soft_dev'@'localhost';
