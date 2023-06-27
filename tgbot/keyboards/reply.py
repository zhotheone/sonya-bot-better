from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button1 = KeyboardButton('Підтримка 🆘')
button2 = KeyboardButton('Фідбек 🗣')
button3 = KeyboardButton('Надіслати арт 🖼')
button4 = KeyboardButton('Наш чат 💭')


menu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).row(button1, button2).add(button3).add(button4)

cancel_button = KeyboardButton('Скасувати ❌')
cancel = ReplyKeyboardMarkup(resize_keyboard=True).add(cancel_button)