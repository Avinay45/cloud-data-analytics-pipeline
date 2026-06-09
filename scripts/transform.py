import pandas as pd
import random

orders = pd.read_csv(
    "data/processed/orders_clean.csv"
)

# -------------------------
# Generate Order Date
# -------------------------

orders["order_date"] = pd.to_datetime(
    pd.date_range(
        start="2024-01-01",
        periods=len(orders),
        freq="h"
    )
)

# -------------------------
# Month
# -------------------------

orders["order_month"] = (
    orders["order_date"]
    .dt.month
)

# -------------------------
# Year
# -------------------------

orders["order_year"] = (
    orders["order_date"]
    .dt.year
)

# -------------------------
# Revenue Category
# -------------------------

def revenue_category(amount):

    if amount < 200:
        return "Low"

    elif amount < 1000:
        return "Medium"

    else:
        return "High"

orders["revenue_category"] = (
    orders["total_amount"]
    .apply(revenue_category)
)

# -------------------------
# Save
# -------------------------

orders.to_csv(
    "data/processed/orders_transformed.csv",
    index=False
)

print("Transformation Completed")