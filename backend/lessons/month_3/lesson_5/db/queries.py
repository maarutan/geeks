# queries.py

# В db_main.py


CREATE_TABLE_TABLE = """
CREATE TABLE IF NOT EXISTS store (
    id INTEGER PRIMARY KEY,
    name_product TEXT,
    product_id TEXT,
    size TEXT,
    price INTEGER,
    photo BLOB
)
"""

INSERT_STORE = """
    INSERT INTO STORE (name_product, product_id, size, price, photo)
    values (?, ?, ?, ?, ?)
"""
