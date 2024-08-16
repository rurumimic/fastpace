from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, Request

from fastpace.applications.services import Service
from fastpace.dependency import Container

router = APIRouter()


@router.get("/")
async def home():
    return {"greeting": "Hello, World!"}


@router.get("/state")
@inject
async def state(
    request: Request,
    service: Service = Depends(Provide[Container.services.service]),
    config: dict = Depends(Provide[Container.config]),
):
    return service.state()
