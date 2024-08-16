from fastapi import FastAPI

from fastpace.conf.settings import Settings
from fastpace.dependency import Container
from fastpace.interfaces.routes import router

settings = Settings()
container = Container()
container.config.from_dict(settings.model_dump())

app = FastAPI(
    debug=settings.debug,
    title=settings.title,
    summary=settings.summary,
    description=settings.description,
    version=settings.version,
)
app.include_router(router)
