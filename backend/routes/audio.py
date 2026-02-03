from fastapi import APIRouter, UploadFile, File

router = APIRouter()

@router.post("/audio")
async def transcribe_audio(file: UploadFile = File(...)):
    return {
        "message": "Audio received",
        "transcription": "Sample transcribed text..."
    }
