from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import FileResponse
import os
import yt_dlp as youtube_dl

app = FastAPI()

@app.get("/")
async def homepage():
    return FileResponse("frontend/templates/index.html")

@app.post("/download")
async def download_video(url: str = Form(...)):
    try:
        ydl_opts = {
            'format': 'best',
            'outtmpl': 'downloaded_video.mp4',
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        return FileResponse('downloaded_video.mp4', media_type='video/mp4', filename='downloaded_video.mp4')
    except Exception as e:
        print(f"Error: {str(e)}")
        raise HTTPException(status_code=400, detail=f"Error: Unable to download the video. Details: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
