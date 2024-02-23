from fastapi import FastAPI

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis
from starlette.staticfiles import StaticFiles

from app.config import settings
from app.users.router import router as users_router
from app.events.router import router as events_router
from app.tickets.router import router as tickets_router
from app.images.router import router as images_router

from app.pages.router import router as pages_router

app = FastAPI()

app.mount("/static", StaticFiles(directory='app/static'), name="static")

app.include_router(users_router)
app.include_router(events_router)
app.include_router(tickets_router)
app.include_router(pages_router)
app.include_router(images_router)


@app.on_event("startup")
async def startup():
    redis = aioredis.from_url(f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}",
                              encoding="utf-8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="cache")
