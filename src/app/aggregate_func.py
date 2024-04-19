import json

from aiogram import Router
from aiogram.types import Message

router = Router()


@router.message()
async def aggregate_handler(message: Message):
    data = json.loads(message.text)
    dt_from = data['dt_from']
    dt_upto = data['dt_upto']
    group_type = data['group_type']

    return dt_from, dt_upto, group_type


def setup_handlers() -> Router:
    return router
