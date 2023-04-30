from pytube import YouTube, Playlist
from pytube.helpers import safe_filename
import os
import re

playlist = Playlist('https://www.youtube.com/watch?v=4OQMaz8rPtw&list=PLuLxx7vzE6Hk0EUh7k9K7d5dN62h-grAG')

print("Enter the destination (leave blank for current directory)")
destination = str(input(">> ")) or ''
counter = 1
# physically downloading the audio track
for url in playlist.video_urls:
    print(url)
    # create YouTube Object
    yt = YouTube(url, use_oauth=True)

    # extract only audio
    audioStream = yt.streams.filter(only_audio=True).first()

    # check if the file exists.
    fn = str(counter) + " " + safe_filename(audioStream.title) + '.mp3'
    counter += 1
    path = os.getcwd() + '\\' + fn
    if os.path.isfile(path):
        print("skipped")
        continue     # if exists, jump to next link.
    else:
        # save the file
        out_file = audioStream.download(output_path=destination, filename = fn)

        # result of success
        print(fn + " has been successfully downloaded.")


