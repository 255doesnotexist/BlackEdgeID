# storage_manager.py
import redis

r = redis.Redis(host='localhost', port=6379, db=0)

def save_video_info(video_hash, video_content):
    """
    保存视频信息到Redis。
    """
    r.set(f"{video_hash}_content", video_content)
    r.set(f"{video_hash}_processed", False)
    r.set(f"{video_hash}_black_edge_detected", False)

def get_video_info(video_hash):
    """
    从Redis获取视频信息。
    """
    if r.exists(f"{video_hash}_content"):
        return {
            "processed": r.get(f"{video_hash}_processed"),
            "black_edge_detected": r.get(f"{video_hash}_black_edge_detected")
        }
    else:
        return None

def update_video_info(video_hash, black_edge_detected):
    """
    更新视频处理状态和黑边检测结果。
    """
    r.set(f"{video_hash}_processed", True)
    r.set(f"{video_hash}_black_edge_detected", black_edge_detected)
