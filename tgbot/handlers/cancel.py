from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from tgbot.keyboards.reply import menu

async def cancel_c(message: types.Message, state: FSMContext):
    puk = await state.get_state()
    if puk == None:
        pass
    else:
        await state.finish()
        await message.reply('Успішно', reply_markup=menu)


def register_cancel(dp: Dispatcher):
    dp.register_message_handler(cancel_c, text='Скасувати ❌', state='*')