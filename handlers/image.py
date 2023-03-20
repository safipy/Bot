import random
from aiogram import  types


async def picture(message: types.Message):
    image = ["picture/img", "picture/img.jp", "picture/img.j"]
    photo = open(random.choice(image), 'rb')
    await message.answer_photo(photo)
