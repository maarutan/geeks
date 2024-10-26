import sqlite3 as sq
import os

if os.path.exists("base.db"):
    os.remove("base.db")

with sq.connect("base.db") as connects:
    cursor = connects.cursor()
    cursor.execute(
        """ CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(50),
        surname VARCHAR(50),
        old INTEGER,
        hobby VARCHAR(100),
        dzBall INTEGER
        )
        """
    )

    cursor.execute(
        """ INSERT INTO students(name, surname, old, hobby, dzBall)
                        VALUES
                            ('marat', 'arzymatov', 16, 'chess', 10),
                            ('kamila', 'azybekova', 16, 'shopping', 10),
                            ('nursultan', 'arzymatov', 18, 'coding', 10),
                            ('bekbolot', 'neznayu', 19, 'sports', 10),
                            ('yryskeldy', 'narynbekov', 16, 'music', 10),
                            ('kyaz', 'neznayu', 17, 'painting', 10),
                            ('romazan', 'omoldoshev', 15, 'gaming', 10),
                            ('aibike', 'azybekova', 18, 'dancing', 10),
                            ('aisha', 'azybekova', 16, 'cooking', 10),
                            ('bayaman', 'azybekov', 17, 'traveling', 10)
                   """
    )
    cursor.execute(
        """ SELECT * FROM students WHERE LENGTH(surname) = 10 AND dzBall = 10"""
    )
    studentsSort = cursor.fetchall()

    cursor.execute(""" DELETE FROM students WHERE id % 2 = 0""")
    for row in studentsSort:
        students = row[0]
        cursor.execute(
            """ UPDATE students SET name = 'genius' WHERE id = ?""", (students,)
        )

    for i in studentsSort:
        stuentsidPrint = i[0]
        cursor.execute(""" SELECT * FROM students WHERE id = ?""", (stuentsidPrint,))
        print(cursor.fetchall())
