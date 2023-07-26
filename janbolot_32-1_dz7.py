import sqlite3

conn = sqlite3.connect('hw.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    product_title TEXT NOT NULL,
                    price REAL NOT NULL DEFAULT 0.0,
                    quantity INTEGER NOT NULL DEFAULT 0)''')

def add_products():
    products = [
        ("Мыло", 50.99, 10),
        ("Шампунь", 120.5, 5),
        (" Зубная щетка", 75.0, 20),
        ("Зубная паста", 89.95, 15),
    ]
    cursor.executemany("INSERT INTO products (product_title, price, quantity) VALUES (?, ?, ?)", products)
    conn.commit()

def update_quantity(product_id, new_quantity):
    cursor.execute("UPDATE products SET quantity=? WHERE id=?", (new_quantity, product_id))
    conn.commit()

def update_price(product_id, new_price):
    cursor.execute("UPDATE products SET price=? WHERE id=?", (new_price, product_id))
    conn.commit()

def delete_product(product_id):
    cursor.execute("DELETE FROM products WHERE id=?", (product_id,))
    conn.commit()

def select_all_products():
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    for product in products:
        print(product)

def select_cheap_and_in_stock():
    cursor.execute("SELECT * FROM products WHERE price < 100.0 AND quantity > 5")
    products = cursor.fetchall()
    for product in products:
        print(product)

def search_products_by_title(keyword):
    cursor.execute("SELECT * FROM products WHERE product_title LIKE ?", ('%{}%'.format(keyword),))
    products = cursor.fetchall()
    for product in products:
        print(product)

add_products()
select_all_products()
update_quantity(1, 30)
update_price(2, 99.99)
delete_product(3)
select_cheap_and_in_stock()
search_products_by_title("мыло")

conn.close()