import asyncio
from aiogram import Dispatcher, Bot

from bot.utils import setup_logger

from typing import cast

import os
from dotenv import load_dotenv

from bot.handlers import (start, verify)

setup_logger()
load_dotenv()

TOKEN_BOT = os.getenv('TOKEN_BOT')
DATABASE_URL = os.getenv('DATABASE_URL')

bot = Bot(token=cast(str, TOKEN_BOT))
dp = Dispatcher()

routers = (
    start.router,
    verify.router,
)


async def main():
    for r in routers:
        dp.include_router(r)

    await dp.start_polling(
        bot
    )

if __name__ == '__main__':
    asyncio.run(main())
