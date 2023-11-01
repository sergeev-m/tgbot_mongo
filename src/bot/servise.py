from aiogram import Bot, Dispatcher, types

from src.core.config.settings import settings
import asyncio
from aiogram.filters.command import Command




from aiogram import Router
from aiogram.filters import CommandStart, StateFilter



def setup_handlers(dp: Dispatcher) -> None:
    dp.include_router(prepare_router())


async def setup_aiogram(dp: Dispatcher) -> None:
    # setup_logging(dp)
    # logger = dp["aiogram_logger"]
    # logger.debug("Configuring aiogram")
    # await create_db_connections(dp)
    setup_handlers(dp)
    # setup_middlewares(dp)
    # logger.info("Configured aiogram")


async def aiogram_on_startup_polling(dispatcher: Dispatcher, bot: Bot) -> None:
    await bot.delete_webhook(drop_pending_updates=True)
    await setup_aiogram(dispatcher)
    dispatcher["aiogram_logger"].info("Started polling")


async def aiogram_on_shutdown_polling(dispatcher: Dispatcher, bot: Bot) -> None:
    dispatcher["aiogram_logger"].debug("Stopping polling")
    await bot.session.close()
    await dispatcher.storage.close()
    dispatcher["aiogram_logger"].info("Stopped polling")


def start_app(dp):
    dp.startup.register(aiogram_on_startup_polling)
    dp.shutdown.register(aiogram_on_shutdown_polling)
    asyncio.run(dp.start_polling(bot))
