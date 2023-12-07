--
-- PostgreSQL database dump
--

-- Dumped from database version 16.1
-- Dumped by pg_dump version 16.1

-- Started on 2023-12-07 11:13:20

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 5786 (class 1262 OID 24590)
-- Name: footTraffic; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE "footTraffic" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_United States.1252';


ALTER DATABASE "footTraffic" OWNER TO postgres;

\connect "footTraffic"

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 2 (class 3079 OID 24599)
-- Name: postgis; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS postgis WITH SCHEMA public;


--
-- TOC entry 5787 (class 0 OID 0)
-- Dependencies: 2
-- Name: EXTENSION postgis; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION postgis IS 'PostGIS geometry and geography spatial types and functions';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 221 (class 1259 OID 32792)
-- Name: Brand; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Brand" (
    safegraph_brand_id character varying NOT NULL,
    brand_name character varying,
    parent_safegraph_brand_id character varying,
    naics_code character varying,
    top_category character varying,
    sub_category character varying,
    stock_symbol character varying,
    stock_exchange character varying,
    iso_country_codes_open character varying,
    iso_country_codes_closed character varying
);


ALTER TABLE public."Brand" OWNER TO postgres;

--
-- TOC entry 222 (class 1259 OID 41079)
-- Name: Location; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Location" (
    placekey text NOT NULL,
    parent_placekey text,
    safegraph_brand_ids text,
    location_name text,
    brands text,
    store_id text,
    top_category text,
    sub_category text,
    naics_code text,
    latitude text,
    longitude text,
    street_address text,
    city text,
    region text,
    postal_code text,
    open_hours text,
    category_tags text,
    opened_on text,
    closed_on text,
    tracking_closed_on text,
    geometry_type text,
    polygon_wkt text,
    polygon_class text,
    enclosed text,
    phone_number text,
    is_synthetic text,
    includes_parking_lot text,
    iso_country_code text,
    wkt_area_sq_meters text,
    domains text,
    website text
);


ALTER TABLE public."Location" OWNER TO postgres;

--
-- TOC entry 223 (class 1259 OID 488033)
-- Name: Traffic; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Traffic" (
    placekey text NOT NULL,
    parent_placekey text,
    safegraph_brand_ids text,
    location_name text,
    brands text,
    store_id text,
    top_category text,
    sub_category text,
    naics_code text,
    latitude text,
    longitude text,
    street_address text,
    city text,
    region text,
    postal_code text,
    open_hours text,
    category_tags text,
    opened_on text,
    closed_on text,
    tracking_closed_since text,
    websites text,
    geometry_type text,
    polygon_wkt text,
    polygon_class text,
    enclosed text,
    phone_number text,
    is_synthetic text,
    includes_parking text,
    iso_country_code text,
    wkt_area_sq_meters text,
    date_range_start text NOT NULL,
    date_range_end text NOT NULL,
    raw_visit_counts text,
    raw_visitor_counts text,
    visits_by_day text,
    visits_by_each_hour text,
    poi_cbg text,
    visitor_home_cbgs text,
    visitor_home_aggregation text,
    visitor_daytime_cbgs text,
    visitor_country_of_origin text,
    distance_from_home text,
    median_dwell text,
    bucketed_dwell_times text,
    related_same_day_brand text,
    related_same_week_brand text,
    device_type text,
    normalized_visits_by_state_scaling text,
    normalized_visits_by_region_naics_visits text,
    normalized_visits_by_region_naics_visitors text,
    normalized_visits_by_total_visits text,
    normalized_visits_by_total_visitors text
);


ALTER TABLE public."Traffic" OWNER TO postgres;

-- Completed on 2023-12-07 11:13:27

--
-- PostgreSQL database dump complete
--

