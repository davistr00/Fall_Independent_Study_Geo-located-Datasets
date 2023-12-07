# Code by Toni Davis
# Code References for API Connection and File Download https://community.deweydata.io/t/bulk-downloading-data-using-v3-api-using-python/26533#h-2-get-a-product-path-2
import requests
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
db = psycopg2.connect("host=localhost dbname=footTraffic user=YOUR_SUPERUSER password=YOUR_PASSWORD")
cur = db.cursor()

#API Key
API_KEY = "YOUR_API_KEY"

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
        reader = csv.reader("YOUR_FILE_PATH/Location_CSV_Sample.csv")
        for row in reader:
            # This is the insert
            insert_sql = (
                'INSERT INTO public.\"Brand\"(safegraph_brand_ids, brand_name, parent_safegraph_brand_id, naics_code,top_category, sub_category, stock_symbol, stock_exchange, iso_country_codes_open, iso_country_codes_closed) '
                'VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING;')
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