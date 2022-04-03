import pytest
import pandas as pd
from gtfs_utils.harvesine import harvesine_distance
from gtfs_utils.time import fix_gtfs_time

def test_fix_gtfs_time():
    input_cols = ['a', 'b']
    input_data = pd.DataFrame({'a': ['23:59:59'], 'b': ['24:05:10']})

    expected = pd.DataFrame({'a': [pd.to_datetime('2020-01-01 23:59:59')], 'b': [pd.to_datetime('2020-01-02 00:05:10')]})

    actual = fix_gtfs_time(input_data, input_cols, '2020-01-01')
    print(actual)
    pd.testing.assert_frame_equal(expected, actual)

def test_harvesine_distance():
    harvesine_col = 'harvesine'
    input_cols = ['lon_x', 'lat_x', 'lon_y', 'lat_y']

    input_data = pd.DataFrame({'lon_x': [0.1246], 'lat_x': [51.5007],'lon_y': [74.0445], 'lat_y':[40.6892]})

    expected = pd.DataFrame({harvesine_col: [5574.8405] })

    actual = input_data.apply(lambda x: harvesine_distance(*[x[col] for col in input_cols]), axis=1).to_frame(name=harvesine_col)
    print(actual)
    pd.testing.assert_frame_equal(expected, actual)
