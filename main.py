import sys
from pytube import YouTube
import time

# link = ''
link = 'http://youtube.com/watch?v=9bZkp7q19f0'
video = YouTube(link)
title = (video.title)

print(title)

time.sleep(3)
