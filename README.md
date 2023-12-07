# Fall_Independent_Study_Geo-located-Datasets
This project's goal is to collect geo-spatial data and foot traffic data to create a postgres database to store the data. The database is also supposed to be easily updated as new data is avaiable. 

# System Requirements
- Python 3.11
- latest version of postgreSQL

# Required Python Packages
- csv
- requests
- psycopg2
- gzip

# Recommendations 
I highly recommend using pgAdmin4 to create and manage the database if you are planning to hold it locally on your machine. This system was created for postgreSQL and offers many tools to make it easy to make edits to the database, manage permissions, and any modifications needed. 

# The Data
For this project I used data from SafeGraph for location and brand data, and for the traffic data I pulled it from Advan.

The Brand data collected has 10 columns and 8657 rows. The brand data collects the safegraph brand ID, brand name, parent safegraph brand ID, naics code, top category, subcategory, stock symbol, stock exchange, iso country codes open, and iso country codes closed for each brand. 
![image](https://github.com/davistr00/Fall_Independent_Study_Geo-located-Datasets/assets/125899195/3b425a5e-5ddc-41a8-8dc2-3cf8f2a8de5a)


The Location data collected has 31 columns. This table is meant to be regularly updated as more data is released. The location data is comprised of a placekey, parent placekey, safegraph brand ID, location name, top category, sub category, nacis code, latitude, longitude, street address, city, region, postal code, open hours, category tags, opened on, closed on, tracking closed on, geometry type, polygon weight, polygon class, enclosed, phone number, if it is synthetic, if it includes parking, iso country code, weighted area in square meters, domains, websites. 
![image](https://github.com/davistr00/Fall_Independent_Study_Geo-located-Datasets/assets/125899195/f731ffdf-de2c-443a-908a-c9707bb7ce6d)

The Traffic data collected has 52 columns. The Traffic table like the Location table is meant to be regularly updated to as more data is released. The Traffic data is comprised of placekey, parent placekey, safegraph brand ID, location name, brands, store ID, top category, sub category, naics code, latitude, longitude, street address, city, region, postal code, open hours, category tags, opened on, closed on, tacking closed since, websites, geometry type, polygon weight, polygon class, enclosed, phone number, if it is synthetic, if it includes parking, iso country code, weighted area in square meters, montering date range start, monitering date range end, raw visit counts, raw visitor counts, visits by day, visits by hour, POI cbg, vistor home cbgs, vistor home aggregation, vistor daytime cbgs, visitor country of origin, distance form home, median dwell, bucketed dwell times,related same day brand visits,related same week brand visits, device type, normalized visits by state scaling, normalized visits by region naics visits, normailized visitis by region naics visitors, normalized visits by total visits, normalized visits by total visitors.
![image](https://github.com/davistr00/Fall_Independent_Study_Geo-located-Datasets/assets/125899195/04f822f5-52c5-484b-9984-85dd367fb400)

* Sample CSV Files for Brands, Location, and Traffic are provided

# How to Recreate the project
- Make sure your system is up-to date and follows the system requirments set above.
- 
- # Setting Up The Database
  - Download the Create.sql file and place it in an easy to find area
  - Make sure you have set up your superuser and password when you set up postgreSQL on your system.
  - You will then want to open up your command prompt terminal (you may need to run as admin if connecction error occurs)
  - Once inside the command prompt terminal you will want to navigate to your bin file a typical path for this folder will look like this "C:\Program Files\PostgreSQL\16\bin"
  - You will then create the database using the "createdb -U YOUR_SUPERUSER_NAME footTraffic" you will need to enter your superuser name in the command.
  - You will then need to enter your password you set for your superuser when setting up postgreSQL
  - Once completed you will run the command "psql -U YOUR_SUPERUSER_NAME -d footTraffic < FILE_PATH" you will again need to add in your superuser name and include the file path for the Create.sql file. You can also add the file directly in the bin file and just call Create.sql
  - You can then run \l to test that the database was added and set up or you can open pgAdmin4 and refresh your server to check the database initalization.

* If any issues with initalization occurs the indvidual create statements for the databases and the tables can be found in the Basic Database Creation file. These can be run in pgAdmin4 query tool or in MySQL.
- # Inserting Values Into The Database
   - Download the sample Brands, Location, and Traffic csv files and place them in an area that is easy to find.
   - For the samples you can run the Sample_Insert.py script. You will need to open the script and enter your Superuser name and password to your database server. 
