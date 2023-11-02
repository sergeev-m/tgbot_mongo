import asyncio

from src.bot.bot import start_app
from src.core.log import log


async def main():
    try:
        log.info('Started app')
        return await start_app()
    except Exception as e:
        log.error(e)


if __name__ == "__main__":
    asyncio.run(main())
