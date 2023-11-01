from pathlib import Path
import sys

import sys
import os

BASE_PATH = Path(__file__).resolve().parent.parent

src_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'src'))
sys.path.append(src_dir)


from src.salaries.repozitory import salaries_repozitory
# from src.salaries.schemas import Document, AvgResponse, RequestData
# from src.bot.servise import start_app

# app = FastAPI()


# @app.get('/', response_model=list[Document])
# async def get_all():
#     res = await salaries_repozitory.get_all()
#     return res
#
#
# @app.get('/load')
# async def load():
#     return await salaries_repozitory.load_data()
#
#
# @app.post('/aggregate', response_model=AvgResponse)
# async def avg(data: RequestData):
#     return await salaries_repozitory.avg_by_date(data.model_dump())
#
#
# @app.get('/{pk}', response_model=Document)
# async def retrieve(pk: str):
#     return await salaries_repozitory.retrieve(pk)

import asyncio
from distutils.cmd import Command

from aiogram import Dispatcher, Bot, types, F, Router

from src.core.config.settings import settings



router = Router()


@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")


async def cmd_test(message: types.Message):
    await message.reply("ne Hello!")


@router.message(F.json)
async def cmd_arg(message: types.Message):
    await message.reply("ne Hello!")


async def main():
    bot = Bot(token=settings.BOT_TOKEN)
    dp = Dispatcher()
    dp.message.register(cmd_test, Command("test"))
    # await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

import uvicorn
if __name__ == "__main__":
    asyncio.run(main())
