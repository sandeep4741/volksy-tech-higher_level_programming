-- create user with all privilages
CREATE USER
IF NOT EXISTS 'user_0d_1'@'localhost'
IDENTIFIED by 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.*
TO 'user_0d_1'@'localhost'
IDENTIFIED by 'user_0d_1_pwd';
FLUSH PRIVILEGES;
