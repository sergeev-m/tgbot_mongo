from aiogram import Bot, Dispatcher

from src.core.config.settings import settings
from src.bot.handlers import router
from src.core.log import log


class BotApp:
    def __init__(self):
        self.bot = Bot(token=settings.BOT_TOKEN)
        self.dp = Dispatcher()

    async def __call__(self, *args, **kwargs):
        self.dp.startup.register(self.__aiogram_on_startup_polling)
        self.dp.shutdown.register(self.__aiogram_on_shutdown_polling)
        await self.dp.start_polling(self.bot)

    def __setup_handlers(self) -> None:
        self.dp.include_router(router)

    async def __setup_aiogram(self) -> None:
        self.__setup_handlers()
        log.info("Configured aiogram")

    async def __aiogram_on_startup_polling(self) -> None:
        await self.bot.delete_webhook(drop_pending_updates=True)
        await self.__setup_aiogram()
        log.info("Started polling")

    async def __aiogram_on_shutdown_polling(self) -> None:
        log.debug("Stopping polling")
        await self.bot.session.close()
        await self.dp.storage.close()
        log.info("Stopped polling")


bot_app = BotApp()
