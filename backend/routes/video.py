from fastapi import APIRouter, UploadFile, File

router = APIRouter()

@router.post("/video")
async def upload_video(file: UploadFile = File(...)):
    return {
        "message": "Video received",
        "status": "Processing will be added later"
    }
