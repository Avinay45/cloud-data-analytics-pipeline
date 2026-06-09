from fastapi import APIRouter

from app.analytics.products import (
    get_top_products
)

router = APIRouter()


@router.get("/top-products")
def top_products():

    data = get_top_products()

    return {
        "products": [
            {
                "product_name": row[0],
                "revenue": float(row[1])
            }
            for row in data
        ]
    }