import pandas as pd
import numpy as np

data = pd.read_excel("Online reatil.xlsx")

data = data.dropna(subset=["CustomerID"])
data = data[data["Quantity"] > 0]

data["InvoiceDate"] = pd.to_datetime(data["InvoiceDate"])

#customers table
customers = data["CustomerId", "Country"].drop_duplicates
customers.columns = ["customer_id", "country"]

customers.to_csv(
    "../data/processed/customers.csv",
    index=False
)

#products table
products = data["StockCode", "Description", "UnitPrice"].drop_duplicates
products = products.reset_index(drop=True)
products["product_id"] = products.index+1
products = products[
    ["product_id", "StockCode", "Description", "UnitPrice"]
]
products.columns = ["product_id", "stock_code", "description", "unit_price"]

products.to_csv(
    "../data/processed/products.csv",
    index=False
)

#orders table
orders = data["InvoiceNo", "CustomerID", "InvoiceDate"].drop_duplicates
orders.columns = ["order_id", "customer_id", "order_date"]

orders.to_csv(
    "../data/processed/orders.csv",
    index=False
)

#order items table
items = data["InvoiceNo", "StockCode", "Quantity"].drop_duplicates
items.columns = ["order_id", "stock_code", "quantity"]

items.to_csv(
    "../data/processed/order_items.csv",
    index=False
)

print()
