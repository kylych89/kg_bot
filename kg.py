from datetime import datetime
import requests
import datetime
from aiogram import Bot, Dispatcher, types, executor
import pyqrcode as pr

from config import TOKEN, open_weather_token

bot = Bot(TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply(
        f"Саламатсызбы {message.from_user.username} областтардын аба ырайын билуу учун областтын атын жазыныз!\n"
        f"Жана ар кандай тексти qrcode кылуу учун тексти томон жака жазыныз")


@dp.message_handler()
async def get_weather(message: types.Message):
    code_to_smile = {
        "Clear": "Аба ырайы ачык \U00002600",
        "Clouds": "Булуттуу \U00002601",
        "Rain": "Жамгыр \U00002614",
        "Drizzle": "Жамгыр \U00002614",
        "Thunderstorm": "Бороон \U000026A1",
        "Snow": "Каар \U0001F328",
        "Mist": "Тумандуу \U0001F32B"
    }

    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?lat={message.text}&appid={open_weather_token}&units=metric"
        )
        data = r.json()

        city = data["name"]
        cur_weather = data["main"]["temp"]

        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Терезеден карачы, ал жакта аба ырайы кандай экенин түшүнбөйм!"

        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
            data["sys"]["sunrise"])

        await message.reply(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
                            f"Областтын аба ырайы: {city}\nТемпература: {cur_weather}C° {wd}\n"
                            f"Нымдуулук: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind} м/с\n"
                            f"Күндүн чыгышы: {sunrise_timestamp}\nКүндүн батышы: {sunset_timestamp}\nКүндүн узактыгы: {length_of_the_day}\n"
                            f"***Күнүңүз куттуу болсун!***"
                            )

    except:
        await message.reply("\U00002620 Областтын атын текшериңиз \U00002620")


@dp.message_handler()
async def send_text_qr(message: types.Message):
    await message.answer('Сиздин жазган текст кабыл алынды куто турунуз!')

    qr_code = pr.create(message.text)
    qr_code.png('code.png', scale=6)

    with open('code.png', 'rb') as foto:
        await bot.send_photo(message.chat.id, foto)
        await bot.send_message(message.chat.id, 'Сиздин qrcode даяр! Дагы текст жазсаныз болот!')


if __name__ == '__main__':
    executor.start_polling(dp)

# async def get_time():
#     now = datetime.now()
#     current_time = now.strftime("%H:%M:%S")
#     await current_time
#
#
# async def get_date():
#     return date.today()
#
#
# async def get_markup():
#     markup = types.ReplyKeyboardMarkup(row_width=3)
#     itembtn1 = types.KeyboardButton('Салам')
#     itembtn2 = types.KeyboardButton('Cаaт канча болду?')
#     itembtn3 = types.KeyboardButton('Датаны корсот.')
#     markup.add(itembtn1, itembtn2, itembtn3)
#     return markup
#
#
# @dp.message_handler(commands=['start'])
# async def on_message(message: types.Message):
#     await bot.send_message(message.from_user.id, f'Hello, {message.from_user.username}')
#
#
#
#
#
# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)
