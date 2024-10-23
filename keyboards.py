from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

# Клавиатура с кнопками ПРИВЕТ и ПОка
inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
   [InlineKeyboardButton(text="Привет", callback_data="hello"), InlineKeyboardButton(text="Пока", callback_data="bye")]
])

# Словарь с текстами кнопок и соответствующими URL
button_links = {
    "Новости": "https://dzen.ru/news?ysclid=m2lgnz7i64213667675",
    "Музыка": "https://music.yandex.ru/home/?ysclid=m2lgp260mb680903494",
    "Видео": "https://rutube.ru/"
}

# Клавиатура с кнопками "Новости", "Музыка" и "Видео" из словаря
async def keyboard_links():
    kb = InlineKeyboardBuilder()
    for text, url in button_links.items():
        kb.add(InlineKeyboardButton(text=text, url=url))

    return kb.adjust(3).as_markup()


keyboard_dynamic = InlineKeyboardMarkup(inline_keyboard=[
   [InlineKeyboardButton(text="Показать больше", callback_data='more')]])

async def keyboard_dynamic_options():
    kb = InlineKeyboardBuilder()
    kb.add(InlineKeyboardButton(text="Опция 1", callback_data="option 1"))
    kb.add(InlineKeyboardButton(text="Опция 2", callback_data="option 2"))

# Добавляем кнопку "Назад"
    kb.row(InlineKeyboardButton(text="Назад", callback_data="back"))

    return kb.adjust(2).as_markup()