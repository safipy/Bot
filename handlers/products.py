from aiogram import types
#from config import bot

kb = types.ReplyKeyboardMarkup()
kb.add(
    types.KeyboardButton("BYREDO")
)
in_kb = types.InlineKeyboardMarkup()
in_kb.add(types.InlineKeyboardButton(
    text="BLANCE",
    callback_data="parfume"
))
in_kb.add(types.InlineKeyboardButton(
    text="GYPSY WATER",
    callback_data="parfume"
))
kb.add(
    types.KeyboardButton("TOM FORD")
)
in_kb_s = types.InlineKeyboardMarkup()
in_kb_s.add(types.InlineKeyboardButton(
    text="LOST CHERRY",
    callback_data="parfume"
))
in_kb_s.add(types.InlineKeyboardButton(
    text="ROSE DAMALFI",
    callback_data="parfume"
))


async def show(call: types.CallbackQuery):
    """
        Показывает товар
    """
    await call.message.answer(
        text="Выберите бренд парфюма:",
        reply_markup=kb
    )


async def show_b(message: types.Message):
    """
       Показать виды выбранного товара
    """
    await message.reply(
      text="Какой запах, BLANCE вам нужен?",
      reply_markup=in_kb
    )

async def show_tf(message: types.Message):
    """
       Показать виды выбранного товара
    """
    await message.reply(
      text="Какой запах, TOM FORD вам нужен?",
      reply_markup=in_kb_s
    )