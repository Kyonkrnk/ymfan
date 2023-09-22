from router.item.background import background_info
from router.item.effect import effect_info
from router.item.particle import particle_info
from router.item.skin import skin_info
from router.item.engine import engine_info


def get_level_info(level_info):
    background = background_info(level_info)
    effect = effect_info(level_info)
    particle = particle_info(level_info)
    skin = skin_info(level_info)
    engine = engine_info(level_info, background, effect, particle, skin)
    data = {
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
        "preview": {
            "hash": level_info[7],
            "type": "LevelBgm",
            "url": level_info[6]
        },
        "description": level_info[5],
        "engine": engine,
        "name": f"ymfan-{level_info[0]}",
        "rating": int(level_info[4]),
        "title": level_info[1],
        "useBackground": {
            "item": background,
            "useDefault": False
            },
        "useEffect": {
            "item": effect,
            "useDefault": True
        },
        "useParticle": {
            "item": particle,
            "useDefault": True
        },
        "useSkin": {
            "item": skin,
            "useDefault": True
        },
        "version": 1
    }
    return data