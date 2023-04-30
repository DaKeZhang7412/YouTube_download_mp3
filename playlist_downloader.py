from pytube import YouTube, Playlist
import os.path
import re

playlist = Playlist(str(input("Enter the URL of the video you want to download: \n>> ")))

print('Number of videos in playlist: %s' % len(playlist.video_urls))


print("Enter the destination (leave blank for current directory)")
destination = str(input(">> ")) or '.'
counter = 1

# physically downloading the audio track
for url in playlist.video_urls:
    print(url)
    # create YouTube Object
    yt = YouTube(url, use_oauth=True)

    # extract only audio
    audioStream = yt.streams.filter(only_audio=True).first()

    # check if the file exists.
    fn = str(counter) + " " + re.sub(r"[^a-zA-Z0-9 ]", "", audioStream.title) + '.mp3'
    counter += 1
    path = os.getcwd() + '\\' + fn
    if os.path.isfile(path):
        print(path + "File already exists!")
        continue     # if exists, jump to next link.
    else:
        # save the file
        out_file = audioStream.download(output_path=destination, filename = fn)

        # result of success
        print(fn + " has been successfully downloaded.")
