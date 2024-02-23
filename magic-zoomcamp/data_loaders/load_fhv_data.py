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
    dfs = []

    for month in range(1, 13):
        t_start = time()
        if month < 10:
            url = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/fhv/fhv_tripdata_2019-0' + str(month) + '.csv.gz'
        else:
            url = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/fhv/fhv_tripdata_2019-' + str(month) + '.csv.gz'
        
        add = pd.read_csv(
            url, 
            engine="pyarrow", 
            compression='gzip',
        )
        
        dfs.append(add)

        t_end = time()
        print('appended ' + str(month) + '... it took %.3f seconds' % (t_end - t_start))
    
    print('doing final concat')
    
    df = pd.DataFrame()
    for d in dfs:
        final_df =  df.append(d, ignore_index=True)
    return final_df

@test
def test_output(output, *args) -> None:
    assert output is not None, 'The output is undefined'