# import requests
import csv
import requests
import psycopg2
import pandas as pd
import gzip
import io
import sys
import os

#This allows the program to continue running and not running into a Overflow error
maxInt = sys.maxsize

while True:
    # decrease the maxInt value by factor 10
    # as long as the OverflowError occurs.

    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt/10)


#database connection
db = psycopg2.connect("host=localhost dbname=footTraffic user=YOUR_SUPER_USER password=YOUR_PASSWORD")
cur = db.cursor()

#API Key
API_KEY = "ENTER_YOUR_API_KEY"

#Safegraph Data Path
safegraph_Path = "YOUR_API_LINK"

#collects result json objects from safegraph/advan
results = requests.get(url=safegraph_Path,
                           headers={'X-API-KEY': API_KEY,
                                    'accept': 'application/json'
                                   })
response_json = results.json()

#Here links are collected and formal get requests are placed
for link_data in response_json['download_links']:
    data=requests.get(link_data['link'])

    #The file is writen on to storage
    with open(link_data['file_name'], 'wb') as file:
        file.write(data.content)

    #The file is unziped, read as a csv and then inserted into the database table
    with gzip.open(link_data['file_name'], 'rt', newline='',encoding='utf8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            #This is the insert
            insert_sql = ('INSERT INTO public.\"Location\"(placekey, parent_placekey, safegraph_brand_ids, location_name, brands, store_id, top_category, sub_category, naics_code, latitude, longitude, street_address, city, region, postal_code, open_hours, category_tags, opened_on, closed_on, tracking_closed_on, geometry_type, polygon_wkt, polygon_class, enclosed, phone_number, is_synthetic, includes_parking_lot, iso_country_code, wkt_area_sq_meters, domains, website) '
                          'VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING;')
            cur.execute(insert_sql, row)
            db.commit()
        else:
            print("End of file")
        #Here the file is removed from storage
        csvfile.close()
        print(link_data['file_name'],'closed')
        os.remove(link_data['file_name'])

#Connections Closed
cur.close()
db.close()