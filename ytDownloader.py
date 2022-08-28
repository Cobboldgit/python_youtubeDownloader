from pytube import YouTube
from sys import argv
import os
from pathlib import Path


def downloader(video_link, saveTo=None):
    try:
        videoLink = YouTube(video_link)
        title = str(videoLink.title)
        print('Preparing to download ' + title)
        video = videoLink.streams.filter(
            progressive=True, file_extension='mp4').first()
      
        if saveTo is not None:
            video.download(saveTo)
        else:
            video.download()
        print('Download completed 😊 ' + title)
    except Exception as e:
        print("ErrorDownloadVideo | " + str(video_link))
        print(e)


link = None
folderPath = os.path.join(Path.home(), 'Downloads')

try:
    link = argv[1]
    downloader(link, folderPath)
except Exception as e:
    print("""try this instead: ytDownloader URL""")


# https://www.youtube.com/watch?v=W5dmuKO2BSI
