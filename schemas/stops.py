from pyspark.sql.types import StructType,StructField, StringType, IntegerType

stop_id = "stop_id"
stop_name = "stop_name"
stop_lat = "stop_lat"
stop_lon = "stop_lon"
stop_url = "stop_url"

schema = StructType([
  StructField(stop_id,StringType(),True),
  StructField(stop_name,StringType(),True),
  StructField(stop_lat,StringType(),True),
  StructField(stop_lon,StringType(),True),
  StructField(stop_url,StringType(),True)
])
