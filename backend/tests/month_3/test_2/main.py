from config import dp, executor
from handlers import commands, add_in_store, send_products, fsm_order
from db import db_main
import logging

commands.register_commands(dp)
add_in_store.register_fsm_add(dp)
send_products.register_handlers_send_products(dp)
fsm_order.register_handlers_fsm_order(dp)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=db_main.sql_create)
#
