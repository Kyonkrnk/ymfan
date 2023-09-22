from fastapi import APIRouter
from fastapi.responses import JSONResponse

from database.db import get_leveldata_from_database

from router.sonolus.level_info import get_level_info


router = APIRouter()

@router.get("/sonolus/levels/{chart_id}")
async def levelinfo(chart_id: str):
    level_info = get_leveldata_from_database(chart_id[6:])
    data = get_level_info(level_info)
    data = {
        "item": data
    }
    return JSONResponse(data)