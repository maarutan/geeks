import sqlite3 as sq
from . import queries

db = sq.connect("./db/data.db")
cursor = db.cursor()


async def sql_create(*args):
    if db:
        print("База данных подключена")
    cursor.execute(queries.CREATE_TABLE)
    db.commit()


async def insert_store(name, category, size, articul, photo):
    cursor.execute(
        queries.INSERT_TABLE,
        (name, category, size, articul, photo),
    )
    db.commit()
