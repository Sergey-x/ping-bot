from aiogram import Bot, Router
from aiogram.filters import Text
from aiogram.types import Message
from keyboards.base import BUTTON_HEALTHCHECK_TEXT, BUTTON_START_HEALTHCHECK_PROCESS_TEXT
from services.healthchecks import HEALTH_CHECKERS
from services.send_messages import check_services_continuously


router_healthcheck = Router()


@router_healthcheck.message(Text(text=BUTTON_HEALTHCHECK_TEXT, ignore_case=True))
async def get_services_status(message: Message):
    answer: str = "Состояние сервисов:\n"
    for healthchecker in HEALTH_CHECKERS:
        check_result = await healthchecker.check()
        answer += f"{check_result[0]}\n"
    await message.answer(
        text=answer,
    )


is_proc_running: bool = False


@router_healthcheck.message(Text(text=BUTTON_START_HEALTHCHECK_PROCESS_TEXT, ignore_case=True))
async def start_services_checking(message: Message, bot: Bot):
    global is_proc_running
    if is_proc_running:
        await message.answer(
            text="Уже работает",
        )
    else:

        await message.answer(
            text="Начинаю опрос серверов...\nЕсли что-то произойдет - сообщу",
        )
        is_proc_running = True
        await check_services_continuously(bot)
