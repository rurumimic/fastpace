from fastapi import FastAPI

app = FastAPI()


def create_app() -> FastAPI:
    return app


def start_app():
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)


@app.get("/")
async def Home():
    return {"greeting": "Hello, World!"}
