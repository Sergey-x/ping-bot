import aiohttp
from settings.settings import HOST_JWT, HOST_JWT_FILTER, HOST_MEDIA, HOST_SCHEDULE, HOST_USER


class BaseHealthcheck:
    healthcheck_url: str = None
    service_name: str = None

    @classmethod
    async def _get_healthcheck_result(cls) -> bool:
        if cls.healthcheck_url is None:
            raise ValueError("`healthcheck_url` is not defined")

        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(cls.healthcheck_url) as resp:
                    if resp.status < 500:
                        return True
                    return False
            except:  # noqa
                return False

    @classmethod
    async def check(cls) -> tuple[str, bool]:
        is_alive: bool = await cls._get_healthcheck_result()

        return f"{'✅' if is_alive else '❌'} {cls.service_name}", is_alive


class FileServiceHealthcheck(BaseHealthcheck):
    healthcheck_url = HOST_MEDIA
    service_name = "Media"


class ScheduleServiceHealthcheck(BaseHealthcheck):
    healthcheck_url = HOST_SCHEDULE
    service_name = "Schedule"


class UserServiceHealthcheck(BaseHealthcheck):
    healthcheck_url = HOST_USER
    service_name = "User"


class JWTServiceHealthcheck(BaseHealthcheck):
    healthcheck_url = HOST_JWT
    service_name = "JWT"


class JWTFilterServiceHealthcheck(BaseHealthcheck):
    healthcheck_url = HOST_JWT_FILTER
    service_name = "JWT-Filter"


HEALTH_CHECKERS = (
    FileServiceHealthcheck,
    ScheduleServiceHealthcheck,
    UserServiceHealthcheck,
    JWTServiceHealthcheck,
    JWTFilterServiceHealthcheck,
)
