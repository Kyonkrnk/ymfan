def background_info(level_info):
    data = {
        "author": "きょん",
        "configuration": {
            "hash": "d6d0a3f33b1be72cf49c3e5fe7ef248ee8a0a5fa",
            "type": "BackgroundConfiguration",
            "url": "/assets/BackgroundConfiguration"
        },
        "data": {
            "hash": "adad592c5532a4faf64bcd56f6ef1ac65d783e1f",
            "type": "BackgroundData",
            "url": "/assets/BackgroundData"
        },
        "description": "Version: 1.0.0",
        "image": {
            "hash": level_info[13],
            "type": "BackgroundImage",
            "url": level_info[12]
        },
        "name": f"ymfan-bg-{level_info[0]}",
        "subtitle": "ymfan Background",
        "thumbnail": {
            "hash": level_info[9],
            "type": "BackgroundThumbnail",
            "url": level_info[8]
        },
        "title": level_info[1],
        "version": 2
    }
    return data