from pyspark.sql.functions import col, acos, cos, sin, lit, radians
from pyspark.sql import Column

def harvesine_distance(long_x: str, lat_x: str, long_y: str, lat_y: str)-> Column:
    '''
    The haversine formula determines the great-circle distance between two points on a sphere given their longitudes and latitudes.
    ''' 
    return acos(
        sin(radians(lat_x)) * sin(radians(lat_y)) + 
        cos(radians(lat_x)) * cos(radians(lat_y)) * 
            cos(radians(long_x) - radians(long_y))
    ) * lit(6371.0)