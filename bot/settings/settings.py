import os

from dotenv import load_dotenv


load_dotenv()

TELEGRAM_BOT_API_KEY: str | None = os.getenv("TELEGRAM_BOT_API_KEY", None)
if TELEGRAM_BOT_API_KEY is None:
    raise ValueError("TELEGRAM_BOT_API_KEY must be specified!")

__all__ = (
    "TELEGRAM_BOT_API_KEY",
)
