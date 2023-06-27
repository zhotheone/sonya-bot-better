from aiogram import Dispatcher, types
from tgbot.services.feedback_states import Feedback
from aiogram.dispatcher import FSMContext
from aiogram.utils.markdown import hcode
from ex import bot
from tgbot.keyboards.reply import cancel, menu

async def feedback_c(message: types.Message):
    if message.chat.type == 'private':
        await message.answer('Тут Ви можете залишити відгук про канал або поставити запитання адміністраторам <u>анонімно.</u> Ваш юзернейм не буде доступний для адміністраторів. Якщо Ви хочете отримати відповідь від адміністраторів особисто у приватні повідомлення, краще перейдіть до кнопки Підтримка', reply_markup=cancel)
        await Feedback.ans.set()

async def feedback_ans(message: types.Message, state: FSMContext):
    answer = message.text
    config = bot.get('config')
    await message.reply('Дякуємо за ваш відгук або запитання. Адміністратор невдовзі зв’яжеться з Вами.', reply_markup=menu)
    await bot.send_message(config.misc.groupid, f'Фідбек 🗣: {answer}\nВідповісти: {hcode(f"/answer {message.chat.id} ")}')
    await state.finish()

def register_feedback(dp: Dispatcher):
    dp.register_message_handler(feedback_c, text='Фідбек 🗣', state=None)
    dp.register_message_handler(feedback_ans, state=Feedback.ans)