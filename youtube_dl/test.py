
import os
import youtube_dl

# Set the URL of the YouTube playlist
playlist_url = 'https://www.youtube.com/watch?v=IsoLRx_39bQ&list=PL_YKZKVmyNHh16FhvtHtir0TAqlTNFZJb'

# Set the output directory
output_dir = 'path/to/output/directory'

# Set the options for downloading the playlist
options = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '128',
    }],
    'outtmpl': os.path.join(output_dir, '%(autonumber)03d %(title)s.%(ext)s'),
}

# Download the playlist using youtube_dl
with youtube_dl.YoutubeDL(options) as ydl:
    ydl.download([playlist_url])