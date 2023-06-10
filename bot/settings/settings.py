import os

from dotenv import load_dotenv


load_dotenv()

HOST_MEDIA: str | None = os.getenv("HOST_MEDIA", None)
if HOST_MEDIA is None:
    raise ValueError("HOST_MEDIA must be specified!")

HOST_SCHEDULE: str | None = os.getenv("HOST_SCHEDULE", None)
if HOST_SCHEDULE is None:
    raise ValueError("HOST_SCHEDULE must be specified!")

HOST_USER: str | None = os.getenv("HOST_USER", None)
if HOST_USER is None:
    raise ValueError("HOST_USER must be specified!")

HOST_JWT: str | None = os.getenv("HOST_JWT", None)
if HOST_JWT is None:
    raise ValueError("HOST_JWT must be specified!")

HOST_JWT_FILTER: str | None = os.getenv("HOST_JWT_FILTER", None)
if HOST_JWT_FILTER is None:
    raise ValueError("HOST_JWT_FILTER must be specified!")

TELEGRAM_BOT_API_KEY: str | None = os.getenv("TELEGRAM_BOT_API_KEY", None)
if TELEGRAM_BOT_API_KEY is None:
    raise ValueError("TELEGRAM_BOT_API_KEY must be specified!")

__all__ = (
    "TELEGRAM_BOT_API_KEY",
    "HOST_MEDIA",
    "HOST_SCHEDULE",
    "HOST_USER",
    "HOST_JWT",
    "HOST_JWT_FILTER",
)
