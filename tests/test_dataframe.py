import pandas as pd
import numpy as np


def test_indexed_date_range():

    s = pd.date_range(start='2019-06-01', end='2019-07-01', freq='D').to_series()
    date_range_list = list(zip(s.dt.strftime('%Y-%m-%d'), s.shift(-2).dropna().dt.strftime('%Y-%m-%d')))

    assert len(date_range_list) > 0


    r = pd.date_range(start='2019-06-01', end='2019-07-01').strftime('%Y-%m-%d').values

# def rolling_window(a, window):
#     shape = a.shape[:-1] + (a.shape[-1] - window + 1, window)
#     strides = a.strides + (a.strides[-1],)
#     return np.lib.stride_tricks.as_strided(a, shape=shape, strides=strides)
# L1 = list(map(tuple, rolling_window(r, 3)[:, [0, -1]].tolist()))


