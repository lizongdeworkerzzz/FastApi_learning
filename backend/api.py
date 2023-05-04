from fastapi import FastAPI, Request, APIRouter
from pydantic import BaseModel
from typing import Union
import subprocess

router = APIRouter(prefix="/wetest")


class Item(BaseModel):
    name: str
    desc: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


@router.post("/run")
async def run(strip: str, request: Request):
    res = {
        "method": request.method,
        "query": request.url.query,
        "query_params": request.query_params,
        "path_params": request.path_params,
        "body": await request.body(),
        "json": await request.json(),
    }
    return res


@router.get("/stop")
async def stop(q: int, p: str, request: Request):
    res = {
        "method": request.method,
        "query": request.url.query,
        "query_params": request.query_params,
        "path_params": request.path_params,
    }
    return res


@router.get("/disrupt")
async def disrupt(q: int, p: str, request: Request):
    res = {
        "method": request.method,
        "query": request.url.query,
        "query_params": request.query_params,
        "path_params": request.path_params,
    }
    return res
