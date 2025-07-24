from aiogram import Bot, Dispatcher, executor, types
import pandas as pd
import os

TOKEN = "8100093485:AAE2DCxETIWOEXAXifLA0TpSAylG8I3en2g"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет, я бот! Напиши /list, чтобы увидеть данные.")

@dp.message_handler(commands=['list'])
async def send_list(message: types.Message):
    try:
        df = pd.read_csv('products.csv')
        if df.empty or 'name' not in df.columns or 'price' not in df.columns:
            await message.reply("Файл пустой или столбцы 'name' и 'price' не найдены.")
            return
        result = df[['name', 'price']].head()
        response = "Вот первые 5 товаров:\n\n"
        for index, row in result.iterrows():
            response += f"{row['name']}: {row['price']} руб.\n"
        await message.reply(response)
    except Exception as e:
        await message.reply(f"Ошибка: {str(e)}")
        
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
