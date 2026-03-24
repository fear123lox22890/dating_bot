import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# Токен будет браться из переменной окружения на хостинге
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    print("❌ Токен не найден! Добавьте BOT_TOKEN в переменные окружения")
    exit(1)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("👋 Привет! Бот работает на хостинге!")

async def main():
    print("🚀 Бот запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
