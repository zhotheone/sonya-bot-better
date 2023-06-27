from aiogram import Dispatcher, types
from tgbot.services.sendart_states import Sendart
from aiogram.dispatcher import FSMContext
from ex import bot
from tgbot.keyboards.inline import chat_button
from tgbot.keyboards.reply import cancel, menu

async def sendart_c(message: types.Message):
    if message.chat.type == 'private':
        await message.answer('Якщо у Вас є улюблений артер(ка), Ви можете надіслати зображення (бажано файлом) з кредітами (посиланнями) автора. Адміністратори в рандомному порядку його опублікують.\nПросимо не ображатись, якщо Ви одразу не побачите запропонований Вами арт на каналі, ми спробуємо опублікувати усі по можливості.', reply_markup=cancel)
        await Sendart.ans.set()

async def sendart_ans(message: types.Message, state: FSMContext):
    config = bot.get('config')
    if message.photo:
        photo = message.photo[-1].file_id
        await bot.send_photo(config.misc.groupid, photo, caption=message.caption)
        await bot.send_message(config.misc.groupid, f'From: @{message.from_user.username}')
    else:
        doc = message.document.file_id
        await bot.send_document(config.misc.groupid, doc, caption=message.caption)
        await bot.send_message(config.misc.groupid, f'From: @{message.from_user.username}')
    await message.reply('Дякуємо, за цей гарний арт, ми спробуємо його опублікувати найближчим часом.', reply_markup=menu)
    await state.finish()

def register_sendart(dp: Dispatcher):
    dp.register_message_handler(sendart_c, text='Надіслати арт 🖼', state=None)
    dp.register_message_handler(sendart_ans, content_types=['photo', 'document'], state=Sendart.ans)