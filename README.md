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
code(https://github.com/davistr00/Fall_Independent_Study_Geo-located-Datasets/blob/c47f66a97522a5cfdbfb7673677a30f0ec379d4c/Brand%20CSV%20Sample.csv)

The Location data collected has 31 columns. This table is meant to be regularly updated as more data is released. The location data is comprised of a placekey, parent placekey, safegraph brand ID, location name, top category, sub category, nacis code, latitude, longitude, street address, city, region, postal code, open hours, category tags, opened on, closed on, tracking closed on, geometry type, polygon weight, polygon class, enclosed, phone number, if it is synthetic, if it includes parking, iso country code, weighted area in square meters, domains, websites. 
![image](https://github.com/davistr00/Fall_Independent_Study_Geo-located-Datasets/assets/125899195/f731ffdf-de2c-443a-908a-c9707bb7ce6d)

The Traffic data collected has 52 columns. The Traffic table like the Location table is meant to be regularly updated to as more data is released. The Traffic data is comprised of placekey, parent placekey, safegraph brand ID, location name, brands, store ID, top category, sub category, naics code, latitude, longitude, street address, city, region, postal code, open hours, category tags, opened on, closed on, tacking closed since, websites, geometry type, polygon weight, polygon class, enclosed, phone number, if it is synthetic, if it includes parking, iso country code, weighted area in square meters, montering date range start, monitering date range end, raw visit counts, raw visitor counts, visits by day, visits by hour, POI cbg, vistor home cbgs, vistor home aggregation, vistor daytime cbgs, visitor country of origin, distance form home, median dwell, bucketed dwell times,related same day brand visits,related same week brand visits, device type, normalized visits by state scaling, normalized visits by region naics visits, normailized visitis by region naics visitors, normalized visits by total visits, normalized visits by total visitors.
![image](https://github.com/davistr00/Fall_Independent_Study_Geo-located-Datasets/assets/125899195/04f822f5-52c5-484b-9984-85dd367fb400)

* Sample CSV Files for Brands, Location, and Traffic are provided

# How to Recreate the project
- Make sure your system is up-to date and follows the system requirments set above.
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
- # Inserting Values Into The Database (Samples CSVs)
   - Download the sample [Brand](https://github.com/davistr00/Fall_Independent_Study_Geo-located-Datasets/blob/main/Brand%20CSV%20Sample.csv), [Location](https://github.com/davistr00/Fall_Independent_Study_Geo-located-Datasets/blob/main/Location%20CSV%20Sample.csv), and [Traffic](https://github.com/davistr00/Fall_Independent_Study_Geo-located-Datasets/blob/main/Traffic%20CSV%20Sample.csv) csv files and place them in an area that is easy to find.
   - For the samples you can run the [Sample_Insert.py](Sample_Insert.py) script. You will need to open the script and enter your Superuser name and password to your database server.
     ![image](https://github.com/davistr00/Fall_Independent_Study_Geo-located-Datasets/assets/125899195/0a8ca067-7c2e-48c3-aed5-86e70386403f)
   - Once the script completes you should have 100 rows of data in each of the 3 tables. 

- # Inserting Values Into The Database (Dewey API Calls/ Full Dataset)
    - You will need an account to Dewey Data (https://auth.deweydata.io/)
    - You will need to set up an API Key. For a how to on setting up an API key follow the tutorial [here](https://community.deweydata.io/t/bulk-downloading-data-using-v3-api-using-python/26533) or see the image below Save this API key as you will need it later.
      ![Dewey Part1](https://github.com/davistr00/Fall_Independent_Study_Geo-located-Datasets/assets/125899195/cb4b87ca-0257-461e-bc75-8842f8760d5a)
      image from:https://community.deweydata.io/t/bulk-downloading-data-using-v3-api-using-python/26533

    - Once you have an account and API Key you will need to subscribe to Global Places (POI) & Geometry and Brand Info from SafeGraph and Weekly Patterns - Foot Traffic from Advan. You will follow the same tutorial above or the image below to set up the subscriptions and to collect the connection urls.
      ![Dewey Part 2](https://github.com/davistr00/Fall_Independent_Study_Geo-located-Datasets/assets/125899195/e2b4625b-74e5-4110-8720-40eced3a8333)
      image from:https://community.deweydata.io/t/bulk-downloading-data-using-v3-api-using-python/26533
    - You will need to download the [brandsUpload.py](brandsUpload.py), [locationUpload.py](locationUpload.py), and [trafficUpload.py](trafficUpload.py) scripts and store them in an easy to find area.
    - Depending on which table you want to update you will open that upload file. For example, if you want to collect the values/update the Brand table you will open the brandUpload.py file.
    - Once you have the file open, you will need to Enter your superuser name and password in the directed fields.
      ![image](https://github.com/davistr00/Fall_Independent_Study_Geo-located-Datasets/assets/125899195/b6002ef4-beab-418b-bca0-32b210a33c1f)

    - You will then enter your API Key and API URL in the directed field. You will need to do this to all of the upload files.
    - 
      ![image](https://github.com/davistr00/Fall_Independent_Study_Geo-located-Datasets/assets/125899195/d974deeb-1836-4b7c-acac-c334205e55d9)

    - When you run the script the API will be called and the script will automatically collect file links.
    - 
      ![image](https://github.com/davistr00/Fall_Independent_Study_Geo-located-Datasets/assets/125899195/383df87c-052a-4477-a86b-4c3103e90e98)

    - For each file the file will be downloaded, unzipped, read each row into the corresponding database table, then deletes the file from storage.
    - 
      ![image](https://github.com/davistr00/Fall_Independent_Study_Geo-located-Datasets/assets/125899195/5b925fcc-12b6-4578-97e7-3c276bd0693e)
    - Once the scripts completes you can refresh your pgAdmin4 portal or run \l from the command line terminal in the bin directory to view your table and data. Below is a look at the first 100 rows of the traffic table in pgAdmin4
      ![image](https://github.com/davistr00/Fall_Independent_Study_Geo-located-Datasets/assets/125899195/991a0c4f-7e4b-42bd-8731-5eb33649a49e)

    - The data tables should look similar to the sample CSV files when looking at the database. 
    - * Some of the tables require a lot of storage to hold the database locally. The scripts may also take a while to complete depending on the size of the dataset you are collecting/updating.

# Have questions or suggestions?
  - Please reach out to me at tonidbusiness@gmail.com

