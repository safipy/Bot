import sqlite3
from pathlib import Path


def init_dp():
    global db, cursor
    DB_NAME = 'db.sqlite'
    MAIN_PATH = Path(__file__).parent.parent
    db = sqlite3.connect(MAIN_PATH / DB_NAME)
    cursor = db.cursor()


def create_tables():
    cursor.execute("""CREATE TABLE IF NOT EXISTS products(
        id INTEGER PRIMARY KEY, 
        name TEXT, 
        description TEXT,
        price INTEGER.
        photo TEXT
    )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS orders(
        id INTEGER PRIMARY KEY,
        username TEXT,
        address TEXT,
        product_id INTEGER
          REFERENCES products(id)
          ON DELETE CASCADE
    )
    """)

    db.commit()

def add_products():
    cursor.execute("""INSERT INTO products(name, description, price, photo) VALUES 
    ('Parfume-1', 'BYREDO - BLANCE', 2000, '/photo/jer.jpeg')
    ('Parfume-2', 'TOM FORD- LOST CHERY', 3000, '/photo/jer.jpeg')
    ('Parfume-3', 'BYREDO - GYPSY WATER', 2500, '/photo/jer.jpeg')
    ('Parfume-4', 'BYREDO - ROSE DAMALFI', 3500, '/photo/jer.jpeg')
    """)

    db.commit()

def delete_table_products():
    cursor.execute("""DROP TABLE IF EXISTS products""")
    db.commit()

def get_products():
    cursor.execute("""SELECT * FROM products""")
    all_products = cursor.fetchall()
    print(all_products)

    return all_products




def save_order(data):
    print(data.as_dict())
    data = data.as_dict()
    cursor.execute("""INSERT INTO orders (username, adress, product_id)
    VALUES (:username, :adress, :product_id)
    """, {'username': data['name'],
          'adress': data['adress'],
          'product_id': data['product_id']}
    )
    db.commit()



if __name__ == "__main__":
    init_dp()
    create_tables()
    add_products()
    delete_table_products()
    get_products()
    save_order()
    