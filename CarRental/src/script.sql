-- Created by David Trimino

-- mysql -u root -p --local_infile=1 
-- source /path/to/sql/file
-- local_infile helps to read int he files locally

CREATE SCHEMA IF NOT EXISTS CarRental;
USE CarRental;

CREATE TABLE IF NOT EXISTS Customer(
	custID		INT,						-- Unique numeric value for each customer 
    custName	VARCHAR(30),				-- Name attribute can be broken up into first and last 
    phone		VARCHAR(15)					-- Interantional phone numbers can be up to 15 digits long 
);

CREATE TABLE IF NOT EXISTS Rental(
	custID		INT,
    vehicleID	VARCHAR(30),
    startDate	DATE,
    orderDate	DATE,
    rentalType	TINYINT,					-- Two values: '1 = Daily' and '7 = Weekly' -> tinyint only takes up a byte in the db 
    quanity		TINYINT,					-- Probability of a customer renting more than 127 cars is low
    returnDate	DATE,
    total		DECIMAL (7, 2),				-- Total can reach seven figures if customer purchases the most expensive car for several days
    payDate		DATE
);

CREATE TABLE IF NOT EXISTS Vehicle(
	vehicleID	VARCHAR(30),				-- Unique numeric identifier for wach car 
    descrip		VARCHAR(50),				-- Description length for each car can vary by car and category 
    carYear		INT,						-- DATE can be more efficient and saves space other than VARCHAR and we can do DATE arthimetic using DATE datatype
    carType		TINYINT,					-- Fixed number because smallest type is 3 letters and largest is five 
    category	TINYINT						-- Valid values are 0 and 1
);

CREATE TABLE IF NOT EXISTS Rate(
	carType		TINYINT,
    category 	TINYINT,
    weekly		DECIMAL (6,2),				-- 6 digits in front of decimal and 2 digits after decimal 
    daily		DECIMAL	(5,2)
);


-- LOAD DATA TO THE DATABASE
SET GLOBAL local_infile = 1;
LOAD DATA LOCAL INFILE '/home/logic/Documents/CompanyDatabase/CAR_RENTAL/data/CUSTOMER.csv' 
INTO TABLE CarRental.Customer 
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(custID, custName, phone);

LOAD DATA LOCAL INFILE '/home/logic/Documents/CompanyDatabase/CAR_RENTAL/data/RATE.csv' 
INTO TABLE CarRental.Rate 
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(carType, category, weekly, daily);

LOAD DATA LOCAL INFILE '/home/logic/Documents/CompanyDatabase/CAR_RENTAL/data/RENTAL.csv'
INTO TABLE CarRental.Rental
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(custID, vehicleID, @startvar, @ordervar, rentalType, quanity, @returnvar, total, @payvar)
SET startDate  = STR_TO_DATE   (@startvar,  '%Y-%m-%d'),
	orderDate  = STR_TO_DATE   (@ordervar,  '%Y-%m-%d'),
	returnDate = STR_TO_DATE   (@returnvar, '%Y-%m-%d'),
	payDate	   = STR_TO_DATE   (@payvar,    '%Y-%m-%d');

LOAD DATA LOCAL INFILE '/home/logic/Documents/CompanyDatabase/CAR_RENTAL/data/VEHICLE.csv' 
INTO TABLE CarRental.Vehicle 
FIELDS TERMINATED BY ','
ENCLOSED BY '\"' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(vehicleID, descrip, carYear, carType, category);


-- ADD CONSTRAINTS TO TABLES  
ALTER TABLE Customer ADD CONSTRAINT PRIMARY KEY (custID);
ALTER TABLE Customer MODIFY custID INTEGER AUTO_INCREMENT;

ALTER TABLE Vehicle ADD CONSTRAINT PRIMARY KEY (vehicleID);

ALTER TABLE Rental ADD CONSTRAINT FOREIGN KEY(vehicleID) REFERENCES Vehicle(vehicleID) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE Rental ADD CONSTRAINT FOREIGN KEY(custID) REFERENCES Customer(custID) ON DELETE CASCADE ON UPDATE CASCADE;


-- TASK 1 FOR PROJECT PART 3
ALTER TABLE Rental ADD COLUMN Returned TINYINT NOT NULL AFTER payDate;
UPDATE Rental SET Returned = 1 WHERE payDate IS NOT NULL;
UPDATE Rental SET Returned = 0 WHERE payDate IS NULL;

-- Question about TotalDays and Rental Balance
CREATE VIEW vRentalInfo AS
SELECT  Rental.orderDate, Rental.startDate, Rental.returnDate, 
		CASE Rental.rentalType
			WHEN 1 THEN DATEDIFF( Rental.returnDate, Rental.startDate )
            WHEN 7 THEN DATEDIFF( Rental.returnDate, Rental.startDate )
		END AS RentalType,
		Vehicle.vehicleID AS VIN, Vehicle.descrip AS Vehicle, 
        CASE Vehicle.carType 
			WHEN 1 THEN 'Compact'
            WHEN 2 THEN 'Medium'
            WHEN 3 THEN 'Large'
            WHEN 4 THEN 'SUV'
            WHEN 5 THEN 'Truck'
            WHEN 6 THEN 'VAN'
		END AS CarType, 
        CASE Vehicle.category 
			WHEN 0 THEN 'Basic'
            WHEN 1 THEN 'Luxury'
        END AS Category,
        Customer.custID AS CustomerID, Customer.custName AS CustomerName,
        Rental.total AS OrderAmount,
        CASE 
			WHEN ISNULL(Rental.payDate) AND Customer.custID = Rental.custID THEN 
            (
				SELECT SUM( Rental.total ) FROM Rental WHERE Rental.custID = Customer.custID 
			)
            ELSE 0
		END AS RentalBalance
FROM Rental, Vehicle, Customer
WHERE  (Vehicle.vehicleID = Rental.vehicleID) 
	   AND
       (Customer.custID = Rental.custID)
ORDER BY Rental.startDate ASC;


