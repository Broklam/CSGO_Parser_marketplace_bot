import json

from aiogram import Bot, Dispatcher, executor, types
import os
from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import hbold, hlink
from parser import data_collect
import time

token = 'TOKEN'
bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dispatcher = Dispatcher(bot)


@dispatcher.message_handler(commands='start')
async def start(message: types.Message):
    start_buttons = ['Что это и зачем?']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)

    await message.answer('Выберите категорию', reply_markup=keyboard)


@dispatcher.message_handler(Text(equals='Что это и зачем?'))
async def what(message: types.Message):
    what_buttons = ['Предложения']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*what_buttons)
    await message.answer(
        'Изучаю парсинг.\n\nБот собирает данные с биржи КС МАНИ епта, затем отбирает из них скидочные предложения.\nТам еще и инфы вдобавок достаточно.\n\nВ планах конечно сделать поиск по размеру скидки или предметам, но в данный момент поебать',reply_markup=keyboard)

@dispatcher.message_handler(Text(equals='Предложения'))
async def get_discounted(message: types.Message):
    await message.answer('Запрос обрабатывается...\n\nЭто может занять до 5 минут.\n\nПридет кстати примерно около 100 сообщений сразу.\n\nСоветую выключить звук')
    data_collect()
    # await message.answer(f"В данный момент обрабатывается страница {}")
    with open('result.json') as file:
        data = json.load(file)

    for index, item in enumerate(data):
        card = f'{hlink(item.get("full_name"), item.get("3d"))}\n' \
               f'{hbold("Скидка: ")}{item.get("overprice")}%\n' \
               f'{hbold("Цена: ")}${item.get("item_price")}\n' \
               f'{hbold("Cтарая цена: ")}${item.get("oldPrice")}\n' \
               f'{hbold("Деф цена: ")}${item.get("default price")}\n' \
               f'{hbold("float: ")}{item.get("float")}\n'
        await message.answer(card)

        if index % 30 == 0:
            time.sleep(3)

            # await message.answer(card)


def main():
    executor.start_polling(dispatcher)


if __name__ == '__main__':
    main()
