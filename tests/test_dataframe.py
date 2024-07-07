import os
import pandas as pd
import numpy as np


base_dir = os.path.abspath(os.path.dirname(__file__))

test_data_dir = os.path.join(base_dir, r'data')


def test_indexed_date_range():

    s = pd.date_range(start='2015-06-01', end='2024-05-01', freq='D').to_series()
    date_range_list = list(zip(s.dt.strftime('%Y-%m-%d'), s.shift(-30).dropna().dt.strftime('%Y-%m-%d')))

    business_s = pd.bdate_range(start='2019-06-01', end='2019-07-01', freq='D').to_series()
    bdate_range_list = list(zip(s.dt.strftime('%Y-%m-%d'), business_s.shift(-30).dropna().dt.strftime('%Y-%m-%d')))

    assert len(date_range_list) > 0


    r = pd.date_range(start='2019-06-01', end='2019-07-01').strftime('%Y-%m-%d').values

def rolling_window(a, window):
    shape = a.shape[:-1] + (a.shape[-1] - window + 1, window)
    strides = a.strides + (a.strides[-1],)
    # return np.lib.stride_tricks.as_strided(a, shape=shape, strides=strides)
    l1 = list(map(tuple, rolling_window(r, 3)[:, [0, -1]].tolist()))

def test_vol_grouping():

    fname = 'prices.csv'
    fpath = os.path.join(test_data_dir, fname)
    df = pd.read_csv(fpath)

    # Splitting into Series

    series = [y for x, y in df.groupby('date', as_index=False)]

    df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
    df['year'] = df['date'].dt.year
    
    # Get max volume for every year

    # 1. idxmax

    max_vol_df = df.loc[df.groupby(['date']).idxmax()]
    assert len(max_vol_df) > 0

def test_splitting_ts():

    df = pd.DataFrame(
        columns = ['date', 'tenor', 'price'],
        data = [
            ['2024-05-01', '4w', 0.5],
            ['2024-05-01', '13w', 0.6],
            ['2024-05-01', '26w', 0.7],
            ['2024-05-02', '4w', 0.5],
            ['2024-05-02', '13w', 0.6],
            ['2024-05-02', '26w', 0.7],

        ]
    )

    series = [y for x, y in df.groupby('date', as_index=False)]

    assert len(series) > 0

def test_as_of_merge_dataframe():

    left = pd.DataFrame({'a': [1, 5, 10], 'left_val': ['a', 'b', 'c']})

    right = pd.DataFrame({'a': [1, 2, 3, 6, 7],'right_val': [1, 2, 3, 6, 7]})

    pd.merge_asof(left, right, on='a')

    pd.merge_asof(left, right, on='a', allow_exact_matches=False)

    pd.merge_asof(left, right, on='a', direction='forward')

    pd.merge_asof(left, right, on='a', direction='nearest')



 

    

