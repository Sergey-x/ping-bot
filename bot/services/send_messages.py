from asyncio import sleep

from aiogram import Bot
from services.file_s import ChatIdsManager
from services.healthchecks import HEALTH_CHECKERS


async def check_services_continuously(bot: Bot):
    prev_status: bool = True

    while True:
        msg: str = "Состояние сервисов:\nЧИНИ БЫСТРЕЕ!\n"
        all_ok: bool = True

        for healthchecker in HEALTH_CHECKERS:
            check_result: tuple[str, bool] = await healthchecker.check()
            all_ok = all_ok and check_result[1]
            msg += f"{check_result[0]}\n"

        if all_ok and not prev_status:
            await send_all(bot, "Сервера снова живы - откисай, Чу!")

        if not all_ok:
            await send_all(bot, msg)

        prev_status = all_ok
        await sleep(300)


async def send_all(bot: Bot, msg: str):
    chat_ids: list[int] = await ChatIdsManager.get_from_file()
    for chat in chat_ids:
        await bot.send_message(chat_id=chat, text=msg)
        await sleep(.05)  # 20 messages per second (Limit: 30 messages per second)
