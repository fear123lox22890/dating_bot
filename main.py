import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

BOT_TOKEN = "7925155197:AAHsae10cg2J7It0DVv--tmdFN8eepTEmM0"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("✅ Бот работает! Привет из Сорокино!")

@dp.message(Command("help"))
async def help_cmd(message: types.Message):
    await message.answer("Команды:\n/start - приветствие\n/help - помощь")

async def main():
    print("🚀 Бот запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
