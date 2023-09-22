from fastapi import APIRouter
from fastapi.responses import JSONResponse
from database.db import get_data_from_database
from router.sonolus.level_info import get_level_info

import json


with open("config.json", encoding="UTF-8") as file:
    config = json.load(file)

router = APIRouter()

@router.get("/sonolus/info")
async def server_info():
    headers = {"Sonolus-Version": config["Sonolus-Version"]}
    body = {}

    body["title"] = config["Server-Name"]
    body["banner"] = {
        "type":"ServerBanner",
        "url": config["Server-Banner-Path"]
    }  

    # levels
    lists = []
    level_info_list = get_data_from_database("20")
    for level_info in level_info_list:
        lists.append(get_level_info(level_info))
    body["levels"] = {
        "items": lists,
        "search": {}
    }
    body["skins"] = {
        "items": [],
        "search": {}
    }
    body["backgrounds"] = {
        "items": [],
        "search": {}
    }
    body["effects"] = {
        "items": [],
        "search": {}
    }
    body["particles"] = {
        "items": [],
        "search": {}
    }
    body["engines"] = {
        "items": [],
        "search": {}
    }

    return JSONResponse(body, headers=headers)