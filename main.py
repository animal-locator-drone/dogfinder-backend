from fastapi import FastAPI
from aiohttp import web

app = FastAPI()


@app.get("/")
async def root():
        return {"message": "Hello World"}


@app.get("/missions_available")
async def missions_available():
        return {
                "missions": [
                        {"id": "123", "name": "Path A", "path_preview": "TODO"}
                ]
        }


@app.post("/select_mission")
async def select_mission():
        return {"status": "Mission Started"}


@app.get("/mission_status")
async def mission_status():
        return {
                "status_info": {
                        "battery_percent": 69,
                        "time_elapsed": 200,
                        "current_location": [420.69, 69.420],
                        "time_remaining": 500,
                        "progress_percent": 69,
                }
        }


@app.get("/detections")
async def detections():
        return {
                "detections": [
                        {
                                "id": "1234",
                                "location": [123, 123],
                                "time": "timeUTC",
                                "images": [
                                        "www.link.to/image.png",
                                        "www.link.to/another_image.png"
                                ],
                        }
                ]
        }


@app.post("/abort_mission")
async def abort_mission():
        return {"status": "success"}
