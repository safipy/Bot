from aiogram import types
async def check_user_is_admin(message: types.Message):
    """
    Проверка на админа
    """
    admins = await message.chat.get_administrators()
    for admin in admins:
        if admin["user"]["id"] == message.from_user.id:
            return True
    return False

async def check_words(message: types.Message):
    """
    Фильтр на плохие слова
    """
    BAD_WORDS = ['дурак', 'идиот']
    if message.chat.type != 'private':
        for i in BAD_WORDS:
            if i in message.text.lower().replace('', ''):
                await message.reply(
                    text=f"Пользователь {message.from_user.first_name} отправил"
                         f"запрещённое слово\n"
                         f"Админы удалять {message.from_user.first_name}: да/нет?")
                break


async def ban_user(message: types.Message):
    """
    Бан пользователя
    """
    if message.chat.type != 'private':
        admin_author = await check_user_is_admin(message)
        print(f"{admin_author=}")
        if admin_author and message.reply_to_message:
            await message.bot.ban_chat_member(
                chat_id=message.chat.id,
                user_id=message.reply_to_message.from_user.id
            )
