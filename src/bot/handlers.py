from aiogram import Router
from aiogram.filters.command import Command
from aiogram.types import Message

from src.salaries.service import salary_service as ss
from src.salaries.schemas import RequestData
router = Router()


@router.message(Command('start'))
async def cmd_start(message: Message):
    await message.answer(
        "Hi <a href='%s'>%s</a>!" % (message.from_user.url, message.from_user.first_name),
        parse_mode='HTML'
    )


@router.message()
async def avg_by_date(message: Message):
    message_data = RequestData.parse_raw(message.text)
    try:
        res = await ss.avg_by_date(message_data)
        await message.answer(str(res))
    except Exception as e:
        await message.answer("Ошибка валидации данных", str(e))
