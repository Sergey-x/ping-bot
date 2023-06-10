import json

import aiofiles


FILENAME: str = "chat_ids.txt"


class ChatIdsManager:
    @classmethod
    async def get_from_file(cls) -> list[int]:
        async with aiofiles.open(FILENAME, "r") as f:
            chat_ids: list[int] = json.loads(await f.read())
        return chat_ids

    @classmethod
    async def write_to_file(cls, chat_ids: list[int]) -> None:
        unique_ids: list[int] = list(set(chat_ids))
        async with aiofiles.open(FILENAME, "w") as f:
            chat_ids_str: str = json.dumps(unique_ids)
            await f.write(chat_ids_str)
        return

    @classmethod
    async def add_id(cls, chat_id: int) -> None:
        chat_ids: list[int] = await cls.get_from_file()
        chat_ids.append(chat_id)
        await cls.write_to_file(chat_ids)
