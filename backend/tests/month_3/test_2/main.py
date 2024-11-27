from config import dp, executor
from handlers import send_message, commands, add_in_store
import logging

commands.register_commands(dp)
add_in_store.register_fsm_add(dp)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
