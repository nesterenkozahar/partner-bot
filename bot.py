from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = "8103348822:AAHRUmDFCaGLbKKxwOpwZRK8zI700KMQezc"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Тексты по кнопкам
options = {
    "Прием и выдача наличных": (
        "📦 *Прием и выдача наличных в большинстве стран мира*\n\n"
        "— Работаем с EUR, USD и другими валютами\n"
        "— Поддержка крупных сумм\n"
        "— Безопасные и проверенные партнёры\n"
        "— Быстрые сроки: от 1 дня\n"
        "— Индивидуальные условия по стране и сумме\n\n"
        "📍 Уточните страну, валюту и объём — подберём оптимальное решение."
    ),
    "Оплата по инвойсам": (
        "🧾 *Оплата по заграничным инвойсам для бизнеса*\n\n"
        "— Оплата в течение 1–3 рабочих дней\n"
        "— Поддержка USD, EUR и других валют\n"
        "— Работаем с юр.лицами и ИП\n"
        "— Возможна оплата из дружественных юрисдикций\n"
        "— Предоставляем подтверждение об оплате\n\n"
        "📌 Уточните валюту, сумму и страну назначения."
    ),
    "Перевод наличных": (
        "🌍 *Перевод наличных средств в любую точку мира*\n\n"
        "— Работаем по заявке: страна → страна\n"
        "— Быстрые сроки: от 1 дня\n"
        "— Безопасные маршруты\n"
        "— Поддержка крупных сумм\n"
        "— Подходит как для частных, так и для корпоративных клиентов\n\n"
        "💬 Уточните откуда → куда, сумму и срок."
    ),
    "Возврат валюты": (
        "💸 *Возврат валюты с зарубежных счетов и бизнеса*\n\n"
        "— Помогаем безопасно вернуть выручку или личные средства\n"
        "— Возможен возврат из Европы, Азии, ОАЭ, Турции и др.\n"
        "— Используем легальные и эффективные маршруты\n"
        "— Без блокировок, с документальным сопровождением\n"
        "— Индивидуальный подход под кейс\n\n"
        "📩 Опишите юрисдикцию и объём — предложим вариант."
    ),
    "Перевод в безопасную юрисдикцию": (
        "🏦 *Перевод с личных счетов в безопасную юрисдикцию*\n\n"
        "— Работаем с РФ, СНГ, ЕС, Турцией и др.\n"
        "— Вывод средств без нарушения валютного контроля\n"
        "— Поддержка как физлиц, так и ИП\n"
        "— Документальное сопровождение при необходимости\n"
        "— Гарантируем конфиденциальность\n\n"
        "📋 Уточните страну и объём — обсудим решение."
    ),
    "Оплата заграничных счетов": (
        "💳 *Оплата заграничных счетов (аренда, услуги, товары)*\n\n"
        "— Оплата в USD, EUR, AED и др.\n"
        "— Работаем с юр.лицами и физлицами\n"
        "— Быстрая и надёжная схема\n"
        "— Возможность регулярных оплат по договору\n"
        "— Подходит для аренды, обучения, маркетплейсов\n\n"
        "📤 Уточните страну и сумму — рассчитаем условия."
    )
}

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
for key in options.keys():
    keyboard.add(KeyboardButton(text=key))

@dp.message_handler(commands=["start"])
async def start_cmd(message: types.Message):
    await message.answer("Выберите интересующий пункт:", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text in options)
async def handle_option(message: types.Message):
    try:
        await message.delete()
    except:
        pass
    text = options[message.text]
    copy_button = InlineKeyboardMarkup().add(InlineKeyboardButton("📋 Скопировать", callback_data=message.text))
    await message.answer(text, parse_mode="Markdown", reply_markup=copy_button)

@dp.callback_query_handler(lambda call: call.data in options)
async def handle_copy(call: types.CallbackQuery):
    await call.message.answer(options[call.data], parse_mode="Markdown")

if __name__ == "__main__":
    executor.start_polling(dp)
