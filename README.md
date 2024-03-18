# BlackEdgeID 🎥🔍

## Introduction
**BlackEdgeID** is an advanced video processing tool designed to detect black edges in videos, thereby identifying improper aspect ratios. Utilizing cutting-edge image processing technology, this project offers a swift and reliable solution for content creators and media professionals.

## Features ❤️
- **Fast Uploads**: Built with FastAPI, the server-side can quickly receive uploaded video files.
- **Intelligent Detection**: Smartly identifies unsightly black edges by analyzing pixel changes over time in video frames.
- **Real-Time Queries**: Provides a real-time query interface, allowing users to check the video processing status and black edge detection results at any time.
- **Efficient Storage**: Employs Redis for efficient management of video files and processing results.

## Technology Stack 📝
- **FastAPI**: A modern, fast (high-performance) web framework for building APIs.
- **ffmpeg**: A powerful multimedia framework for processing video and audio files.
- **OpenCV**: An open-source computer vision library for image processing and video analysis.
- **Redis**: An in-memory data structure store, used as a database, cache, and message broker.

## Usage Examples 🪜
1. Upload a video:
   ```bash
   curl -X 'POST' \
     'http://127.0.0.1:8000/upload-video' \
     -H 'accept: application/json' \
     -H 'Content-Type: multipart/form-data' \
     -F 'file=@path_to_video.mp4;type=video/mp4'
    ```

2. Query a video:
   ```bash
    curl -X 'GET' \
    'http://127.0.0.1:8000/query-video/{video_hash}' \
    -H 'accept: application/json'
    ```