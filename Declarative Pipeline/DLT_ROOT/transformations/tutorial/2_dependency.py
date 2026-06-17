# import dlt
# from pyspark.sql.functions import *

# # Creating an End-to-End basic pipeline

# # Staging area

# @dlt.table

# def staging_orders():
#     df=spark.readStream.table("rjrohan.source.orders")
#     return df

# # Transformation

# @dlt.view

# def transformed_orders():
#     df=spark.readStream.table("staging_orders")
#     df=df.withColumn("order_status",lower(col('order_status')))
#     return df

# # Create Aggregated area

# @dlt.table

# def agg_orders():
#     df=spark.readStream.table("transformed_orders")
#     df=df.groupBy("order_status").count()
#     return df




