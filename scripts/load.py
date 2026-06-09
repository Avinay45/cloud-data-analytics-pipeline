import pandas as pd

from app.database.db import SessionLocal

from app.database.models import (
    Customer,
    Product,
    Order
)

db = SessionLocal()

print("Database Connected")

customers_df = pd.read_csv(
    "data/processed/customers_clean.csv"
)

for _, row in customers_df.iterrows():

    customer = Customer(
        customer_id=int(row["customer_id"]),
        first_name=row["first_name"],
        last_name=row["last_name"],
        email=row["email"],
        city=row["city"]
    )

    db.add(customer)

db.commit()

print("Customers Loaded")

products_df = pd.read_csv(
    "data/processed/products_clean.csv"
)

for _, row in products_df.iterrows():

    product = Product(
        product_id=int(row["product_id"]),
        product_name=row["product_name"],
        category=row["category"],
        price=float(row["price"])
    )

    db.add(product)

db.commit()

print("Products Loaded")

orders_df = pd.read_csv(
    "data/processed/orders_transformed.csv"
)

for _, row in orders_df.iterrows():

    order = Order(

        order_id=int(row["order_id"]),

        customer_id=int(row["customer_id"]),

        product_id=int(row["product_id"]),

        quantity=int(row["quantity"]),

        total_amount=float(
            row["total_amount"]
        ),

        order_date=pd.to_datetime(
            row["order_date"]
        ),

        order_month=int(
            row["order_month"]
        ),

        order_year=int(
            row["order_year"]
        ),

        revenue_category=row[
            "revenue_category"
        ]
    )

    db.add(order)

db.commit()

print("Orders Loaded")

db.close()

print(
    "All Data Loaded Successfully"
)