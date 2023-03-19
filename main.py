import logging
import random
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os

load_dotenv()

bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("Добро пожаловать!")


@dp.message_handler(commands=["help"])
async def help(message: types.Message):
    await message.answer(
        """
/start - Приветствие
/help - Функции Бота
/myinfo - Ваши личные данные
/picture - Картинка для хорошего настроения
      """
    )


@dp.message_handler(commands=["myinfo"])
async def myinfo(message: types.Message):
    user_firstname = message.from_user.first_name
    user_name = message.from_user.username
    user_id = message.from_user.id
    await message.answer(
        f"Ваше имя - {user_firstname} "
        f"\nВаше имя пользователя - {user_name} "
        f"\nВаш id - {user_id} "
    )


@dp.message_handler(commands=["picture"])
async def picture(message: types.Message):
    image = ["picture/img", "picture/img.jp", "picture/img.j"]
    photo = open(random.choice(image), 'rb')
    await message.answer_photo(photo)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp)
