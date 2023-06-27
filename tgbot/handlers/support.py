from aiogram import Dispatcher, types
from tgbot.services.support_states import Support
from aiogram.dispatcher import FSMContext
from ex import bot
from tgbot.keyboards.reply import cancel, menu

async def support_c(message: types.Message):
    if message.chat.type == 'private':
        await message.answer('Зауважимо, що <u>після того як ви напишете повідомлення через цю команду, адміністраторам буде доступний Ваш юзеренейм</u> для того, щоб вони могли зв’язатись з Вами.\nЗалиште Вашу пропозицію або запит на рекламу/взаємний піар.', reply_markup=cancel)
        await Support.ans.set()

async def support_ans(message: types.Message, state: FSMContext):
    answer = message.text
    config = bot.get('config')
    await message.reply('Дякуємо, що звернулись до нас, невдовзі адміністратори зв’яжуться з Вами.', reply_markup=menu)
    await bot.send_message(config.misc.groupid, f'Підтримка 🆘: {answer}\nFrom: @{message.from_user.username}')
    await state.finish()

def register_support(dp: Dispatcher):
    dp.register_message_handler(support_c, text='Підтримка 🆘', state=None)
    dp.register_message_handler(support_ans, state=Support.ans)