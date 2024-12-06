# db_main.py
# CRUD - CREAD READ update DELETE
import sqlite3
from db import queries
import aiosqlite


db = sqlite3.connect('db/store.sqlite3')
cursor = db.cursor()

async def sql_create():
    if db:
        print('База данных подключена!')
    cursor.execute(queries.CREATE_TABLE_TABLE)
    cursor.execute(queries.CREATE_TABLE_TABLE_DETAIL)



# Запись стадий FSM_store
# ====================================================================================

async def sql_insert_store(name_product, product_id, size, price, photo):
    cursor.execute(queries.INSERT_STORE, (
        name_product, product_id, size, price, photo
    ))
    db.commit()


async def sql_insert_store_detail(info_product, product_id, category):
    cursor.execute(queries.INSERT_STORE_DETAIL, (
        info_product, product_id, category
    ))
    db.commit()


# CRUD - Read
# ====================================================================================

def get_db_connection():
    conn = sqlite3.connect('db/store.sqlite3')
    conn.row_factory = sqlite3.Row
    return conn


def fetch_all_products():
    conn = get_db_connection()
    products = conn.execute("""
        SELECT * FROM store s
        INNER JOIN store_detail sd ON s.product_id = sd.product_id
        """).fetchall()
    conn.close()
    return products


# CRUD - Delete
# ====================================================================================

def delete_product(product_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM STORE WHERE product_id = ?', (product_id,))

    conn.commit()
    conn.close()



# CRUD - Update
# ====================================================================================

def update_product_field(product_id, field_name, new_valeu):
    store_table = ["name_product", "size", "price", "photo"]
    store_detail_table = ["info_product", "category"]

    conn = get_db_connection()

    try:
        if field_name in store_table:
            query = f'UPDATE store SET {field_name} = ? WHERE product_id = ?'
        elif field_name in store_detail_table:
            query = f'UPDATE store_detail SET {field_name} = ? WHERE product_id = ?'

        else: 
            raise ValueError(f'Нет такого поля {field_name}')
        
        conn.execute(query, (new_valeu, product_id))

        conn.commit()
    except sqlite3.OperationalError as e:
        print(f'Ошибка - {e}')

    finally:
        conn.close()


