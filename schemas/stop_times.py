from pyspark.sql.types import StructType,StructField, StringType, IntegerType

trip_id = "trip_id"
arrival_time = "arrival_time"
departure_time = "departure_time"
stop_id = "stop_id"
stop_sequence = "stop_sequence"

schema = StructType([
  StructField(trip_id, StringType(), True),
  StructField(arrival_time, StringType(), True),
  StructField(departure_time, StringType(), True),
  StructField(stop_id, StringType(), True),
  StructField(stop_sequence, IntegerType(), True)
])

