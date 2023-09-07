import uvicorn
from fastapi import FastAPI

from router.sonolus import info, levels
from router.assets import asset
from router.chart import upload, upload_form

app = FastAPI()
app.include_router(info.router)
app.include_router(levels.router)
app.include_router(asset.router)
app.include_router(upload_form.router)
app.include_router(upload.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run("main:app", port=80, host="192.168.0.10", reload=True)