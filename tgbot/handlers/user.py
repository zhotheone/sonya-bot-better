from aiogram import Dispatcher
from aiogram.types import Message
from tgbot.keyboards.reply import menu


async def user_start(message: Message):
    if message.chat.type == 'private':
        await message.reply("Привіт, це бот підтримки телеграм-каналу «Архів Дань Хе»! Тут ми зможемо відповісти на Ваші запитання та пропозиції.", reply_markup=menu)


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")
