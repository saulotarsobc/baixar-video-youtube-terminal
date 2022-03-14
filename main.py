import sys
from pytube import YouTube
import time
import pafy


def get_video_info(url):
    try:
        ptvideo = YouTube(url)
        pfvideo = pafy.new(url)
        print(ptvideo.title)
    except Exception as e:
        msg = f'Erro: {e}\n'
        sys.exit(msg)


def download_video(url):
    ptvideo = YouTube(url, on_progress_callback=progress)\
        .streams\
        .filter(file_extension='mp4', resolution='720p', progressive=True)\
        .first()\
        .download()
    # .download('Baixando/') # Define o diretório destino


def progress(stream, chunck, bytes_remaining):
    filesize = stream.filesize
    current = ((filesize - bytes_remaining)/filesize)
    percent = ('{0:.1f}').format(current*100)
    progress = int(50*current)
    status = '█' * progress + '-' * (50 - progress)
    sys.stdout.write(' ↳ |{bar}| {percent}%\r'.format(
        bar=status, percent=percent))
    sys.stdout.flush()


# url = 'http://youtube.com/watch?v=9bZkp7q19f0'
url = ''
while url == '':
    url = input('URL do video: ')

get_video_info(url)
download_video(url)

time.sleep(3)
