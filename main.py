from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
import asyncio
import logging
from handlers.book import router as book_router


bot = Bot(BOT_TOKEN)
dp = Dispatcher()


async def main():
    logging.basicConfig(level=logging.INFO)
    dp.include_router(book_router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())