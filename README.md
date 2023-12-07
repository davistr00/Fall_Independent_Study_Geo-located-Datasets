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

"safegraph_brand_id"	"brand_name"	"parent_safegraph_brand_id"	"naics_code"	"top_category"	"sub_category"	"stock_symbol"	"stock_exchange"	"iso_country_codes_open"	"iso_country_codes_closed"
"SG_BRAND_000a715912215622"	"Good Earth Coffeehouse"		"722513"	"Restaurants and Other Eating Places"	"Limited-Service Restaurants"			"[CA]"	"[CA]"
"SG_BRAND_000b4281ac65a291"	"CareWell Urgent Care"		"621493"	"Outpatient Care Centers"	"Freestanding Ambulatory Surgical and Emergency Centers"			"[US]"	"[]"
"SG_BRAND_00212215412d108904aad380c025632e"	"Kloeckner Metals"		"332313"	"Architectural and Structural Metals Manufacturing"	"Plate Work Manufacturing"			"[MX,US]"	"[US]"

The Location data collected has 31 columns. This table is meant to be regularly updated as more data is released. The location data is comprised of a placekey, parent placekey, safegraph brand ID, location name, top category, sub category, nacis code, latitude, longitude, street address, city, region, postal code, open hours, category tags, opened on, closed on, tracking closed on, geometry type, polygon weight, polygon class, enclosed, phone number, if it is synthetic, if it includes parking, iso country code, weighted area in square meters, domains, websites. 

The Traffic data collected has 52 columns. The Traffic table like the Location table is meant to be regularly updated to as more data is released. The Traffic data is comprised of placekey, parent placekey, safegraph brand ID, location name, brands, store ID, top category, sub category, naics code, latitude, longitude, street address, city, region, postal code, open hours, category tags, opened on, closed on, tacking closed since, websites, geometry type, polygon weight, polygon class, enclosed, phone number, if it is synthetic, if it includes parking, iso country code, 
