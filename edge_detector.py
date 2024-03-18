# edge_detector.py
import cv2
import numpy as np

def detect_black_edges(video_path):
    """
    检测视频黑边。计算中心像素与边缘像素随时间的变化量。
    """
    # 读取视频
    cap = cv2.VideoCapture(video_path)
    frames_variance = []
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # 转换为灰度图像
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # 获取中心像素和边缘像素
        center_pixel = gray_frame[gray_frame.shape[0] // 2, gray_frame.shape[1] // 2]
        edge_pixel = gray_frame[0, 0]
        
        # 计算变化量
        frames_variance.append((center_pixel - edge_pixel)**2)
    
    cap.release()
    
    # 计算方差
    variance = np.var(frames_variance)
    
    # 如果方差小于某个阈值，则认为检测到黑边
    return variance < 10  # 假设阈值
