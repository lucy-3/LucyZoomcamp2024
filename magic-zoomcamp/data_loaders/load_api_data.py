import io
import os
import pandas as pd
import requests
from time import time
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    taxi_dtypes = {
        'VendorID': pd.Int64Dtype(),
        'passenger_count': pd.Int64Dtype(),
        'trip_distance': float,
        'RatecodeID': pd.Int64Dtype(),
        'store_and_fwd_flag' :str,
        'PULocationID': pd.Int64Dtype(),
        'DOLocationID': pd.Int64Dtype(),
        'payment_type': pd.Int64Dtype(),
        'fare_amount': float,
        'extra': float,
        'mta_tax': float,
        'tip_amount': float,
        'tolls_amount': float,
        'improvement_surcharge': float,
        'total_amount': float,
        'congestion_surcharge': float
    }

    parse_dates = ['lpep_pickup_datetime', 'lpep_dropoff_datetime']

    dfs = []

    for year in range(2019, 2021): 
        for month in range(1, 13):
            t_start = time()
            if month < 10:
                url = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_'+ str(year) + '-0' + str(month) + '.csv.gz'

            else:
                url = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_'+ str(year) + '-' + str(month) + '.csv.gz'

            add = pd.read_csv(
                url, 
                engine="pyarrow", 
                compression='gzip',
                # dtype=taxi_dtypes, 
                # parse_dates=parse_dates
            )
            dfs.append(add)

            t_end = time()
            print('inserted ' + str(year) + '-' + str(month) + '... it took %.3f seconds' % (t_end - t_start))
    
    print('starting final concat')

    df = pd.DataFrame()

    for d in dfs:
        final_df = df.append(d, ignore_index=True)

    return df

@test
def test_output(output, *args) -> None:
    assert output is not None, 'The output is undefined'
