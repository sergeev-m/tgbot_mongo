import asyncio

from src.bot.bot import bot_app
from src.core.log import log


async def main():
    try:
        await bot_app()
        log.info('Started app')
    except Exception as e:
        log.error(e)


if __name__ == "__main__":
    asyncio.run(main())
