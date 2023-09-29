# Bitcoin-Streaming-Data-Pipeline

This project is all about streaming data pipeline, focusing on gathering live Bitcoin prices, processing, storing, and visualizing them in real-time. This project is designed to showcase the capabilities of cloud technology, leveraging its strength to unlock the value of data for businesses, all without the hassle of managing infrastructure complexities. The key aspect of this project is to create a Data pipeline with low latency, high scalability, and availabilit.

# Architecture
![Bitcoin_Analysis](https://github.com/MdAhmedKhan/Bitcoin_Streaming-Data-Pipeline/assets/47691372/0e2c4155-edd7-4e69-b622-fa161fa747c9)

The diagram above displays the detailed architecture of the pipeline.
All the services used in this project are running on the **cloud** from start to finish.

**Data Ingestion layer**- A **Python** application called Finhub_Producer running on **Azure Databricks** connects to FInhub.io via **WebSocket** API. It retrieves live Bitcoin stock details (Price, Symbol, volume, and trade_timestmap) as **JSON** string messages, serialises the JSON, and publishes it to the **Kafka** broker using Kafka Producer.

**Message broker layer** – Messages from Finhub_Producer are received in the **Kafka** cluster by the Kafka broker, which is installed and running in an **AWS EC2** container. **Zookeeper** service is also available in EC2 for metadata management of the Kafka cluster.

**Stream Processing Layer** – **Azure Databricks** notebook containing a **Spark-Kafka** consumer application named Stream Processor is configured to connect to the Kafka broker to retrieve messages and serialize them into JSON objects. 

![Realtime_Dashboard](https://github.com/MdAhmedKhan/Bitcoin_Real-time_analysis/assets/47691372/a5b62539-3bb5-4ac0-a75e-300f07c7dc0e)






