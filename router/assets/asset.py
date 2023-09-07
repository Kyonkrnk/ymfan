from fastapi import APIRouter
from fastapi.responses import FileResponse

import os


router = APIRouter()

@router.get("/assets/{filepath}")
async def send_asset(filepath: str):
    path = os.path.join("router", "assets", "data", filepath)
    return FileResponse(path)