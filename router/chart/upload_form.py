from fastapi import APIRouter
from fastapi.responses import FileResponse

import os


router = APIRouter()

@router.get("/up_chart")
async def send_form():
    path = os.path.join("static", "up_chart", "index.html")
    return FileResponse(path)

@router.get("/up_chart/{filename}")
async def send_script_css(filename: str):
    path = os.path.join("static", "up_chart", filename)
    return FileResponse(path)