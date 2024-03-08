from aiogram import Dispatcher, Bot
from core.settings import settings
from core.handlers.basic import *
from core.utils.commands import set_commands
import asyncio
import logging


async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(settings.bots.admin_token, text='Бот запущен')


async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_token, text='Бот остановлен')


async def start():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - [%(levelname)s] - %(name)s - '
                                                   '(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s')
    bot = Bot(settings.bots.bot_token, parse_mode='HTML')

    dp = Dispatcher()

    # Не забудь первый написать боту!

    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())
