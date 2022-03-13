import sys
from pytube import YouTube
import time

# link = ''
url = 'http://youtube.com/watch?v=9bZkp7q19f0'

def get_video_info():
    ptvideo = YouTube(url)

video = YouTube(link)
title = (video.title)

print(title)

time.sleep(3)
