from aiogram import Dispatcher, types
from tgbot.keyboards.inline import chat_button


async def chat_c(message: types.Message):
    if message.chat.type == 'private':
        await message.reply('Ласкаво просимо!)', reply_markup=chat_button)

def register_chat_button(dp: Dispatcher):
    dp.register_message_handler(chat_c, text='Наш чат 💭')