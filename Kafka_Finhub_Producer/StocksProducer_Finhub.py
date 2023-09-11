# Databricks notebook source
pip install websocket


# COMMAND ----------

pip install websocket-client

# COMMAND ----------

pip install kafka-python

# COMMAND ----------

import websocket
import json
import time
from kafka import KafkaProducer
from time import sleep
from json import dumps
from pyspark.sql.types import StructType, StructField,StringType, DateType,DoubleType,LongType,TimestampType, IntegerType, ArrayType, NullType

producer = KafkaProducer(bootstrap_servers=['ec2-3-22-66-169.us-east-2.compute.amazonaws.com:9092'],
                        value_serializer=lambda x: dumps(x,default=str).encode('utf-8'))


def on_message(ws, message):
    json_object = json.loads(message)
    
    producer.send('Finhub1',value=json_object)
    print("done")

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    #ws.send('{"type":"subscribe","symbol":"MSFT"}')
    #ws.send('{"type":"subscribe","symbol":"AMZN"}')
    ws.send('{"type":"subscribe","symbol":"BINANCE:BTCUSDT"}')
    #ws.send('{"type":"subscribe","symbol":"IC MARKETS:1"}')

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://ws.finnhub.io?token=cji3ijpr01qonds7j5l0cji3ijpr01qonds7j5lg",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    time.sleep(5)
    ws.run_forever()
