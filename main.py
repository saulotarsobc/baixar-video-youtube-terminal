from pytube import YouTube
import requests
import sys

# link = ''
link = 'http://youtube.com/watch?v=9bZkp7q19f0'

video = YouTube(link)


title = (video.title)


for i in video.streams.get_by_resolution(144):
    print(i)
