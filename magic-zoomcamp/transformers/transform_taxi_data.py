if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    data['check'] = data['passenger_count'] + data['trip_distance']
    print(f"Prepocessing: rows with zero trip distance: {data['trip_distance'].isin([0]).sum()}")
    print(f"Prepocessing: rows with zero passenger count: {data['passenger_count'].isin([0]).sum()}")

    return data[(data['passenger_count'] > 0) & (data['trip_distance'] > 0)]