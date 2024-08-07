from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def Home():
    return {"greeting": "Hello, World!"}
