from aiogram import Bot, Dispatcher

from src.core.config.settings import settings
from src.bot.handlers import router
from src.core.log import log


def setup_handlers(dp: Dispatcher) -> None:
    dp.include_router(router)


async def setup_aiogram(dp: Dispatcher) -> None:
    setup_handlers(dp)
    log.info("Configured aiogram")


async def aiogram_on_startup_polling(dispatcher: Dispatcher, bot: Bot) -> None:
    await bot.delete_webhook(drop_pending_updates=True)
    await setup_aiogram(dispatcher)
    log.info("Started polling")


async def aiogram_on_shutdown_polling(dispatcher: Dispatcher, bot: Bot) -> None:
    log.debug("Stopping polling")
    await bot.session.close()
    await dispatcher.storage.close()
    log.info("Stopped polling")


async def start_app():
    bot = Bot(token=settings.BOT_TOKEN)
    dp = Dispatcher()
    dp.startup.register(aiogram_on_startup_polling)
    dp.shutdown.register(aiogram_on_shutdown_polling)
    await dp.start_polling(bot)
    return dp
