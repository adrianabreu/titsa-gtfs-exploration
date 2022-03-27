from pyspark.sql import DataFrame, Column
from pyspark.sql.types import TimestampType, IntegerType
from pyspark.sql.functions import col, lit, when, length, concat, unix_timestamp

def fix_gtfs_time(df: DataFrame, cols: [str], date: str)-> DataFrame: 
    '''
    This method converts the problematic gtfs format (which goes from 00:00:00 to 27:00:00) into a valid date time format
    It will append the time to the current date applying the extra hours to the next day.
    For example for the following row:
    
    |r | a |  b |
    | -- | -- | -- |
    | 1 | 23:50:00 | 24:15:00 |

    And the date 2022-03-15, it will yield:

     |r | a |  b |
    | -- | -- | -- |
    | 1 | 2022-03-15 23:50:00 | 2022-03-16 00:15:00 |   

    ''' 
    for col_name in cols:
        df = df\
        .withColumn(col_name + "_day", when(col(col_name) > '23:59:59', 1).otherwise(0))\
        .withColumn(
            col_name, 
            when(col(col_name) > '23:59:59', concat(col(col_name).substr(lit(1), lit(2)).cast(IntegerType()) - 24, col(col_name).substr(lit(3), length(col_name) - 2)))
            .otherwise(col(col_name))
                   )\
        .withColumn(col_name, concat(lit(date + " "), col(col_name)).cast(TimestampType()))\
        .withColumn(col_name, (unix_timestamp(col_name) + col(col_name + '_day') * 24 * 60 * 60).cast(TimestampType()))\
        .drop(col_name + "_day")
    return df