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









if __name__ == "__main__":
    init_dp()
    create_tables()
