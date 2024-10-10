# main.py
from datetime import datetime
from fastapi import Depends, FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi_timezone.dependencies import get_timezone
from zoneinfo import ZoneInfo

app = FastAPI()
templates = Jinja2Templates(directory="templates")


# def datetimeformat(value: datetime, timezone_str: str):
#     return value.astimezone(ZoneInfo(timezone_str)).strftime("%Y-%m-%d %H:%M:%S")

def datetimeformat(value: datetime, timezone_str: str):
    return value.astimezone(ZoneInfo(timezone_str)).strftime('%Y-%m-%d %-I:%M:%S %p')

templates.env.filters["datetimeformat"] = datetimeformat


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request, timezone: str = Depends(get_timezone)):
    # Fetch your data, ensuring datetimes are timezone-aware and in UTC
    data = {"event_time": datetime.now(timezone)}
    return templates.TemplateResponse(
        "index.html", {"request": request, "data": data, "timezone": timezone.key}
    )
@app.get("/event", response_class=HTMLResponse)
async def read_root(request: Request, timezone: str = Depends(get_timezone)):
    # Fetch your data, ensuring datetimes are timezone-aware and in UTC
    data = {"event_time": datetime.now(timezone)}
    return templates.TemplateResponse(
        "event.html", {"request": request, "data": data, "timezone": timezone.key}
    )
