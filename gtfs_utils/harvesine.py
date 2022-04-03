from math import radians, cos, sin, asin, sqrt, acos

def harvesine_distance(long_x, lat_x, long_y, lat_y):
    '''
    The haversine formula determines the great-circle distance between two points on a sphere given their longitudes and latitudes.
    ''' 
    return acos(
        sin(radians(lat_x)) * sin(radians(lat_y)) + 
        cos(radians(lat_x)) * cos(radians(lat_y)) * 
            cos(radians(long_x) - radians(long_y))
    ) * 6371.0
