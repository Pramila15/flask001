import sqlite3

conn = sqlite3.connect('database.db')
print("opened database successfully")

conn.execute('CREATE TABLE products (behavior TEXT, trend TEXT, product_name TEXT, business_purpose TEXT, short_des TEXT, long_des TEXT, function TEXT, strategy TEXT, business_impact TEXT, enterprise_value TEXT, feature_attribute TEXT, report_embed_code TEXT)')
print("table created successfully")

conn.close()