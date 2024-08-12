from fastapi import FastAPI

from fastpace.conf.settings import Settings
from fastpace.routes import router

settings = Settings()

app = FastAPI(
    debug=settings.debug,
    title=settings.title,
    summary=settings.summary,
    description=settings.description,
    version=settings.version,
)
app.include_router(router)
