from django.shortcuts import render
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6287877530:AAEGHSuJgsvNzP2p3m6L7LD071p9cBw49hY'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])  # Явно указываем в декораторе, на какую команду реагируем.
async def send_welcome(message: types.Message):
        await message.reply(
            "Привет!\nЯ Эхо-бот от Skillbox!\nОтправь мне любое сообщение, а я тебе обязательно отвечу.")  # Так как код работает асинхронно, то обязательно пишем await.


@dp.message_handler()  # Создаём новое событие, которое запускается в ответ на любой текст, введённый пользователем.
async def echo(
            message: types.Message):  # Создаём функцию с простой задачей — отправить обратно тот же текст, что ввёл пользователь.
        await message.answer(message.text)