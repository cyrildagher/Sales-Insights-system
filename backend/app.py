from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import pymysql
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

app = FastAPI()

# CORS middleware setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development only! Use specific origins in production.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db_connection():
    return pymysql.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        port=int(os.getenv('DB_PORT')),
        database=os.getenv('DB_NAME')
    )

@app.get("/api/monthly-sales")
def monthly_sales(product: str = Query(None)):
    conn = get_db_connection()
    if product:
        query = '''
            SELECT
                DATE_FORMAT(sale_date, '%%Y-%%m') AS month,
                SUM(quantity * price) AS total_revenue
            FROM sales_data
            WHERE product_name = %s
            GROUP BY month
            ORDER BY month;
        '''
        df = pd.read_sql(query, conn, params=[product])
    else:
        query = '''
            SELECT
                DATE_FORMAT(sale_date, '%%Y-%%m') AS month,
                SUM(quantity * price) AS total_revenue
            FROM sales_data
            GROUP BY month
            ORDER BY month;
        '''
        df = pd.read_sql(query, conn)
    conn.close()
    return df.to_dict(orient="records")

@app.get("/api/top-products")
def top_products():
    conn = get_db_connection()
    query = '''
        SELECT product_name, SUM(quantity * price) AS total_revenue
        FROM sales_data
        GROUP BY product_name
        ORDER BY total_revenue DESC
        LIMIT 5;
    '''
    df = pd.read_sql(query, conn)
    conn.close()
    return df.to_dict(orient="records")

@app.get("/api/sales-by-region")
def sales_by_region(product: str = Query(None)):
    conn = get_db_connection()
    if product:
        query = '''
            SELECT region, SUM(quantity * price) AS total_revenue
            FROM sales_data
            WHERE product_name = %s
            GROUP BY region
            ORDER BY total_revenue DESC;
        '''
        df = pd.read_sql(query, conn, params=[product])
    else:
        query = '''
            SELECT region, SUM(quantity * price) AS total_revenue
            FROM sales_data
            GROUP BY region
            ORDER BY total_revenue DESC;
        '''
        df = pd.read_sql(query, conn)
    conn.close()
    return df.to_dict(orient="records")
