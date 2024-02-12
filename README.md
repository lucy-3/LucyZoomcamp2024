# LucyZoomcamp2024

# HW3 Queries

# create external table from gcs path
CREATE OR REPLACE EXTERNAL TABLE `ny-taxi-data-413601.ny_taxi.green_taxi_2022`
OPTIONS (
  format = 'parquet',
  uris = ['gs://ny-taxi-data-413601-terra-bucket/green_taxi_2022.parquet']
);

# create non partitioned table from external table
CREATE OR REPLACE TABLE ny-taxi-data-413601.ny_taxi.green_taxi_trips_2022 AS
SELECT * FROM ny-taxi-data-413601.ny_taxi.green_taxi_2022;

# create partitioned and clustered table from external table
CREATE OR REPLACE TABLE ny-taxi-data-413601.ny_taxi.green_taxi_trips_2022_partitioned
PARTITION BY lpep_pickup_date
CLUSTER BY (PULocationID) AS
SELECT * FROM ny-taxi-data-413601.ny_taxi.green_taxi_2022;

# non partitioned count
SELECT count(distinct PULocationID) FROM `ny-taxi-data-413601.ny_taxi.green_taxi_trips_2022`
where lpep_pickup_date BETWEEN '2022-06-01' and '2022-06-30';

# partitioned count
SELECT count(distinct PULocationID) FROM `ny-taxi-data-413601.ny_taxi.green_taxi_trips_2022_partitioned`
where lpep_pickup_date BETWEEN '2022-06-01' and '2022-06-30';