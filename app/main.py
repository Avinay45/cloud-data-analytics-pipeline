from fastapi import FastAPI

from app.api.revenue import router as revenue_router
from app.api.products import router as products_router
from app.api.customers import router as customers_router
from app.api.dashboard import router as dashboard_router

app = FastAPI(
    title="Cloud Data Analytics Pipeline",
    version="1.0.0"
)

app.include_router(revenue_router)
app.include_router(products_router)
app.include_router(customers_router)
app.include_router(dashboard_router)


@app.get("/")
def root():

    return {
        "message":
        "Cloud Analytics API Running"
    }