# queries.py
CREATE_TABLE_TABLE = """
CREATE TABLE IF NOT EXISTS store (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_product TEXT,
    product_id TEXT,
    size TEXT,
    price TEXT,
    photo
)
"""

INSERT_STORE = """
    INSERT INTO store (name_product, product_id, size, price, photo)
    VALUES (?, ?, ?, ?, ?)
"""


# queries.py
CREATE_TABLE_TABLE_DETAIL = """
CREATE TABLE IF NOT EXISTS store_detail (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    info_product TEXT,
    product_id TEXT,
    category TEXT
)
"""

INSERT_STORE_DETAIL = """
    INSERT INTO store_detail (info_product, product_id, category)
    VALUES (?, ?, ?)
"""