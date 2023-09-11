# Databricks notebook source
import time
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField,StringType, DateType,DoubleType,LongType,TimestampType, IntegerType, ArrayType, NullType
from pyspark.sql.functions import from_json, col ,round, current_timestamp, explode, from_unixtime, to_utc_timestamp,from_utc_timestamp
import json
from pyspark.sql.functions import col, schema_of_json,get_json_object

ReadFinhub = spark.readStream \
  .format("kafka") \
  .option("kafka.bootstrap.servers", "ec2-3-22-66-169.us-east-2.compute.amazonaws.com:9092") \
  .option("subscribe", "Finhub1") \
  .option("failOnDataLoss", "false")\
  .option("includeHeaders", "true") \
  .option("startingOffsets", "latest") \
  .load()
  

schema = StructType([
    StructField("data", ArrayType(
        StructType([
            StructField("c", StringType(), True),  
            StructField("p", DoubleType(), True),  
            StructField("s", StringType(), True),  
            StructField("t", LongType(), True),   
            StructField("v", DoubleType(), True)   
        ])
    ), True),  
    
    StructField("type", StringType(), True)  
])


JsonDF = ReadFinhub.select(from_json(col("value").cast("string"), schema).alias("data"))
ExplodedDF =JsonDF.select(explode("data.data").alias("exploded"))
                                
selected_df = ExplodedDF.select("exploded.p", "exploded.s", "exploded.t", "exploded.v")

renameDf=selected_df\
    .withColumnRenamed("p","price")\
        .withColumnRenamed("s","symbol")\
            .withColumnRenamed("v","volume")\
                .withColumnRenamed("t","trade_timestamp")\
                    .withColumn("trade_timestamp",(col("trade_timestamp") / 1000).cast("timestamp"))\
                        .withColumn("trade_timestamp",from_utc_timestamp(col("trade_timestamp"),"UTC"))\
                         .withColumn("ingest_timestamp",current_timestamp())\
                             .withColumn("ingest_timestamp",from_utc_timestamp(col("ingest_timestamp"),"UTC"))
  
#display(renameDf)
        




'''
kafka_stream.writeStream \
    .format("json") \
    .option("checkpointLocation", "dbfs:/mnt/stocks/Checkpoint") \
    .start("dbfs:/mnt/stocks/")"""
'''

stockDF_Write = (
  renameDf.writeStream
    .format("mongodb") \
    .queryName("ToMDB2") \
    .option("checkpointLocation", "/tmp/pyspark7/")\
    .option("forceDeleteTempCheckpointLocation", "true")\
    .option('spark.mongodb.database', 'Finhub')\
    .option('spark.mongodb.collection', 'bitcoin3')\
    .option('spark.mongodb.connection.uri', 'mongodb+srv://Ahmed123:Ahmed786@cluster1.n6ct8hc.mongodb.net/')\
    .outputMode("append")\
    .start())






