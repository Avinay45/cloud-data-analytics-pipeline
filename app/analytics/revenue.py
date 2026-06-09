from sqlalchemy import text

from app.database.db import SessionLocal


def get_total_revenue():

    db = SessionLocal()

    query = text("""

        SELECT
            ROUND(
                SUM(total_amount)::numeric,
                2
            ) AS revenue
        FROM orders

    """)

    result = db.execute(query)

    revenue = result.fetchone()[0]

    db.close()

    return revenue

def get_monthly_revenue():

    db = SessionLocal()

    query = text("""

        SELECT

            order_month,

            ROUND(
                SUM(total_amount)::numeric,
                2
            ) AS revenue

        FROM orders

        GROUP BY order_month

        ORDER BY order_month

    """)

    result = db.execute(query)

    data = result.fetchall()

    db.close()

    return data