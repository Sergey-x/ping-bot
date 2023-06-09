import asyncio
import logging

from aiogram import Bot, Dispatcher
from handlers.base import router_base
from handlers.healthcheck import router_healthcheck
from settings.settings import TELEGRAM_BOT_API_KEY


# Configure logging
logging.basicConfig(level=logging.INFO)


# Запуск бота
async def main():
    bot: Bot = Bot(token=TELEGRAM_BOT_API_KEY)

    dp = Dispatcher()

    dp.include_routers(router_base, router_healthcheck)

    # Запускаем бота и пропускаем все накопленные входящие
    # Да, этот метод можно вызвать даже если у вас поллинг
    await bot.delete_webhook(drop_pending_updates=True)

    print("start bot")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
