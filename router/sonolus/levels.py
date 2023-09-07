from fastapi import APIRouter
from fastapi.responses import JSONResponse
from database.db import get_leveldata_from_database


router = APIRouter()

@router.get("/sonolus/levels/{chart_id}")
async def levelinfo(chart_id: str):
    level_info = get_leveldata_from_database(chart_id[6:])
    data = {
        "description": level_info[5],
        "item": {
            "artists": level_info[2],
            "author": level_info[3],
            "bgm": {
                "hash": level_info[7],
                "type": "LevelBgm",
                "url": level_info[6]
            },
            "cover": {
                "hash": level_info[9],
                "type": "LevelCover",
                "url": level_info[8]
            },
            "data": {
                "hash": level_info[11],
                "type": "LevelData",
                "url": level_info[10]
            },
            "description": level_info[5],
            "engine": {
                "author": "LittleYang0531",
                "background": {
                    "author": "World Dai Star: Dream's Stellarium",
                    "configuration": {
                        "hash": "d6d0a3f33b1be72cf49c3e5fe7ef248ee8a0a5fa",
                        "type": "BackgroundConfiguration",
                        "url": "http://8.130.81.127:8000/data/d6d0a3f33b1be72cf49c3e5fe7ef248ee8a0a5fa"
                    },
                    "data": {
                        "hash": "adad592c5532a4faf64bcd56f6ef1ac65d783e1f",
                        "type": "BackgroundData",
                        "url": "http://8.130.81.127:8000/data/adad592c5532a4faf64bcd56f6ef1ac65d783e1f"
                    },
                    "description": "",
                    "image": {
                        "hash": "83e331c59146c674d5c3d6ed56ba5ac69ecca06a",
                        "type": "BackgroundImage",
                        "url": "http://8.130.81.127:8000/data/83e331c59146c674d5c3d6ed56ba5ac69ecca06a"
                    },
                    "name": "sirius-default",
                    "subtitle": "World Dai Star: Dream's Stellarium",
                    "thumbnail": {
                        "hash": "4d84f6ea99c28b7787161f012b353baf4c1752e7",
                        "type": "BackgroundThumbnail",
                        "url": "http://8.130.81.127:8000/data/4d84f6ea99c28b7787161f012b353baf4c1752e7"
                    },
                    "title": "Sirius Default",
                    "version": 2
                },
                "configuration": {
                    "hash": "b83d6e65e91fde752ea2f1b9fa875bfa939d7888",
                    "type": "EngineConfiguration",
                    "url": "http://8.130.81.127:8000/data/b83d6e65e91fde752ea2f1b9fa875bfa939d7888"
                },
                "data": {
                    "hash": "1a3bd2b6bdcd766dca9bf605bf00e348d9808680",
                    "type": "EngineData",
                    "url": "http://8.130.81.127:8000/data/1a3bd2b6bdcd766dca9bf605bf00e348d9808680"
                },
                "description": "A recreation of World Dai Star: Dream's Stellarium engine in Sonolus.\nVersion: 1.0.0.20230903_beta\n\nGithub Repository\nhttps://github.com/SonolusHaniwa/sonolus-sirius-engine",
                "effect": {
                    "audio": {
                        "hash": "fb615f16acdbf1f70bdf4253f665ec5d67e51e1c",
                        "type": "EffectAudio",
                        "url": "http://8.130.81.127:8000/data/fb615f16acdbf1f70bdf4253f665ec5d67e51e1c"
                    },
                    "author": "LittleYang0531",
                    "data": {
                        "hash": "c5809b0d0f595655d669bf2d67cab30ce6bafdb5",
                        "type": "EffectData",
                        "url": "http://8.130.81.127:8000/data/c5809b0d0f595655d669bf2d67cab30ce6bafdb5"
                    },
                    "description": "",
                    "name": "sirius",
                    "subtitle": "World Dai Star: Dream's Stellarium",
                    "thumbnail": {
                        "hash": "4d84f6ea99c28b7787161f012b353baf4c1752e7",
                        "type": "EffectThumbnail",
                        "url": "http://8.130.81.127:8000/data/4d84f6ea99c28b7787161f012b353baf4c1752e7"
                    },
                    "title": "Sirius",
                    "version": 5
                },
                "name": "sirius",
                "particle": {
                    "author": "Burrito",
                    "data": {
                        "hash": "3d6c06680612cb880c8552672ac2999cfaeb49a8",
                        "type": "ParticleData",
                        "url": "http://8.130.81.127:8000/data/3d6c06680612cb880c8552672ac2999cfaeb49a8"
                    },
                    "description": "",
                    "name": "pjsekai",
                    "subtitle": "世界计划 彩色舞台",
                    "texture": {
                        "hash": "57b4bd504f814150dea87b41f39c2c7a63f29518",
                        "type": "ParticleTexture",
                        "url": "http://8.130.81.127:8000/data/57b4bd504f814150dea87b41f39c2c7a63f29518"
                    },
                    "thumbnail": {
                        "hash": "e5f439916eac9bbd316276e20aed999993653560",
                        "type": "ParticleThumbnail",
                        "url": "http://8.130.81.127:8000/data/e5f439916eac9bbd316276e20aed999993653560"
                    },
                    "title": "世界计划",
                    "version": 2
                },
                "playData": {
                    "hash": "1a3bd2b6bdcd766dca9bf605bf00e348d9808680",
                    "type": "EnginePlayData",
                    "url": "http://8.130.81.127:8000/data/1a3bd2b6bdcd766dca9bf605bf00e348d9808680"
                },
                "skin": {
                    "author": "LittleYang0531",
                    "data": {
                        "hash": "bb86d7cc9c0c8f00e51bf62e813b2857ac35807d",
                        "type": "SkinData",
                        "url": "http://8.130.81.127:8000/data/bb86d7cc9c0c8f00e51bf62e813b2857ac35807d"
                    },
                    "description": "",
                    "name": "sirius",
                    "subtitle": "World Dai Star: Dream's Stellarium",
                    "texture": {
                        "hash": "120939a9227e1890aea388d560a976af5739c82d",
                        "type": "SkinTexture",
                        "url": "http://8.130.81.127:8000/data/120939a9227e1890aea388d560a976af5739c82d"
                    },
                    "thumbnail": {
                        "hash": "4d84f6ea99c28b7787161f012b353baf4c1752e7",
                        "type": "SkinThumbnail",
                        "url": "http://8.130.81.127:8000/data/4d84f6ea99c28b7787161f012b353baf4c1752e7"
                    },
                    "title": "Sirius",
                    "version": 3
                },
                "subtitle": "World Dai Star: Dream's Stellarium",
                "thumbnail": {
                    "hash": "4d84f6ea99c28b7787161f012b353baf4c1752e7",
                    "type": "EngineThumbnail",
                    "url": "http://8.130.81.127:8000/data/4d84f6ea99c28b7787161f012b353baf4c1752e7"
                },
                "title": "Sirius",
                "tutorialData": {
                    "hash": "0a00ae6b688d19af9e8394e67c2df3236ecdb5e1",
                    "type": "EngineTutorialData",
                    "url": "http://8.130.81.127:8000/data/0a00ae6b688d19af9e8394e67c2df3236ecdb5e1"
                },
                "version": 9
            },
            "name": f"ymfan-{level_info[0]}",
            "preview": {
                "hash": level_info[7],
                "type": "LevelBgm",
                "url": level_info[6]
            },
            "rating": int(level_info[4]),
            "title": level_info[1],
            "useBackground": {
            "item": {
                "author": "ワールドダイスター 夢のステラリウム",
                "configuration": {
                    "hash": "d6d0a3f33b1be72cf49c3e5fe7ef248ee8a0a5fa",
                    "type": "BackgroundConfiguration",
                    "url": "http://8.130.81.127:8000/data/d6d0a3f33b1be72cf49c3e5fe7ef248ee8a0a5fa"
                },
                "data": {
                    "hash": "adad592c5532a4faf64bcd56f6ef1ac65d783e1f",
                    "type": "BackgroundData",
                    "url": "http://8.130.81.127:8000/data/adad592c5532a4faf64bcd56f6ef1ac65d783e1f"
                },
                "description": "Version: 1.0.0",
                "image": {
                    "hash": "975870ced76d888fcc2e0dbabcca4497931b4772",
                    "type": "BackgroundImage",
                    "url": "http://8.130.81.127:8000/data/975870ced76d888fcc2e0dbabcca4497931b4772"
                },
                "name": "sirius-60",
                "subtitle": "与那国緋花里、阿伎留カミラ",
                "thumbnail": {
                    "hash": "6a03a3b3583e6e6e3003d10692e8bfa4b3876909",
                    "type": "BackgroundThumbnail",
                    "url": "http://8.130.81.127:8000/data/6a03a3b3583e6e6e3003d10692e8bfa4b3876909"
                },
                "title": "シル・ヴ・プレジデント",
                "version": 2
            },
            "useDefault": False
            },
            "useEffect": {
                "item": {
                    "audio": {
                        "hash": "",
                        "type": "EffectAudio",
                        "url": ""
                    },
                    "author": "",
                    "data": {
                        "hash": "",
                        "type": "EffectData",
                        "url": ""
                    },
                    "description": "",
                    "name": "",
                    "subtitle": "",
                    "thumbnail": {
                        "hash": "",
                        "type": "EffectThumbnail",
                        "url": ""
                    },
                    "title": "",
                    "version": 5
                },
                "useDefault": True
            },
            "useParticle": {
                "item": {
                    "author": "",
                    "data": {
                        "hash": "",
                        "type": "ParticleData",
                        "url": ""
                    },
                    "description": "",
                    "name": "",
                    "subtitle": "",
                    "texture": {
                        "hash": "",
                        "type": "ParticleTexture",
                        "url": ""
                    },
                    "thumbnail": {
                        "hash": "",
                        "type": "ParticleThumbnail",
                        "url": ""
                    },
                    "title": "",
                    "version": 2
                },
                "useDefault": True
            },
            "useSkin": {
                "item": {
                    "author": "",
                    "data": {
                        "hash": "",
                        "type": "SkinData",
                        "url": ""
                    },
                    "description": "",
                    "name": "",
                    "subtitle": "",
                    "texture": {
                        "hash": "",
                        "type": "SkinTexture",
                        "url": ""
                    },
                    "thumbnail": {
                        "hash": "",
                        "type": "SkinThumbnail",
                        "url": ""
                    },
                    "title": "",
                    "version": 3
                },
                "useDefault": True
            },
            "version": 1
        }
    }
    return JSONResponse(data)