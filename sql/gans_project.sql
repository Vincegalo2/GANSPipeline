-- Create the 'gans' database
CREATE DATABASE gans;

-- Uncomment the following line to drop the 'gans' database if it already exists
-- DROP DATABASE gans;

-- Switch to the 'gans' database
USE gans;

-- Create a table to store city information
CREATE TABLE cities (
    city_id INT AUTO_INCREMENT, -- Unique identifier for each city
    city_name VARCHAR(200), -- Name of the city
    country_code VARCHAR(20), -- Country code of the city
    latitude FLOAT, -- Latitude of the city's location
    longitude FLOAT, -- Longitude of the city's location
    PRIMARY KEY(city_id) -- Define city_id as the primary key
);

-- Uncomment the following lines to drop, truncate, or delete from the 'cities' table
-- DROP TABLE cities;
-- TRUNCATE TABLE cities;
-- DELETE FROM cities;

-- Example insert statements to add cities to the 'cities' table
/*
INSERT INTO cities (city_name, country_code) VALUES ('Berlin','DE');
INSERT INTO cities (city_name, country_code) VALUES ('Munich','DE');
INSERT INTO cities (city_name, country_code) VALUES ('Frankfurt','DE');
INSERT INTO cities (city_name, country_code) VALUES ('London','UK');
INSERT INTO cities (city_name, country_code) VALUES ('Copenhaguen','DK');
*/

-- Select all records from the 'cities' table
SELECT * FROM cities;

-- Create a table to store population information for each city
CREATE TABLE population (
    city_id INT, -- Reference to the city's unique identifier
    population INT, -- Population of the city
    timestamp_population YEAR, -- Year of the population record
    PRIMARY KEY(city_id, timestamp_population), -- Define a composite primary key
    FOREIGN KEY(city_id) REFERENCES cities(city_id) -- Define a foreign key constraint
);

-- Example insert statements to add population records to the 'population' table
/*
INSERT INTO population(city_id, population, timestamp_population) VALUES (1, 3850809, 2023);
INSERT INTO population(city_id, population, timestamp_population) VALUES (2, 1512491, 2023);
INSERT INTO population(city_id, population, timestamp_population) VALUES (3, 773068, 2023);
INSERT INTO population(city_id, population, timestamp_population) VALUES (4, 8799800, 2023);
INSERT INTO population(city_id, population, timestamp_population) VALUES (5, 660842, 2023);
*/

-- Uncomment the following line to drop the 'population' table
-- DROP TABLE population;

-- Select all records from the 'population' table
SELECT * from population;

-- Create a table to store information about airports in cities
CREATE TABLE cities_airports (
    city_id INT, -- Reference to the city's unique identifier
    airport_icao VARCHAR(100), -- ICAO code of the airport
    airport_name VARCHAR(100), -- Name of the airport
    PRIMARY KEY(airport_icao), -- Define airport_icao as the primary key
    FOREIGN KEY(city_id) REFERENCES cities(city_id) -- Define a foreign key constraint
);

-- Example insert statements to add airport records to the 'cities_airports' table
/*
INSERT INTO cities_airports(city_id, airport_icao, airport_name) VALUES(1,'EDDB','Berlin');
INSERT INTO cities_airports(city_id, airport_icao, airport_name) VALUES(2,'EKCH','Copenhaguen');
INSERT INTO cities_airports(city_id, airport_icao, airport_name) VALUES(3,'EDDM','Munich');
INSERT INTO cities_airports(city_id, airport_icao, airport_name) VALUES(4,'EDDF','Frankfurt');
INSERT INTO cities_airports(city_id, airport_icao, airport_name) VALUES(5,'EGLL','London');
INSERT INTO cities_airports(city_id, airport_icao, airport_name) VALUES(5,'EGKK','London');
INSERT INTO cities_airports(city_id, airport_icao, airport_name) VALUES(5,'EGLL','London');
*/

-- Uncomment the following line to drop the 'cities_airports' table
-- DROP TABLE cities_airports;

-- Select all records from the 'cities_airports' table
SELECT * FROM cities_airports;

-- Create a table to store weather forecast information for each city
CREATE TABLE forecast (
    city_id INT, -- Reference to the city's unique identifier
    temperature FLOAT, -- Temperature forecast
    min FLOAT, -- Minimum temperature forecast
    max FLOAT, -- Maximum temperature forecast
    humidity INT, -- Humidity forecast
    weather VARCHAR(200), -- Weather condition
    description TEXT, -- Description of the weather condition
    wind_speed FLOAT, -- Wind speed forecast
    visibility INT, -- Visibility forecast
    forecast_time DATETIME, -- Time of the forecast
    FOREIGN KEY(city_id) REFERENCES cities(city_id) -- Define a foreign key constraint
);

-- Select all records from the 'forecast' table
SELECT * FROM forecast;

-- Uncomment the following lines to drop, truncate, or delete from the 'forecast' table
-- DROP TABLE forecast;
-- TRUNCATE TABLE forecast;

-- Create a table to store flight information
CREATE TABLE flights (
    flight_id INT AUTO_INCREMENT, -- Unique identifier for each flight
    airport_icao VARCHAR(100), -- ICAO code of the arrival airport
    departure_airport_icao VARCHAR(100), -- ICAO code of the departure airport
    departure_airport_name VARCHAR(200), -- Name of the departure airport
    scheduled_time DATETIME, -- Scheduled departure time
    revised_time DATETIME, -- Revised departure time, if any
    flight_number VARCHAR(100), -- Flight number
    flight_status VARCHAR(100), -- Status of the flight
    aircraft_used VARCHAR(200), -- Aircraft used for the flight
    airline_name VARCHAR(200), -- Name of the airline
    PRIMARY KEY(flight_id), -- Define flight_id as the primary key
    FOREIGN KEY(airport_icao) REFERENCES cities_airports(airport_icao) -- Define a foreign key constraint
);

-- Uncomment the following lines to drop, truncate, or delete from the 'flights' table
-- DROP TABLE flights;
-- TRUNCATE TABLE flights;

-- Select all records from the 'flights' table
SELECT * FROM flights;