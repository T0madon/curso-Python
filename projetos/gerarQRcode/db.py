import sqlite3

def initialize_db():
    conn = sqlite3.connect("sales_app.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        quantity INTEGER NOT NULL
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tickets (
        id INTEGER PRIMARY KEY,
        product_id INTEGER NOT NULL,
        validated INTEGER DEFAULT 0,
        FOREIGN KEY (product_id) REFERENCES products (id)
    )
    """)
    conn.commit()
    conn.close()

def add_product(name, quantity):
    conn = sqlite3.connect("sales_app.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (name, quantity) VALUES (?, ?)", (name, quantity))
    conn.commit()
    conn.close()

def get_products():
    conn = sqlite3.connect("sales_app.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE quantity > 0")
    products = cursor.fetchall()
    conn.close()
    return products

def validate_ticket(ticket_id):
    conn = sqlite3.connect("sales_app.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE tickets SET validated = 1 WHERE id = ?", (ticket_id,))
    cursor.execute("""
    UPDATE products 
    SET quantity = quantity - 1 
    WHERE id = (SELECT product_id FROM tickets WHERE id = ?)
    """, (ticket_id,))
    conn.commit()
    conn.close()