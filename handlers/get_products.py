from aiogram import types
from db.base import get_products



async def grafik(message: types.Message):
    await message.reply("""
График работы: 
Понедельник - Пятница с 09:00 до 18:00 
Суббота с 10:00 до 17:00
Воскресенье - выходной

с 13:00 до 14:00 обеденный перерыв 
    """)


def kb_buy(product_id: int):
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton(
        text="Buy",
        calback_data=f'buy_product_{product_id}'))
    return kb



async def catalog(message: types.Message):
    await message.answer(
        text="Наши товары:"
    )
    for product in get_products():
        print(product)
        # with open(product[3], 'rb') as image:
        await message.answer_photo(
            photo=open(product[3], 'rb'),
            caption=f'Товар: {product[1]}\n Цена:{product[2]}',
            reply_markup=kb_buy(product[0])
        )


