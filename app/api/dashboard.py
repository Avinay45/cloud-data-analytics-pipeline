from fastapi import APIRouter

from app.analytics.revenue import (
    get_total_revenue
)

from app.analytics.products import (
    get_top_products
)

from app.analytics.customers import (
    get_top_customers
)

router = APIRouter()


@router.get("/dashboard")
def dashboard():

    return {

        "total_revenue":
            get_total_revenue(),

        "top_products":
            len(get_top_products()),

        "top_customers":
            len(get_top_customers())
    }