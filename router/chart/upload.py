from fastapi import APIRouter, Form, UploadFile, File
from router.chart.upload_s3 import upload_s3
from database.db import save_chart_info

from PIL import Image
from pydub import AudioSegment
import io
import os
import random, string
import datetime
import hashlib
import json
import requests

with open("config.json", encoding="utf-8") as f:
    config = json.load(f)


router = APIRouter()

@router.post("/up_chart")
async def upload_chart(
    title: str = Form(...),
    composer: str = Form(...),
    chart_author: str = Form(...),
    difficulty: int = Form(...),
    description: str = Form(...),
    bgm_file: UploadFile = File(...),
    jacket_file: UploadFile = File(...),
    chart_file: UploadFile = File(...),
):  
    # 譜面IDを決める(0-9,a-fからなる5文字)
    characters = string.digits + "abcdef"
    chart_id = ''.join(random.choice(characters) for _ in range(5))

    # bgm、ジャケット、譜面を変換してS3(R2)へアップロード
    bgm = await bgm_file.read()
    jacket = await jacket_file.read()
    chart = await chart_file.read()

    # 変換
    # bgm
    audio = AudioSegment.from_file(io.BytesIO(bgm))
    bgm = io.BytesIO()
    audio.export(bgm, format="mp3", bitrate="128k")
    bgm.seek(0)
    # ジャケット
    img = Image.open(io.BytesIO(jacket))
    img = img.convert('RGB').resize((500, 500))
    jacket = io.BytesIO()
    img.save(jacket, format='JPEG')
    jacket.seek(0)
    # 譜面
    url = config["convert_url"]
    response = requests.post(url, params={"chart_id": chart_id}, data=chart)
    chart = response.content

    # 背景画像を生成
    background_path = os.path.join("router", "chart", "bg", "background.png")
    ingame_img_path = os.path.join("router", "chart", "bg", "ingame_bg.png")
    background_image = Image.open(background_path)
    ingame_image = Image.open(ingame_img_path)
    jacket_image = Image.open(jacket).resize((450,450))
    background_image.paste(jacket_image, (730,168))
    background_image.paste(ingame_image, (0,0), ingame_image)
    background = io.BytesIO()
    background_image.save(background, format="PNG")
    background.seek(0)
    jacket.seek(0)

    # データ読み込み
    bgm = bgm.read()
    jacket = jacket.read()
    background = background.read()
    
    # アップロード
    upload_s3(content=bgm, path=f"ymfan/{chart_id}/bgm.mp3")
    upload_s3(content=jacket, path=f"ymfan/{chart_id}/jacket.jpg")
    upload_s3(content=chart, path=f"ymfan/{chart_id}/chart.gz")
    upload_s3(content=background, path=f"ymfan/{chart_id}/background.png")

    # sha1hashを計算
    bgm_hash = hashlib.sha1(bytes(bgm)).hexdigest()
    jacket_hash = hashlib.sha1(bytes(jacket)).hexdigest()
    chart_hash = hashlib.sha1(bytes(chart)).hexdigest()
    background_hash = hashlib.sha1(bytes(background)).hexdigest()
    
    # 曲のデータをデータベース上に保存
    save_chart_info(
        chart_id = chart_id,
        title = title,
        composer = composer,
        chart_author = chart_author,
        difficulty = difficulty,
        description = description,
        bgm_url = f"{config['S3_url']}/ymfan/{chart_id}/bgm.mp3",
        bgm_hash = bgm_hash,
        jacket_url = f"{config['S3_url']}/ymfan/{chart_id}/jacket.jpg",
        jacket_hash = jacket_hash,
        chart_url = f"{config['S3_url']}/ymfan/{chart_id}/chart.gz",
        chart_hash = chart_hash,
        background_url = f"{config['S3_url']}/ymfan/{chart_id}/background.png", 
        background_hash = background_hash,
        post_at = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9))).strftime('%Y-%m-%d %H:%M:%S'),
        update_at = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9))).strftime('%Y-%m-%d %H:%M:%S')
    )
