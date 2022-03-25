from pyspark.sql.types import StructType,StructField, StringType, IntegerType

service_id = "service_id"
date = "date"
exception_type = "exception_type"

schema = StructType([
    StructField(service_id, IntegerType(),True), 
    StructField(date, StringType(),True), 
    StructField(exception_type, IntegerType(),True)
  ])