from pyspark.sql.types import StructType,StructField, StringType, IntegerType

route_id = "route_id"
service_id = "service_id"
trip_id = "trip_id"
trip_headsign = "trip_headsign"

schema = StructType([
    StructField(route_id, IntegerType(),True), 
    StructField(service_id, StringType(),True), 
    StructField(trip_id, IntegerType(),True),
    StructField(trip_headsign, StringType(),True)
  ])