import uvicorn

from fastpace import app


def start():
    uvicorn.run(app, host="localhost", port=8000)


if __name__ == "__main__":
    start()
