import sqlite3
conn=sqlite3.connect("amazon.db")
cursor=conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    city TEXT,
    join_date TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    category TEXT,
    price REAL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    order_date TEXT,
    total_amount REAL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS order_items (
    order_item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    subtotal REAL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
)
""")

customers = [
    ('Ali Ahmad', 'ali@gmail.com', 'Lahore', '2024-01-10'),
    ('Burhan Smith', 'burhan@gmail.com', 'Karachi', '2024-02-14'),
    ('Danish Huza', 'danish@yahoo.com', 'Islamabad', '2024-03-01'),
    ('Ehsan Khan', 'ehsan@yahoo.com', 'Lahore', '2024-04-20'),
    ('Fiona Gallagher', 'fiona@gmail.com', 'Karachi', '2024-05-12'),
    ('Ghias Uddin', 'ghias@gmail.com', 'Peshawar', '2024-05-28'),
    ('Hania Amir', 'hania@yahoo.com', 'Islamabad', '2024-06-02'),
    ('Imran Khan', 'imran@gmail.com', 'Lahore', '2024-06-15'),
    ('Junaid Jamshed', 'junaid@gmail.com', 'Karachi', '2024-07-01'),
    ('Kashif Asif', 'kashif@yahoo.com', 'Multan', '2024-07-20')
]
cursor.executemany("INSERT INTO customers (name, email, city, join_date) VALUES (?, ?, ?, ?)", customers)

products = [
    ('Wireless Mouse', 'Electronics', 25.99),
    ('Laptop Sleeve', 'Accessories', 15.49),
    ('Bluetooth Headphones', 'Electronics', 45.99),
    ('Water Bottle', 'Home & Kitchen', 12.00),
    ('Notebook', 'Stationery', 3.50),
    ('Mechanical Keyboard', 'Electronics', 89.99),
    ('Gaming Chair', 'Furniture', 199.99),
    ('Desk Lamp', 'Home & Kitchen', 29.99),
    ('Coffee Mug', 'Home & Kitchen', 8.50),
    ('Gel Pens Set', 'Stationery', 5.00)
]
cursor.executemany("INSERT INTO products (name, category, price) VALUES (?, ?, ?)", products)

orders = [
    (1, '2024-05-05', 97.97),
    (2, '2024-05-07', 15.49),
    (3, '2024-06-02', 245.98),
    (1, '2024-06-10', 12.00),
    (4, '2024-06-12', 89.99),
    (5, '2024-06-15', 38.49),
    (6, '2024-06-20', 199.99),
    (7, '2024-07-02', 33.49),
    (8, '2024-07-05', 54.49),
    (9, '2024-07-11', 115.98),
    (10, '2024-07-15', 5.00),
    (2, '2024-07-18', 45.99)
]
cursor.executemany("INSERT INTO orders (customer_id, order_date, total_amount) VALUES (?, ?, ?)", orders)

order_items = [
    (1, 1, 2, 51.98), (1, 3, 1, 45.99), 
    (2, 2, 1, 15.49),                    
    (3, 3, 1, 45.99), (3, 7, 1, 199.99),
    (4, 4, 1, 12.00),              
    (5, 6, 1, 89.99),                    
    (6, 2, 1, 15.49), (6, 8, 1, 29.99),  
    (7, 7, 1, 199.99),                 
    (8, 5, 1, 3.50),  (8, 8, 1, 29.99),  
    (9, 1, 1, 25.99), (9, 9, 1, 8.50),   
    (10, 6, 1, 89.99), (10, 1, 1, 25.99),
    (11, 10, 1, 5.00),                  
    (12, 3, 1, 45.99)                  
]
cursor.executemany("INSERT INTO order_items (order_id, product_id, quantity, subtotal) VALUES (?, ?, ?, ?)", order_items)
conn.commit()
conn.close()
print("DataBase Created Succesfully!")