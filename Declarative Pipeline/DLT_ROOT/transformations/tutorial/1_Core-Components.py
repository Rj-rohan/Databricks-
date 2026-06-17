# import dlt

# # Creating Streaming table

# @dlt.table

# def stream_table():
#     df=spark.readStream.table("rjrohan.source.orders")
#     return df

# # Creating Materialized View

# @dlt.table

# def mat_view():
#     df=spark.read.table("rjrohan.source.orders")
#     return df

# # Creating View

# #1) Batch View

# @dlt.view

# def batch_view():
#     df=spark.read.table("rjrohan.source.orders")
#     return df

# #2) Streaming View

# @dlt.view

# def stream_view():
#     df=spark.readStream.table("rjrohan.source.orders")
#     return df


 