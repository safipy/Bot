from aiogram import types, bot
from config import scheduler, bot
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext


class UserText(StatesGroup):
    text = State()
    hour = State()
    minutes = State()

async def start_reminder(message: types.Message):
    """
    Запрашиваем текст напоминалки у пользователя
    """
    await UserText.text.set()
    await message.answer("Input your reminder:")

async def notifier_text(message: types.Message, state: FSMContext):
    """
    функция тригерится на "notify", сохраняет остальной текст
    и запускает состояние
    """
    await UserText.text.set()
    text = message.text
    key_word = "напомнить"
    await message.answer("Принято!")
    if key_word in text:
        text_res = text.split(' ', 1)[1]
        text=text_res
        await message.answer(f"your reminder text is: <<{text}>>")
    else:
        text= text
        await message.answer(f"your reminder text is: <<{text}>>")

    async with state.proxy() as data:
        data['text'] = text
    await UserText.next()
    await message.answer("Input hour:")


async def notifier_hour(message: types.Message, state: FSMContext):
    """
    спрашивает у пользователя час, сохраняет и запускает
    """
    hour = message.text
    if not hour.isnumeric():
        await message.reply("Input only numbers!")
    elif int(hour) < 0 or int(hour) > 23:
        await message.reply("Input in correct-24h format!")
    else:
        async with state.proxy() as data:
            data['hour'] = hour
            await UserText.next()
            await message.answer("Input minutes: ")


async def notifier_min(message: types.Message, state: FSMContext):
    """
    спрашивает у пользователя минуты, сохраняет и запускает
    """
    minutes = message.text
    if not minutes.isnumeric():
        await message.reply("Input only numbers!")
    elif int(minutes) < 0 or int(minutes) > 59:
        await message.reply("Input in correct-60min format!")
    else:
        async with state.proxy() as data:
            data['minutes'] = minutes
            print(data)
            text = data['text']
            minutes = int(data['minutes'])
            hour = int(data['hour'])

    await message.answer(f"got it, reminder {text} will be notified at {hour}:{minutes}")
    await state.finish()

    async def notify(user_id: int):
        await bot.send_message(
            text=f'Reminder: {text}',
            chat_id=user_id
        )

    scheduler.add_job(notify, 'cron', hour=hour, minute=minutes, args=(message.from_user.id,))
