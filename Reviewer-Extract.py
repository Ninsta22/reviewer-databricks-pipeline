# Databricks notebook source
import pandas as pd
import numpy as np
import json
from pyspark.sql import SparkSession

# COMMAND ----------

list_data = []

with open("game_id.txt", 'r') as file:
    for line in file:
        file_path = f"10_json_files/review_{line.strip()}.json"
        
        with open(file_path, "r") as file:
            data = json.load(file)
            list_data.append(data)

# COMMAND ----------

df_list = []

for data in list_data:
    reviews = data.get("reviews", {})
    
    for key, value in reviews.items():
        df_list.append(pd.json_normalize(value))


review_df = pd.concat(df_list, ignore_index=True)

# COMMAND ----------

review_df

# COMMAND ----------

spark = SparkSession.builder.appName("Steam").getOrCreate()

# COMMAND ----------

spark_df = spark.createDataFrame(review_df)

# COMMAND ----------

spark_df.write.mode("overwrite").saveAsTable("raw_steam_reviews")

# COMMAND ----------


