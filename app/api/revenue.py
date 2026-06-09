from fastapi import APIRouter

from app.analytics.revenue import (
    get_total_revenue,
    get_monthly_revenue
)

router = APIRouter()


@router.get("/revenue")
def total_revenue():

    return {
        "total_revenue":
        get_total_revenue()
    }


@router.get("/monthly-revenue")
def monthly_revenue():

    data = get_monthly_revenue()

    return {
        "monthly_revenue": [
            {
                "month": row[0],
                "revenue": float(row[1])
            }
            for row in data
        ]
    }