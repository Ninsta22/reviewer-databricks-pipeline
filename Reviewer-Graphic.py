# Databricks notebook source
import pandas as pd
import numpy as np
from pyspark.sql import SparkSession

# COMMAND ----------

spark = SparkSession.builder.appName("Steam").getOrCreate()
spark_df = spark.read.table("hive_metastore.default.steam_reviews_spark")

# COMMAND ----------

pd_df = spark_df.toPandas()

# COMMAND ----------

pd_df

# COMMAND ----------

pd_df["weighted_vote_score"] = pd_df["weighted_vote_score"].astype(float)
pd_df = pd_df[pd_df["weighted_vote_score"] > 0]
pd_df = pd_df[pd_df["comment_count"] > 0]
pd_df

# COMMAND ----------

import seaborn as sns

plot = sns.scatterplot(x=pd_df["weighted_vote_score"], y=pd_df["comment_count"])
plot.set_title("Weighted Vote Score vs Review Comment Count")
plot.set_xlabel("Weighted Vote Score")
plot.set_ylabel("Comments Left under Review")

# COMMAND ----------


