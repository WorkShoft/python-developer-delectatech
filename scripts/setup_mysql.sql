CREATE USER mikel@'%' IDENTIFIED by 'mikel';
GRANT ALL ON *.* to mikel@'%';
CREATE DATABASE python_developer;
FLUSH PRIVILEGES;
