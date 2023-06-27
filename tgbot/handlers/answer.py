from aiogram import types, Dispatcher
import re
from ex import bot

async def answer(message: types.Message):
    if message.chat.type != 'private':
        id = re.search("\d+", message.text)
        listt = message.text.split(" ")
        answer = ' '.join(listt[2:])
        await bot.send_message(id.group(), answer)

def register_answer(dp: Dispatcher):
    dp.register_message_handler(answer, commands=['answer'])