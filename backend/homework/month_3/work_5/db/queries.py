# queries.py
CREATE_TABLE_TABLE = """
CREATE TABLE IF NOT EXISTS store (
    id INTEGER PRIMARY KEY,
    name_product TEXT,
    product_id TEXT,
    size TEXT,
    price INTEGER,
    photo BLOB
);
"""

INSERT_STORE = """
INSERT INTO store (
    name_product,
    product_id,
    size,
    price,
    photo
)
VALUES (?, ?, ?, ?, ?);
"""

CREATE_TABLE_PRODUCTS_DETAILS = """
CREATE TABLE IF NOT EXISTS products_details (
    id INTEGER PRIMARY KEY,
    product_id TEXT,
    category TEXT,
    infoproduct TEXT
);
"""

INSERT_PRODUCTS_DETAILS = """
INSERT INTO products_details (
    product_id,
    category,
    infoproduct
)
VALUES (?, ?, ?);
"""

CREATE_TABLE_COLLECTION_PRODUCTS = """
CREATE TABLE IF NOT EXISTS collection_products (
    id INTEGER PRIMARY KEY,
    product_id TEXT,
    collection TEXT
);
"""

INSERT_COLLECTION_PRODUCTS = """
INSERT INTO collection_products (
    product_id,
    collection
)
VALUES (?, ?);
"""

CREATE_STAGES_TABLE = """
CREATE TABLE IF NOT EXISTS stages (
    id INTEGER PRIMARY KEY,
    product_id TEXT,
    stage_name TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
"""

INSERT_STAGE = """
INSERT INTO stages (
    product_id,
    stage_name
)
VALUES (?, ?);
"""

GET_STAGES_FOR_PRODUCT = """
SELECT stage_name, created_at
FROM stages
WHERE product_id = ?
ORDER BY created_at;
"""
