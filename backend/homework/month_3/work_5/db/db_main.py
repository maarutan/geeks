# db_main.py
import sqlite3
from db import queries
import os

if os.path.exists("db/store.sqlite3"):
    os.remove("db/store.sqlite3")
    print("Старая база данных удалена.")
else:
    print("База данных не найдена.")

db = sqlite3.connect("db/store.sqlite3")
cursor = db.cursor()


def sql_create():
    print("База данных подключена!")
    cursor.execute(queries.CREATE_TABLE_TABLE)
    cursor.execute(queries.CREATE_TABLE_PRODUCTS_DETAILS)
    cursor.execute(queries.CREATE_TABLE_COLLECTION_PRODUCTS)
    db.commit()


def sql_insert_store(name_product, product_id, size, price, photo):
    cursor.execute(queries.INSERT_STORE, (name_product, product_id, size, price, photo))
    db.commit()


def sql_insert_products_details(product_id, category, infoproduct):
    cursor.execute(queries.INSERT_PRODUCTS_DETAILS, (product_id, category, infoproduct))
    db.commit()


def sql_insert_collection_products(product_id, collection):
    cursor.execute(queries.INSERT_COLLECTION_PRODUCTS, (product_id, collection))
    db.commit()
