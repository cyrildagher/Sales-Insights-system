import pymysql 
import os 
from dotenv import load_dotenv
import pandas as pd 

load_dotenv

conn = pymysql.connect(
    host = os.getenv('DB_HOST'), 
    user = os.getenv('DB_USER'), 
    password = os.getenv('DB_PASSWORD'),
    port = os.getenv('DB_PORT'),
    database = os.getenv('DB_NAME')
)

query = '''
    SELECT region , SUM (quantity * price) AS total_revenue 
    FROM sales_data 
    GROUP BY region 
    GROUP BY total_revenue DESC; 
'''

df = pd.read_sql(query, conn)
print ("\n🌍 Total Sales by Region: ")
print(df.to_string(index=False))
conn.close()