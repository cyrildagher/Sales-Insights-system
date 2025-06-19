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


query = '''
    SELECT
        DATE_FORMAT(sale_date, '%Y-%m') AS month,
        SUM(quantity * price) AS total_revenue
    FROM sales_data
    GROUP BY month
    ORDER BY month;
'''

df = pd.read_sql(query, conn)
print("\n📅 Monthly Sales Trend:")
print(df.to_string(index=False))
conn.close()
