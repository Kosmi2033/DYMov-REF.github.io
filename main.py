from aiogram import Bot, Dispatcher,executor, types
from aiogram.types import WebAppInfo

bot = Bot('7555088687:AAEiGeTVUefc4ZmZlu9ApO9K3qiofoJzbts')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.KeyboardButton('Open Website', web_app=WebAppInfo(url='https://kosmi2033.github.io/DYMov-REF.github.io/')))
    await message.answer('Hello, my friend', reply_markup=markup)

executor.start_polling(dp)