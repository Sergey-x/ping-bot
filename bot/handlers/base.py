from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from keyboards.base import keyboard_base
from services.file_s import ChatIdsManager


router_base = Router()


@router_base.message(Command("start"))
async def cmd_start(message: Message):
    chat_id = message.chat.id
    await message.answer(
        text="Дарова!",
        reply_markup=keyboard_base,
    )
    await ChatIdsManager.add_id(chat_id)
