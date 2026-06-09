import pandas as pd

customers = pd.read_csv(
    "data/raw/customers.csv"
)

products = pd.read_csv(
    "data/raw/products.csv"
)

orders = pd.read_csv(
    "data/raw/orders.csv"
)

# ------------------------
# Customers
# ------------------------

customers = customers.drop_duplicates()

customers = customers.dropna()

# ------------------------
# Products
# ------------------------

products = products.drop_duplicates()

products = products[
    products["price"] > 0
]

# ------------------------
# Orders
# ------------------------

orders = orders.drop_duplicates()

orders = orders[
    orders["quantity"] > 0
]

orders = orders[
    orders["total_amount"] > 0
]

# ------------------------
# Save
# ------------------------

customers.to_csv(
    "data/processed/customers_clean.csv",
    index=False
)

products.to_csv(
    "data/processed/products_clean.csv",
    index=False
)

orders.to_csv(
    "data/processed/orders_clean.csv",
    index=False
)

print("Validation Completed")