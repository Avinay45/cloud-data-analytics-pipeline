from fastapi import APIRouter

from app.analytics.customers import (
    get_top_customers
)

router = APIRouter()


@router.get("/top-customers")
def top_customers():

    data = get_top_customers()

    return {
        "customers": [
            {
                "first_name": row[0],
                "last_name": row[1],
                "revenue": float(row[2])
            }
            for row in data
        ]
    }