CREATE_TABLE = """
CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    category TEXT,
    size TEXT,
    articul INTEGER,
    photo
)
"""
INSERT_TABLE = """
INSERT INTO
products
    (name, category, size, articul, photo)
        VALUES
            (?, ?, ?, ?, ?)
                            """
