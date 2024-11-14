# dp_main.py
import sqlite3
from db import queries

db = sqlite3.connect("db/store.sqlite3")
cursor = db.cursor()


async def sql_create():
    if db:
        print("База данных подключена")
    cursor.execute(queries.CREATE_TABLE_TABLE)
