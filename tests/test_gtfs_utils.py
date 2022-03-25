import pytest
from pyspark.sql.functions import col, round
from pyspark.sql import SparkSession

from gtfs_utils.harvesine import harvesine_distance
from gtfs_utils.time import fix_gtfs_time

@pytest.fixture(scope='session')
def spark():
    return SparkSession.builder \
      .master("local") \
      .appName("chispa") \
      .getOrCreate()

def test_fix_gtfs_time(spark):
    input_cols = ["a", "b"]
    input_data = spark.createDataFrame([
            ['23:59:59', '24:05:10']
           ], input_cols
    )
    

    expected = spark.createDataFrame([
        ["2020-01-01 23:59:59", "2020-01-02 00:05:10"],
    ], input_cols)

    actual = fix_gtfs_time(input_data, input_cols, "2020-01-01")
    assert expected.subtract(actual).count() == 0

def test_harvesine_distance(spark):
    harvesine_col = "harvesine"
    input_cols = ["lon_x", "lat_x", "lon_y", "lat_y"]

    input_data = spark.createDataFrame([
            ['0.1246','51.5007','74.0445','40.6892']
           ], input_cols
    )

    expected = spark.createDataFrame([
        [5574.8405]
    ], [harvesine_col])

    actual = input_data\
    .withColumn(harvesine_col, harvesine_distance(*[col(a) for a in input_cols]))\
    .select(round(col(harvesine_col), 4).alias(harvesine_col))

    actual.show()
    expected.show()
    assert expected.subtract(actual).count() == 0