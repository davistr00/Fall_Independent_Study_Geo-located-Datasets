import csv
import psycopg2

#Database connection
db = psycopg2.connect("host=localhost dbname=footTraffic user=YOUR_SUPERUSER password=YOUR_PASSWORD")
cur = db.cursor()

#Reads in Traffic Sample
reader = csv.reader("YOUR_FILE_PATH/Traffic_CSV_Sample.csv")
for row in reader:
        # This is the insert
    insert_sql = (
        'INSERT INTO public.\"Traffic\"(placekey,parent_placekey, safegraph_brand_ids,location_name,brands,store_id,top_category,sub_category,naics_code,latitude, longitude,street_address,city,region,postal_code,open_hours,category_tags,opened_on,closed_on,tracking_closed_since,websites,geometry_type,polygon_wkt,polygon_class,enclosed,phone_number,is_synthetic,includes_parking,iso_country_code,wkt_area_sq_meters,date_range_start,date_range_end,raw_visit_counts,raw_visitor_counts, visits_by_day, visits_by_each_hour, poi_cbg, visitor_home_cbgs, visitor_home_aggregation, visitor_daytime_cbgs, visitor_country_of_origin, distance_from_home, median_dwell, bucketed_dwell_times, related_same_day_brand, related_same_week_brand, device_type, normalized_visits_by_state_scaling, normalized_visits_by_region_naics_visits, normalized_visits_by_region_naics_visitors, normalized_visits_by_total_visits,normalized_visits_by_total_visitors) '
        'VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING;')
    cur.execute(insert_sql, row)
    db.commit()

#Reads in Location Sample
reader = csv.reader("YOUR_FILE_PATH/Location_CSV_Sample.csv")
for row in reader:
    #This is the insert
    insert_sql = ('INSERT INTO public.\"Location\"(placekey, parent_placekey, safegraph_brand_ids, location_name, brands, store_id, top_category, sub_category, naics_code, latitude, longitude, street_address, city, region, postal_code, open_hours, category_tags, opened_on, closed_on, tracking_closed_on, geometry_type, polygon_wkt, polygon_class, enclosed, phone_number, is_synthetic, includes_parking_lot, iso_country_code, wkt_area_sq_meters, domains, website) '
                  'VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING;')
    cur.execute(insert_sql, row)
    db.commit()

#Reads in Location Sample
reader = csv.reader("YOUR_FILE_PATH/Location_CSV_Sample.csv")
for row in reader:
    #This is the insert
    insert_sql = ('INSERT INTO public.\"Brand\"(safegraph_brand_ids, brand_name, parent_safegraph_brand_id, naics_code,top_category, sub_category, stock_symbol, stock_exchange, iso_country_codes_open, iso_country_codes_closed) '
                  'VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING;')
    cur.execute(insert_sql, row)
    db.commit()