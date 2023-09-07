from fastapi import APIRouter
from fastapi.responses import FileResponse

import os


router = APIRouter()

@router.get("/upload")
async def send_form():
    path = os.path.join("static", "upload", "index.html")
    return FileResponse(path)

@router.get("/upload/{filename}")
async def send_script_css(filename: str):
    path = os.path.join("static", "upload", filename)
    return FileResponse(path)