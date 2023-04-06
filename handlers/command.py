from aiogram import types

in_kb = types.InlineKeyboardMarkup()
in_kb.add(types.InlineKeyboardButton(
    text="Наши товары:",
    callback_data="parfume"
))
async def start(message: types.Message):
    user = message.from_user.first_name
    await message.answer(
        f"Добро пожаловать, {user}!",
        reply_markup=in_kb
    )


async def help(message: types.Message):
    await message.answer(
        """
        /start - Наши товары
        /help - помощь бота
        /myinfo - ваши личные данные
        /picture - катринки для настроения
        """)

async def myinfo(message: types.Message):
     user_firstname = message.from_user.first_name
     user_name = message.from_user.username
     user_id = message.from_user.id
     await message.answer(
       f"Ваше имя - {user_firstname} "
       f"\nВаше имя пользователя - {user_name} "
       f"\nВаш id - {user_id} "
        )
