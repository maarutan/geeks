# CRUD - CREATE, READ, UPDATE, DELETE
import sqlite3
from db import queries

db = sqlite3.connect("db/store.sqlite3")
cursor = db.cursor()


def sql_create():
    if db:
        print("База данных подключена!")
    cursor.execute(queries.CREATE_TABLE_STORE)
    cursor.execute(queries.CREATE_TABLE_STORE_DETAIL)
    db.commit()


def sql_insert_store(name_product, product_id, size, price, photo):
    cursor.execute(queries.INSERT_STORE, (name_product, product_id, size, price, photo))
    db.commit()


def sql_insert_store_detail(info_product, product_id, category):
    cursor.execute(
        queries.INSERT_STORE_DETAIL, (info_product, product_id, category)
    )  # Исправлено имя
    db.commit()


def get_db_connection():
    conn = sqlite3.connect("db/store.sqlite3")
    conn.row_factory = sqlite3.Row
    return conn


def fetch_all_products():
    conn = get_db_connection()
    products = conn.execute(
        """
        SELECT * FROM store s
        INNER JOIN store_detail sd ON s.product_id = sd.product_id
        """
    ).fetchall()  # Исправлено имя таблицы
    conn.close()
    return [dict(product) for product in products]  # Возвращаем список словарей


def delete_product(product_id):
    conn = get_db_connection()
    cursor = conn.execute("DELETE FROM store WHERE product_id = ?", (product_id,))
    conn.commit()
    conn.close()
    return cursor.rowcount > 0  # True, если удалён хотя бы один товар
