import pandas as pd
import random
from faker import Faker

fake = Faker()

NUM_CUSTOMERS = 1000
NUM_PRODUCTS = 200
NUM_ORDERS = 50000

# -------------------
# Customers
# -------------------

customers = []

for customer_id in range(1, NUM_CUSTOMERS + 1):

    customers.append({
        "customer_id": customer_id,
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.unique.email(),
        "city": fake.city()
    })

customers_df = pd.DataFrame(customers)

# -------------------
# Products
# -------------------

categories = [
    "Electronics",
    "Clothing",
    "Books",
    "Home",
    "Sports"
]

products = []

for product_id in range(1, NUM_PRODUCTS + 1):

    products.append({
        "product_id": product_id,
        "product_name": fake.word().title(),
        "category": random.choice(categories),
        "price": round(random.uniform(10, 1000), 2)
    })

products_df = pd.DataFrame(products)

# -------------------
# Orders
# -------------------

orders = []

for order_id in range(1, NUM_ORDERS + 1):

    product_price = products_df.sample(1).iloc[0]["price"]

    quantity = random.randint(1, 5)

    orders.append({
        "order_id": order_id,
        "customer_id": random.randint(1, NUM_CUSTOMERS),
        "product_id": random.randint(1, NUM_PRODUCTS),
        "quantity": quantity,
        "total_amount": round(product_price * quantity, 2)
    })

orders_df = pd.DataFrame(orders)

# -------------------
# Save Files
# -------------------

customers_df.to_csv(
    "data/raw/customers.csv",
    index=False
)

products_df.to_csv(
    "data/raw/products.csv",
    index=False
)

orders_df.to_csv(
    "data/raw/orders.csv",
    index=False
)

print("Data Generated Successfully")