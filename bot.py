from aiogram import Bot, Dispatcher, types, executor

API_TOKEN = 8103348822:AAHRUmDFCaGLbKKxwOpwZRK8zI700KMQezc

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Возможности отдела
options = {
    "Прием и выдача наличных": "Мы осуществляем приём и выдачу наличных в большинстве стран мира.",
    "Оплата по инвойсам": "Помогаем оплатить заграничные инвойсы для бизнеса в течение 3 дней.",
    "Перевод наличных": "Осуществляем перевод наличных средств в любую точку мира.",
    "Возврат валюты": "Возвращаем валюту из заграничных счетов и выручку с бизнеса.",
    "Перевод в безопасную юрисдикцию": "Переведем средства с личных счетов РФ и других стран в безопасную юрисдикцию.",
    "Оплата заграничных счетов": "Помогаем оплатить заграничные счета."
}

@dp.message_handler(commands=["start"])
async def start_cmd(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for key in options.keys():
        keyboard.add(types.KeyboardButton(text=key))
    await message.answer("Выберите интересующий пункт:", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text in options)
async def handle_option(message: types.Message):
    await message.answer(options[message.text])

if __name__ == "__main__":
    executor.start_polling(dp)
