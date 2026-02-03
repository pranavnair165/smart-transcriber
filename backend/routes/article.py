from fastapi import APIRouter

router = APIRouter()

@router.post("/article")
async def process_article(url: str):
    return {
        "url": url,
        "extracted_text": "Sample article content"
    }
