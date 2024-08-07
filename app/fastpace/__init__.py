from fastapi import FastAPI

from fastpace.routes import router

app = FastAPI()
app.include_router(router)
