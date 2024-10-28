import sqlite3 as sql
import os

if os.path.exists("base.db"):
    os.remove("base.db")

with sql.connect("base.db") as c:
    cursor = c.cursor()

    cursor.execute(
        """ 
        CREATE TABLE IF NOT EXISTS gamers(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        ) """
    )

    cursor.execute(
        """
        INSERT INTO gamers(name)
            VALUES        
                ('marat'),
                ('taram'),
                ('kamila')
        """
    )

    cursor.execute(
        """ 
        CREATE TABLE IF NOT EXISTS games(
            gameId INTEGER PRIMARY KEY AUTOINCREMENT,
            score INTEGER NOT NULL,
            userId INTEGER,
            FOREIGN KEY(userId) REFERENCES gamers(id)
        )"""
        # one to one - один к одному
    )

    cursor.execute(""" SELECT * FROM gamers """)
    for row in cursor:
        print(row)

    cursor.execute(
        """
        INSERT INTO games(score, userId)
            VALUES
                (100,1),
                (150,1),
                (100,1),
                (100,1),
                (100,1),
                (200,2),
                (300,3)
        """
    )

    cursor.execute(""" SELECT * FROM games""")
    print()
    for row in cursor:
        print(row)

    cursor.execute(""" SELECT COUNT(DISTINCT userId) FROM games """)
    print()
    for row in cursor:
        print("сколько игроков:", row)

    cursor.execute(""" SELECT COUNT(userId) FROM games WHERE userId = 1 """)
    for row in cursor:
        cursor.execute(""" SELECT name FROM gamers WHERE id = 1 """)
        for name in cursor:
            print(f"сколько игр y игрока {name}:", row)

    cursor.execute(""" SELECT SUM(score) FROM games WHERE userId = 1 """)
    for row in cursor:
        cursor.execute(""" SELECT name FROM gamers WHERE id = 1 """)
        for row2 in cursor:
            print(f"сумма очков y {row2}:", row)
    print()

    # min - минимальное значение
    cursor.execute(""" SELECT MIN(score) FROM games WHERE userId = 1 """)
    for row in cursor:
        cursor.execute(""" SELECT name FROM gamers WHERE id = 1 """)
        for row2 in cursor:
            print(f"сумма min очков y {row2}:", row)
    # max - минимальное значение
    cursor.execute(""" SELECT MAX(score) FROM games WHERE userId = 1 """)
    for row in cursor:
        cursor.execute(""" SELECT name FROM gamers WHERE id = 1 """)
        for row2 in cursor:
            print(f"сумма max очков y {row2}:", row)
    print()
    cursor.execute(
        """
        SELECT gamers.name,
        COUNT(games.userId),
        SUM(games.score)
        FROM gamers 
        JOIN games ON games.userid = gamers.id
        GROUP BY gamers.name
        """
    )
    for row in cursor:
        print(row)


# COUNT - подсчет количества строк
# SUM - сумма
# AVG - среднее значение
# MAX - максимальное значение
# MIN - минимальное значение
# DISTINCT - уникальные значения
