# main.py
from fastapi import FastAPI, File, UploadFile
from video_processor import process_video
from storage_manager import save_video_info, get_video_info
import hashlib
import uvicorn

app = FastAPI()

@app.post("/upload-video")
async def upload_video(file: UploadFile = File(...)):
    """
    接收上传的视频文件，生成哈希值作为唯一标识符，并将视频存储在服务器上。
    """
    video_content = await file.read()
    video_hash = hashlib.sha256(video_content).hexdigest()
    save_video_info(video_hash, video_content)
    process_video(video_hash, video_content)
    return {"hash": video_hash}

@app.get("/query-video/{video_hash}")
def query_video(video_hash: str):
    """
    接收视频的哈希值，返回视频处理状态和黑边检测结果。
    """
    video_info = get_video_info(video_hash)
    if video_info:
        return {
            "status": 200,
            "black_edge_detected": video_info['black_edge_detected'],
            "processed": video_info['processed']
        }
    else:
        return {"status": 404, "message": "Video not found"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
