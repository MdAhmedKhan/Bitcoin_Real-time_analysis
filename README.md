# Bitcoin-Streaming-Data-Pipeline

This project is all about streaming data pipeline, focusing on gathering live Bitcoin prices, processing, storing, and visualizing them in real-time. This project is designed to showcase the capabilities of cloud technology, leveraging its strength to unlock the value of data for businesses, all without the hassle of managing infrastructure complexities. The key aspect of this project is to create a Data pipeline with **low latency, high scalability, and availability**.

# Architecture
![Bitcoin_Analysis](https://github.com/MdAhmedKhan/Bitcoin_Streaming-Data-Pipeline/assets/47691372/0e2c4155-edd7-4e69-b622-fa161fa747c9)

The diagram above displays the detailed architecture of the pipeline.
All the services used in this project are running on the **cloud** from start to finish.

**Data Ingestion layer**- A **Python** application called Finhub_Producer running on **Azure Databricks** connects to FInhub.io via **WebSocket** API. It retrieves live Bitcoin stock details (Price, Symbol, volume, and trade_timestmap) as **JSON** string messages, serialises the JSON, and publishes it to the **Kafka** broker using Kafka Producer.

**Message broker layer** – Messages from Finhub_Producer are received in the **Kafka** cluster by the Kafka broker, which is installed and running in an **AWS EC2** container. **Zookeeper** service is also available in EC2 for metadata management of the Kafka cluster.

**Stream Processing Layer** – **Azure Databricks** notebook containing a **Spark-Kafka** consumer application named Stream Processor is configured to connect to the Kafka broker to retrieve messages and serialize them into JSON objects. 

**Data Storage Layer** – **MongoDB Atlas** which is a multi-cloud database is set up to store and persist the real-time data coming from the Spark Databricks job. 

**Real-time Visualisation layer** – **Grafana Cloud** which is an intelligent tightly integrated visualization tool is configured to connect and query the MongoDB database from within the Grafana platform to retrieve the data and visualize the bitcoin stock price in real-time.

**CI/CD** – This project also uses Version control practice using **Azure DevOps** to provide Continuous Integration of code change in Databricks notebooks and Continuous deployment of code into the Testing, Pre-prod, and Production workspace of Databricks. The CI/CD pipeline is configured to automatically build the changes in case any code changes are pushed to the main branch which then can further be used for deployment to different environments. 


![Realtime_Dashboard](https://github.com/MdAhmedKhan/Bitcoin_Real-time_analysis/assets/47691372/a5b62539-3bb5-4ac0-a75e-300f07c7dc0e)






