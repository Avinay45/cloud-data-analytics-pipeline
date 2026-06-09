from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import DateTime
from sqlalchemy.sql import func

from app.database.db import Base


class Customer(Base):

    __tablename__ = "customers"

    customer_id = Column(
        Integer,
        primary_key=True,
        autoincrement=False
    )

    first_name = Column(String)

    last_name = Column(String)

    email = Column(
        String,
        unique=True
    )

    city = Column(String)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )


class Product(Base):

    __tablename__ = "products"

    product_id = Column(
        Integer,
        primary_key=True,
        autoincrement=False
    )

    product_name = Column(String)

    category = Column(String)

    price = Column(Float)


class Order(Base):

    __tablename__ = "orders"

    order_id = Column(
        Integer,
        primary_key=True,
        autoincrement=False
    )

    customer_id = Column(Integer)

    product_id = Column(Integer)

    quantity = Column(Integer)

    total_amount = Column(Float)

    order_date = Column(DateTime)

    order_month = Column(Integer)

    order_year = Column(Integer)

    revenue_category = Column(String)