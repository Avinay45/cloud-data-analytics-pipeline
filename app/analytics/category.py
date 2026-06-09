from sqlalchemy import text

from app.database.db import SessionLocal


def revenue_by_category():

    db = SessionLocal()

    query = text("""

        SELECT

            revenue_category,

            COUNT(*) AS orders

        FROM orders

        GROUP BY revenue_category

        ORDER BY orders DESC

    """)

    result = db.execute(query)

    data = result.fetchall()

    db.close()

    return data