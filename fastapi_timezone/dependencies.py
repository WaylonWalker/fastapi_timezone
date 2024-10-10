# dependencies.py
from fastapi import Request
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError


async def get_timezone(request: Request):
    timezone = request.headers.get("X-Timezone",  request.cookies.get("timezone", "UTC"))
    try:
        timezone = ZoneInfo(timezone)
    except ZoneInfoNotFoundError:
        timezone = ZoneInfo('UTC')
    return timezone

