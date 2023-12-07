# Code by Toni Davis
# Code References for API Connection and File Download https://community.deweydata.io/t/bulk-downloading-data-using-v3-api-using-python/26533#h-2-get-a-product-path-2
import csv
import requests
import psycopg2
import gzip
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
db = psycopg2.connect("host=localhost dbname=footTraffic user=ENTER YOUR USER HERE password password=ENTER YOUR PASSWORD HERE")
cur = db.cursor()

#API Key
API_KEY = "ENTER YOUR API KEY HERE"

#Advan Data Path
Advan_Path = "ENTER YOUR API LINK HERE"

#collects result json objects from safegraph/advan
results = requests.get(url=Advan_Path,
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
            # This is the insert
            insert_sql = (
                'INSERT INTO public.\"Traffic\"(placekey,parent_placekey, safegraph_brand_ids,location_name,brands,store_id,top_category,sub_category,naics_code,latitude, longitude,street_address,city,region,postal_code,open_hours,category_tags,opened_on,closed_on,tracking_closed_since,websites,geometry_type,polygon_wkt,polygon_class,enclosed,phone_number,is_synthetic,includes_parking,iso_country_code,wkt_area_sq_meters,date_range_start,date_range_end,raw_visit_counts,raw_visitor_counts, visits_by_day, visits_by_each_hour, poi_cbg, visitor_home_cbgs, visitor_home_aggregation, visitor_daytime_cbgs, visitor_country_of_origin, distance_from_home, median_dwell, bucketed_dwell_times, related_same_day_brand, related_same_week_brand, device_type, normalized_visits_by_state_scaling, normalized_visits_by_region_naics_visits, normalized_visits_by_region_naics_visitors, normalized_visits_by_total_visits,normalized_visits_by_total_visitors) '
                'VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING;')
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

