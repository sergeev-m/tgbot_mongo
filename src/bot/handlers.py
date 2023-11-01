import json

from aiogram import Router
from aiogram.filters.command import Command
from aiogram.types import Message
from pydantic import ValidationError

from src.salaries.service import salary_service as ss
from src.salaries.schemas import RequestData
from src.core.log import log
from src.core.config.settings import settings


router = Router()


@router.message(Command('start'))
async def cmd_start(message: Message):
    await message.answer(
        "Hi <a href='%s'>%s</a>!" % (message.from_user.url, message.from_user.first_name),
        parse_mode='HTML'
    )


@router.message()
async def avg_by_date(message: Message):
    try:
        message_data = RequestData.parse_raw(message.text)
        res = await ss.avg_by_date(message_data)
        res = json.dumps(res)

        if len(res) > settings.MAX_LENGTH_MESSAGE:
            for i in range(0, len(res), settings.MAX_LENGTH_MESSAGE):
                await message.answer(res[i:i + settings.MAX_LENGTH_MESSAGE])
        else:
            await message.answer(res)
    except ValidationError:
        await message.answer('Невалидный запрос. Пример запроса: {"dt_from": "2022-09-01T00:00:00",\
         "dt_upto": "2022-12-31T23:59:00", "group_type": "month"}')
    except Exception as e:
        log.error(e)
