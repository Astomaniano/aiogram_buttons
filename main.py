# Задание 1: Создание простого меню с кнопками
# При отправке команды /start бот будет показывать меню с кнопками "Привет" и "Пока". При нажатии на кнопку "Привет"
# бот должен отвечать "Привет, {имя пользователя}!", а при нажатии на кнопку "Пока" бот должен отвечать "До свидания,
# {имя пользователя}!".
#
# Задание 2: Кнопки с URL-ссылками
# При отправке команды /links бот будет показывать инлайн-кнопки с URL-ссылками. Создайте три кнопки с ссылками
# на новости/музыку/видео
#
# Задание 3: Динамическое изменение клавиатуры
# При отправке команды /dynamic бот будет показывать инлайн-кнопку "Показать больше". При нажатии на эту кнопку бот
# должен заменять её на две новые кнопки "Опция 1" и "Опция 2". При нажатии на любую из этих кнопок бот должен
# отправлять сообщение с текстом выбранной опции.

import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile, CallbackQuery

from config import TOKEN
import keyboards as keyb

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f"Привет, {message.from_user.first_name}!", reply_markup=keyb.inline_keyboard)

@dp.callback_query(F.data == 'hello') #хендлер для инлайн клавиатуры по захвату callback_data
async def catalog(callback: CallbackQuery):
    await callback.message.answer(f"Привет, {callback.from_user.first_name}!")

@dp.callback_query(F.data == 'bye') #хендлер для инлайн клавиатуры по захвату callback_data
async def catalog(callback: CallbackQuery):
    await callback.message.answer(f"До свидания, {callback.from_user.first_name}!")

@dp.message(Command(commands=['links']))
async def links(message: Message):
    await message.answer("Ссылки на новости, музыку и видео", reply_markup=await keyb.keyboard_links())

@dp.message(Command(commands=['dynamic']))
async def dynamic(message: Message):
    await message.answer("Здесь ты можешь посмотреть все опции:", reply_markup=keyb.keyboard_dynamic)

@dp.callback_query(F.data == 'more') #хендлер для инлайн клавиатуры по захвату callback_data
async def catalog(callback: CallbackQuery):
    await callback.message.answer(f"Попробуй наши опции", reply_markup=await keyb.keyboard_dynamic_options())

@dp.callback_query(F.data == 'option 1')
async def option_1(callback: CallbackQuery):
    await callback.answer("открываются опции")
    await callback.message.answer(f"Это Первая Опция")

@dp.callback_query(F.data == 'option 2')
async def option_2(callback: CallbackQuery):
    await callback.answer("открываются опции")
    await callback.message.answer(f"Это Вторая Опция")

@dp.callback_query(F.data == 'back')
async def back(callback: CallbackQuery):
    await callback.message.answer(f"Здесь ты можешь посмотреть все опции", reply_markup=keyb.keyboard_dynamic)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())