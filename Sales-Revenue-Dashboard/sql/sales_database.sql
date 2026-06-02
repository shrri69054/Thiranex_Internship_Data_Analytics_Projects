CREATE TABLE sales(
id INT PRIMARY KEY AUTO_INCREMENT,
sale_date DATE,
product VARCHAR(100),
region VARCHAR(50),
sales INT,
revenue DECIMAL(12,2)
);