from aiogram import Bot, Dispatcher
from app.handlers import router

import asyncio
import logging

token = "8013273281:AAFBBoazZwIiRaHahETkf8wUp4AxVIpaf3o"


bot = Bot(token = token)
dp = Dispatcher()

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

asyncio.run(main())
