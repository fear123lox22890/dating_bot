import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

BOT_TOKEN = os.getenv("7925155197:AAHsae10cg2J7It0DVv--tmdFN8eeptEMm0")

if not BOT_TOKEN:
    print("❌ Токен не найден!")
    exit(1)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("✅ Бот работает!")

async def main():
    print("🚀 Запуск...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
