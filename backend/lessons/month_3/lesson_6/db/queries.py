CREATE_TABLE_TABLE = """
CREATE TABLE IF NOT EXISTS store (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_product TEXT NOT NULL,
    size TEXT NOT NULL,
    price REAL NOT NULL,
    photo TEXT NOT NULL
);
"""

INSERT_STORE = """
INSERT INTO store
    (name_product, size, price, photo)
    VALUES (?, ?, ?, ?);
"""
