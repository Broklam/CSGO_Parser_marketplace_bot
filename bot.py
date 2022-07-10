import json

from aiogram import Bot, Dispatcher, executor, types
import os
from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import hbold, hlink
from parser import data_collect
import time

token = '5575168151:AAFN-nVl90vzfqCceIbVJ3uxzxRbhfRVVY8'
bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dispatcher = Dispatcher(bot)


@dispatcher.message_handler(commands='start')
async def start(message: types.Message):
    start_buttons = ['Ножи', 'Перчатки', 'Снайперские винтовки']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)

    await message.answer('Выберите категорию', reply_markup=keyboard)


@dispatcher.message_handler(Text(equals='Ножи'))
async def get_discounted_knives(message: types.Message):
    await message.answer('Запрос обрабатывается...')
    data_collect()
    with open('result.json') as file:
        data = json.load(file)

    for index, item in enumerate(data):
        card = f'{hlink(item.get("full_name"), item.get("3d"))}\n' \
               f'{hbold("Скидка: ")}{item.get("overprice")}%\n' \
               f'{hbold("Цена: ")}${item.get("item_price")}'

        if index % 20 == 0:
            time.sleep(3)
            await message.answer(card)


def main():
    executor.start_polling(dispatcher)


if __name__ == '__main__':
    main()
