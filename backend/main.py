from fastapi import FastAPI 
from backend.routes import audio, video, article

app=FastAPI()
app.include_router(audio.router)
app.include_router(video.router)
app.include_router(article.router)

@app.get("/")

def root():
    return{"message":"Backend is running!"}
