# Databricks notebook source
import pandas as pd
import numpy as np
from pyspark.sql import SparkSession

# COMMAND ----------

spark = SparkSession.builder.appName("Steam").getOrCreate()
raw_df = spark.read.table("hive_metastore.default.raw_steam_reviews")

# COMMAND ----------

edited_df = raw_df.select("language", "review", "voted_up", "votes_up", "votes_funny","weighted_vote_score", "comment_count")

# COMMAND ----------

edited_df.show()

# COMMAND ----------

edited_df.write.mode("overwrite").option("overwriteSchema", "true").saveAsTable("steam_reviews_spark")

# COMMAND ----------


