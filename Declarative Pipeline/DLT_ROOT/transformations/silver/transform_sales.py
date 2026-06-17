import dlt

# Creating a destination silver table

dlt.create_table(
    name="silver_enr"
)

dlt.create_auto_cdc_flow