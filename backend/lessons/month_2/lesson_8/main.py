import sqlite3 as sql

with sql.connect("base.db") as con:
    cursor = con.cursor()

    cursor.execute(
        """
    CREATE TABLE IF NO EXISTS gamers(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
    )
                   """
    )
