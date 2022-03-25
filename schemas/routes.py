from pyspark.sql.types import StructType,StructField, StringType, IntegerType

route_id = "route_id"
agency_id = "agency_id"
route_short_name = "route_short_name"
route_long_name = "route_long_name"
route_type = "route_type"
route_color = "route_color"
route_url = "route_url"

schema = StructType([
  StructField(route_id, IntegerType(), True),
  StructField(agency_id, IntegerType(), True),
  StructField(route_short_name, IntegerType(), True),
  StructField(route_long_name, StringType(), True),
  StructField(route_type, IntegerType(), True),
  StructField(route_color, IntegerType(), True),
  StructField(route_url, StringType(), True)
])
