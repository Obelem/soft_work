-- Prepares a MySQL server for the project.
CREATE DATABASE IF NOT EXISTS soft_work_db;
CREATE USER IF NOT EXISTS 'soft_worker'@'localhost' IDENTIFIED BY 'softWorkPwd';
GRANT ALL PRIVILEGES ON soft_work_db . * TO 'soft_worker'@'localhost';
GRANT SELECT ON performance_schema . * TO 'soft_worker'@'localhost';
