import sqlite3 as sq
from db import queries

db = sq.connect("./db/store.sqlite3")
cursor = db.cursor()


async def sql_create():
    if db:
        print("База данных подключена")
    cursor.execute(queries.CREATE_TABLE_TABLE)


async def insert_store(name_product, size, price, photo):
    cursor.execute(
        queries.INSERT_STORE,
        (name_product, size, price, photo),
    )
    await db.commit()
