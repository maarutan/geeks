# SQL - Structured Query Language
# СЯЗ - СтруктурированныйЯзыкЗапросов
# datebase - база данных
# СУБД - СистемаУправленияБазамиДанных
# relation - то что относится к базе данных в табличном виде
# noRelation - то что не относится к базе данных в табличном виде
# CRUD - Create, Read, Update, Delete


# wtih {
#    connect - {
#      cursor - курсор {
#          execute() - выполнить запрос {
#              CRUD - Create, Read, Update, Delete
#          }
#      }
#    }
# }


# ----------------------Clreate---------------------
import sqlite3 as sq




with sq.connect("test.db") as connection:
    cursor = connection.cursor()
    cursor.execute(
        """ CREATE TABLE IF NOT EXISTS users ( 
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    fio VARCHAR(100),
                    old INTEGER DEFAULT 0
                   ) 
    """
    )

    # 1--------------------------------------------------
    # CREATE TABLE - это создать таблицу
    # IF NOT EXISTS - если таблицы нет, то создать
    # а если есть то не создавать и работать с ней

    # 2--------------------------------------------------
    # cursor.execute - это метод который выполняет запрос
    # INTEGER -  это тип данных int
    # PRIMARY KEY - это первичный ключ
    # AUTOINCREMENT - это автоинкремент (создает уникальные значения)
    # 3--------------------------------------------------
    # VARCHAR(100) - это тип данных строка, где 100 это длина строки
    # INTEGER - это тип данных int
    # DEFAULT - это значение по умолчанию
    # --------------------add------------------------

    # cursor.execute(
    #     """
    #                 INSERT INTO users(fio, old)
    #                 VALUES
    #                     ('Bekbolo', 60),
    #                     ('Marat', 16),
    #                     ('beka', 123)

    #                """
    # )

    # 1--------------------------------------------------
    # INSERT - Это операция Вставки данных в таблицу
    # INTO - это вставить в
    # VALUES - это значения которые мы вставляем
    # 2--------------------------------------------------

    # -----------------fetchBase-------------------------
    # cursor.execute(""" SELECT fio,old FROM users  """)
    # print(cursor.fetchall())
    # print(cursor.fetchone())
    # print(cursor.fetchmany(2))

    # for i in cursor:
    #     print(i)

    # 1 -------------------------------------------------
    # SELECT - это операция выбора данных | как return в функции
    # FROM - это откуда выбирать
    #
    # ----------------------fetch------------------------
    # fetchall() - это метод который возвращает все данные
    # fetchone() - это метод который возвращает одну строку
    # fetchmany() - это метод который возвращает несколько строк
    # {
    # for i in cursor:
    #     print(i)
    # } - это цикл который выводит все строки
    # ----------------------Update------------------------

    cursor.execute(""" UPDATE users SET old = 50 WHERE id = 1 """)
    print()

    cursor.execute(""" SELECT * FROM users  """)
    # for i in cursor:
    #     print(i)
    # # 1--------------------------------------------------
    # UPDATE - это операция обновления данных
    # SET - это установить
    # WHERE - это где
    # WHERE - это как if в цикле
    # WHERE операторы - =, >, <, >=, <=, !=, LIKE, IN, BETWEEN, IS NULL, IS NOT NULL

    # ----------------------Delete------------------------

    cursor.execute(""" DELETE FROM users WHERE fio = 'beka' """)

    for i in cursor:
        print(i)
