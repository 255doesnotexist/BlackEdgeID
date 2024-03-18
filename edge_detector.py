# edge_detector.py
import cv2
import numpy as np

def detect_black_edges(video_path):
    """
    使用Canny算法检测视频黑边。
    """
    # 读取视频
    cap = cv2.VideoCapture(video_path)
    black_edge_detected = False
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # 应用Canny边缘检测算法
        edges = cv2.Canny(frame, 100, 200)
        
        # 分析边缘检测结果
        if np.mean(edges) < 10:  # 假设阈值
            black_edge_detected = True
            break
    
    cap.release()
    return black_edge_detected
