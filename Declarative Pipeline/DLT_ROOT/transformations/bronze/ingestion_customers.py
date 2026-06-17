import dlt

# Customer expectations
customers_rules={
    "rule_1":"customer_id IS NOT NULL",
    "rule_2":"customer_name IS NOT NULL"
}

@dlt.expect_all_or_drop(customers_rules)
@dlt.table(
    name="customers_stg"
)
def cutomers_stg():
    df = spark.readStream.table("rjrohan.source.customers")
    return df
