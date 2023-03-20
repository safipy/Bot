import logging
from aiogram import executor
from aiogram.dispatcher.filters import Text
from config import dp
from handlers.command import (start, help, myinfo)
from handlers.image import (picture)
from handlers.products import (show, show_b, show_tf)
from handlers.admin import (ban_user, check_words)



dp.message_handler(start, commands=["start"])
dp.message_handler(help, commands=["help"])
dp.message_handler(myinfo, commands=["myinfo"])
dp.message_handler(picture, commands=["picture"])
dp.register_callback_query_handler(show, Text(startswith="smartphone"))
dp.register_message_handler(show, commands=["parfume"])
dp.register_message_handler(show_b, Text(startswith="BYREDO"))
dp.register_message_handler(show_tf, Text(startswith="TOM FORD"))
dp.register_message_handler(ban_user, commands=['да'], commands_prefix='!')
dp.register_message_handler(check_words)
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp)