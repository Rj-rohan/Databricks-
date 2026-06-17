import dlt

# Products expectations
product_rules={
    "rule_1":"product_id IS NOT NULL",
    "rule_2":"price>=0"
}

@dlt.expect_all(product_rules)
@dlt.table(
    name="products_stg"
)
def products_stg():
    df = spark.readStream.table("rjrohan.source.products")
    return df




