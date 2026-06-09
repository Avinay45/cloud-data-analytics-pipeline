from sqlalchemy import text

from app.database.db import SessionLocal


def get_top_customers():

    db = SessionLocal()

    query = text("""

        SELECT

            c.first_name,

            c.last_name,

            ROUND(
                SUM(o.total_amount)::numeric,
                2
            ) AS revenue

        FROM orders o

        JOIN customers c

        ON o.customer_id =
           c.customer_id

        GROUP BY

            c.first_name,
            c.last_name

        ORDER BY revenue DESC

        LIMIT 10

    """)

    result = db.execute(query)

    data = result.fetchall()

    db.close()

    return data