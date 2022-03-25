from pyspark.sql.types import StructType,StructField, StringType, IntegerType

agency_id = "agency_id"
agency_name = "agency_name"
agency_url = "agency_url"
agency_timezone = "agency_timezone"
agency_lang = "agency_lang"
agency_phone = "agency_phone"

schema = StructType([
    StructField(agency_id, IntegerType(),True), 
    StructField(agency_name, StringType(),True), 
    StructField(agency_url, StringType(),True), 
    StructField(agency_timezone,  StringType(), True), 
    StructField(agency_lang,  StringType(), True), 
    StructField(agency_phone,  StringType(), True)
  ])