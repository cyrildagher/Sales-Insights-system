import pymysql 
import os 
from dotenv import load_dotenv 
import pandas as pd 

load_dotenv() 

conn = pymysql.connect(
    host=os.getenv('DB_HOST'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    port=int(os.getenv('DB_PORT')),
    database=os.getenv('DB_NAME')
)


#query: top 5 products by total revenue 
query = '''
    SELECT product_name, SUM(quantity * price) AS total_revenue
    FROM sales_data 
    GROUP BY product_name 
    ORDER BY total_revenue DESC 
    LIMIT 5; 
'''

df = pd.read_sql(query, conn)

print ("\n 🔥 Top 5 Best-Selling Products by Revenue")
print(df.to_string(index=False))
conn.close()