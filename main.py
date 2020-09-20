# -*- coding: utf-8 -*-

import pyowm
import config
import logging
from aiogram import Bot, Dispatcher, executor, types
import random

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

owm = pyowm.OWM("4052ee0b6353371d1b7acdc7bfe593a8")
manager = owm.weather_manager()
observation = manager.weather_at_place(config.PLACE)

weather_calls = [
    "Погода", "Скажи погоду", 
    "Скажи мне погоду", "Кинь погоду",
    "Дай погоду", "Кинь мне погоду",
    "Какая сейчас погода", "Какая погода",
    "Че по погоде", "Че там по погоде", "Чё там по по погоде
    "Чё по погоде", "Как там погода", "Как погода",
]
welcome_calls = [
    "Hi", "Hello", "Privet", "Дратути",
    "Прив", "Привет", "Хай", 
    "Здравствуйте", "Добрый день", "Добрый вечер", 
    "Доброе утро", "Здравствуй", "Приветик",
]
welcome_answers = [
    "Hi", "Hello", "Privet", "Дратути",
    "Прив", "Привет", "Хай", 
    "Здравствуйте", "Здравствуй", "Приветик",
]
thank_calls = [
    "Спасибо", "Благодарю", "Благодарочка", 
    "Благодарен","Спс", "Спасибки", 
    "Пасибки", "Спасиб", "Четко",
    "Четенько", "Чётенько",
]
thank_answers = [
    "Не за что)", "Всегда пожалуйста)", 
    "Нет проблем", "Пожалуйста", 
    "Обращайтесь ;)", "Не стоит благодарности",
]

@dp.message_handler()
async def echo(message: types.Message):
    if message.text in weather_calls:
        weather = observation.weather

        if weather.status == "Rain":
            weather1 = "дождь"
        elif weather.status == "Clouds":
            weather1 = "облачно"
        elif weather.status == "Clear":
            weather1 = "солнечнo"
        else:
            weather1 = weather.status

        temp = int(weather.temperature("celsius")["temp"])
        temp_min = int(weather.temperature("celsius")["temp_min"])
        temp_max = int(weather.temperature("celsius")["temp_max"])
        
        await message.answer(f"В городе {config.PLACE.split(',')[0]} сейчас {weather1}\nТемпература в районе {temp} градусов")
    
    elif message.text in welcome_calls:
        await message.answer(random.choice(welcome_answers))
    
    elif message.text in thank_calls:
        random_answer = random.choice(thank_answers)
        await message.answer(random_answer)
    
    else:
        await message.answer("Извините, я вас не понял")

executor.start_polling(dp, skip_updates=True)