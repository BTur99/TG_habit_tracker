import asyncio
import logging

from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers import user
from database.database import init_db

async def main():
    logging.basicConfig(level=logging.INFO)
    
    # Инициализация базы данных
    await init_db()
    
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    
    # Подключаем роутеры
    dp.include_router(user.router)
    
    logging.info("Бот запущен!")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот остановлен")