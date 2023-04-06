import logging
from aiogram import executor
from aiogram.dispatcher.filters import Text
from config import dp
from config import dp, scheduler
from handlers.command import (start, help, myinfo)
from handlers.image import (picture)
from handlers.products import (show, show_b, show_tf)
from handlers.admin import (ban_user, check_words)
from handlers.user_info_fsm import (UserForm, start_user_dialog, process_age, process_name,
                                    process_address, process_day, mail, not_mail)

from db.base import (init_dp, create_tables, add_products, delete_table_products, get_products,save_order)
from handlers.notifier import (
    UserText,
    start_reminder,
    notifier_text,
    notifier_hour,
    notifier_min)

from handlers.get_products import (grafik, catalog)

async def on_startup(_):
    init_dp()
    create_tables()
    add_products()
    delete_table_products()
    get_products()
    save_order()



logging.basicConfig(level=logging.INFO)

dp.register_callback_query_handler(mail, Text(startswith="yes"))
dp.register_callback_query_handler(not_mail, Text(startswith="no"))
dp.register_message_handler(start_reminder, commands=["notify"])
dp.register_message_handler(notifier_text, state=UserText.text)
dp.register_message_handler(notifier_hour, state=UserText.hour)
dp.register_message_handler(notifier_min, state=UserText.minutes)


dp.register_message_handler(start_user_dialog, commands=["form"])
dp.register_message_handler(process_name, state=UserForm.name)
dp.register_message_handler(process_age, state=UserForm.age)
dp.register_message_handler(process_address, state=UserForm.address)
dp.register_message_handler(process_day, state=UserForm.day)
dp.register_callback_query_handler(mail, Text(startswith="да"))
dp.register_callback_query_handler(not_mail, Text(startswith="нет"))
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

dp.register_message_handler(grafik, Text(startswith="Режим работы"))
dp.register_message_handler(catalog, Text(equals="Ассортимент духов"))
dp.register_callback_query_handler(catalog, Text(equals="Ассортимент духов"))


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp)