import pandas as pd
from tabulate import tabulate

inventory = pd.read_csv("Columns_pandas/inventory.csv")

#First 10 rows of inventory DataFrame
staten_island = inventory.head(10)

#Selecting column product_description from staten_island
product_request = staten_island["product_description"]

#Selecting columns where location is brooklyn and product type is seeds
seed_request = inventory[(inventory["location"] == "Brooklyn") & (inventory["product_type"] == "seeds")]

#Adding a column to inventory called in_stock
inventory["in_stock"] = inventory.apply(lambda row: \
  True if row["quantity"] > 0 \
  else False,
  axis=1
)

inventory["total_value"] = inventory["price"] * inventory["quantity"]

combine_lambda = lambda row: \
    '{} - {}'.format(row.product_type,
                     row.product_description)

inventory["full_description"] = inventory.apply(combine_lambda, axis=1)

print(tabulate(inventory, headers="keys", tablefmt="grid"))
