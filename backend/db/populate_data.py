from dotenv import load_dotenv
import os 
import random 
from datetime import datetime , timedelta
import pymysql 


#DB connection settings 

load_dotenv()
conn = pymysql.connect(
    host=os.getenv('DB_HOST'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    port=int(os.getenv('DB_PORT')),
    database=os.getenv('DB_NAME')
)
cursor = conn.cursor() 

#sample data pools 
products = ['Soap', 'Shampoo', 'Toothpaste', 'Lotion', 'Detergent']
regions = ['Accra', 'Kumasi', 'Takoradi', 'Tamale']
start_date = datetime(2023, 1, 1)

# Ensure each product has a top region
for idx, product in enumerate(products):
    # Assign a unique region to be the "top" for this product
    top_region = regions[idx % len(regions)]
    # Insert a high-quantity sale for this product-region
    cursor.execute('''
        INSERT INTO sales_data (product_name, region, quantity, price, sale_date)
        VALUES (%s, %s, %s, %s, %s)
    ''', (product, top_region, 200, round(random.uniform(10.0, 20.0), 2), start_date.date()))

# Add additional random sales for realism
for i in range(100):
    product = random.choice(products)
    region = random.choice(regions)
    quantity = random.randint(1, 20)
    price = round(random.uniform(5.0, 20.0), 2)
    sale_date = start_date + timedelta(days=random.randint(0, 364))

    cursor.execute('''
        INSERT INTO sales_data (product_name, region, quantity, price, sale_date)
        VALUES (%s, %s, %s, %s, %s)
    ''', (product, region, quantity, price, sale_date.date()))
    
conn.commit()
conn.close()