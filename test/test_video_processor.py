# test/test_video_processor.py
import unittest
from storage_manager import get_video_info
from video_processor import process_video

from asyncio import aiofiles
import hashlib

class TestVideoProcessor(unittest.TestCase):
    async def test_process_video(self):
        """
        测试视频处理功能。
        """
        # 这里应该添加测试用例和断言

        video_example = "./got_black_edge.mp4"
        async with aiofiles.open(video_example, mode='rb') as f:
            video_content = await f.read()
        video_hash = hashlib.sha256(video_content).hexdigest()

        processed = False
        while processed != True:
            get_video_info(video_hash).processed

        assert get_video_info(video_hash).black_edge_detected == True
        pass

if __name__ == '__main__':
    unittest.main()
