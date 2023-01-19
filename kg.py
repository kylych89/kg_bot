from datetime import datetime
import requests
import datetime
from aiogram import Bot, Dispatcher, types, executor
import pyqrcode as pr
import os

from config import TOKEN, open_weather_token

bot = Bot(TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    with open('voices/Sound.mp3', 'rb') as v:
        await bot.send_voice(message.chat.id, v)

    await message.reply(
        f"Саламатсызбы {message.from_user.username} \n"
        f"Областтар жонундо маалымат билуу учун жана \n qrcode кылуу учун областтын атын жазыныз!")


@dp.message_handler()
async def send_text_qr(message: types.Message):
    await message.answer('Сиздин жазган текст кабыл алынды куто турунуз!')

    chui = 'Чуйская область ' \
           'В состав Чуйской области входят 8 районов - Панфиловский район, ' \
           'Жайыльский район, Московский район, Сокулукский район, Аламединский район, ' \
           'Чуйский район, Ысык-Атинский район и Кеминский район'

    talas = 'Таласская область ' \
            'В состав Таласской области входят 4 района - Бакай-Атинский район, Кара-Бууринский район, ' \
            'Манасский район и Таласский район.'

    yssykkul = 'Иссык-Кульская область ' \
               'В состав Иссык-Кульской области входят 5 районов - Ак-Суйский район, ' \
               'Джети-Огузский район, Тонский район, Тюпский район и Иссык-Кульский район.'

    naryn = 'Нарынская область ' \
            'В состав Нарынской области входят 5 районов ' \
            '- Ак-Талинский район, Ат-Башинский район, ' \
            'Жумгальский район, Кочкорский район и Нарынский район.'

    osh = 'Ошская область ' \
          'В состав Ошской области входят 7 районов ' \
          '- Алайский район, Араванский район, Кара-Кулджинский район, ' \
          'Кара-Суйский район, Ноокатский район, Узгенский район и Чон-Алайский район.'

    jalal_abad = 'Джалал-Абадская область ' \
                 'В состав Джалал-Абадской области входят 8 районов ' \
                 '- Аксыйский район, Ала-Букинский район, Базар-Коргонский район, ' \
                 'Ноокенский район, Сузакский район, Тогуз-Тороуский район, ' \
                 'Токтогульский район и Чаткальский район.'

    batken = 'Баткенская область ' \
             'В состав Баткенской области входят 3 района - Баткенский район, Кадамжайский район и Лейлекский район.'

    wrong = 'Кечиресиз андай област жок'

    if message.text.lower() == 'chui':
        await bot.send_message(message.chat.id, chui)

        qr_code = pr.create(message.text)
        qr_code.png('img/code.png', scale=6)

        with open('img/code.png', 'rb') as foto:
            await bot.send_photo(message.chat.id, foto)
            await bot.send_message(message.chat.id, 'Сиздин qrcode даяр! Дагы текст жазсаныз болот!')

    elif message.text.lower() == 'talas':
        await bot.send_message(message.chat.id, talas)

        qr_code = pr.create(message.text)
        qr_code.png('img/code.png', scale=6)

        with open('img/code.png', 'rb') as foto:
            await bot.send_photo(message.chat.id, foto)
            await bot.send_message(message.chat.id, 'Сиздин qrcode даяр! Дагы текст жазсаныз болот!')

    elif message.text.lower() == 'yssykkul':
        await bot.send_message(message.chat.id, yssykkul)

        qr_code = pr.create(message.text)
        qr_code.png('img/code.png', scale=6)

        with open('img/code.png', 'rb') as foto:
            await bot.send_photo(message.chat.id, foto)
            await bot.send_message(message.chat.id, 'Сиздин qrcode даяр! Дагы текст жазсаныз болот!')

    elif message.text.lower() == 'naryn':
        await bot.send_message(message.chat.id, naryn)

        qr_code = pr.create(message.text)
        qr_code.png('img/code.png', scale=6)

        with open('img/code.png', 'rb') as foto:
            await bot.send_photo(message.chat.id, foto)
            await bot.send_message(message.chat.id, 'Сиздин qrcode даяр! Дагы текст жазсаныз болот!')

    elif message.text.lower() == 'osh':
        await bot.send_message(message.chat.id, osh)

        qr_code = pr.create(message.text)
        qr_code.png('img/code.png', scale=6)

        with open('img/code.png', 'rb') as foto:
            await bot.send_photo(message.chat.id, foto)
            await bot.send_message(message.chat.id, 'Сиздин qrcode даяр! Дагы текст жазсаныз болот!')

    elif message.text.lower() == 'jalal_abad':
        await bot.send_message(message.chat.id, jalal_abad)

        qr_code = pr.create(message.text)
        qr_code.png('img/code.png', scale=6)

        with open('img/code.png', 'rb') as foto:
            await bot.send_photo(message.chat.id, foto)
            await bot.send_message(message.chat.id, 'Сиздин qrcode даяр! Дагы текст жазсаныз болот!')

    elif message.text.lower() == 'batken':
        await bot.send_message(message.chat.id, batken)

        qr_code = pr.create(message.text)
        qr_code.png('img/code.png', scale=6)

        with open('img/code.png', 'rb') as foto:
            await bot.send_photo(message.chat.id, foto)
            await bot.send_message(message.chat.id, 'Сиздин qrcode даяр! Дагы текст жазсаныз болот!')

    else:
        await bot.send_message(message.chat.id, wrong)


if __name__ == '__main__':
    executor.start_polling(dp)

# @dp.message_handler()
# async def get_weather(message: types.Message):
#     code_to_smile = {
#         "Clear": "Аба ырайы ачык \U00002600",
#         "Clouds": "Булуттуу \U00002601",
#         "Rain": "Жамгыр \U00002614",
#         "Drizzle": "Жамгыр \U00002614",
#         "Thunderstorm": "Бороон \U000026A1",
#         "Snow": "Каар \U0001F328",
#         "Mist": "Тумандуу \U0001F32B"
#     }
#
#     try:
#         r = requests.get(
#             f"https://api.openweathermap.org/data/2.5/weather?lat={message.text}&appid={open_weather_token}&units=metric"
#         )
#         data = r.json()
#
#         city = data["name"]
#         cur_weather = data["main"]["temp"]
#
#         weather_description = data["weather"][0]["main"]
#         if weather_description in code_to_smile:
#             wd = code_to_smile[weather_description]
#         else:
#             wd = "Терезеден карачы, ал жакта аба ырайы кандай экенин түшүнбөйм!"
#
#         humidity = data["main"]["humidity"]
#         pressure = data["main"]["pressure"]
#         wind = data["wind"]["speed"]
#         sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
#         sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
#         length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
#             data["sys"]["sunrise"])
#
#         await message.reply(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
#                             f"Областтын аба ырайы: {city}\nТемпература: {cur_weather}C° {wd}\n"
#                             f"Нымдуулук: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind} м/с\n"
#                             f"Күндүн чыгышы: {sunrise_timestamp}\nКүндүн батышы: {sunset_timestamp}\nКүндүн узактыгы: {length_of_the_day}\n"
#                             f"***Күнүңүз куттуу болсун!***"
#                             )
#
#     except:
#         await message.reply("\U00002620 Областтын атын текшериңиз \U00002620")
#
#
