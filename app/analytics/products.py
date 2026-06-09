from sqlalchemy import text

from app.database.db import SessionLocal


def get_top_products():

    db = SessionLocal()

    query = text("""

        SELECT

            p.product_name,

            ROUND(
                SUM(o.total_amount)::numeric,
                2
            ) AS revenue

        FROM orders o

        JOIN products p

        ON o.product_id =
           p.product_id

        GROUP BY p.product_name

        ORDER BY revenue DESC

        LIMIT 10

    """)

    result = db.execute(query)

    data = result.fetchall()

    db.close()

    return data