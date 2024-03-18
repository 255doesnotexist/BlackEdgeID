# video_processor.py
import subprocess
from edge_detector import detect_black_edges
from storage_manager import update_video_info

def process_video(video_hash, video_content):
    """
    处理视频，提取帧，并进行黑边检测。
    """
    # 将视频内容保存到临时文件中
    temp_video_path = f"/tmp/{video_hash}.mp4"
    with open(temp_video_path, 'wb') as f:
        f.write(video_content)
    
    # 使用ffmpeg提取帧
    subprocess.run(["ffmpeg", "-i", temp_video_path, "-r", "1", f"/tmp/{video_hash}_%04d.png"])
    
    # 检测黑边
    black_edge_detected = detect_black_edges(temp_video_path)
    
    # 更新视频信息
    update_video_info(video_hash, black_edge_detected)
