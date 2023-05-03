'''
    In the code above, we set the playlist_url variable to the URL of the YouTube playlist. We use the format and postprocessors options as shown in the previous answer to download the audio in MP3 format with a bitrate of 128k. We also use the outtmpl option with the %(title)s.%(ext)s format string to specify the output filename and path. This format string will include the title of the video followed by the file extension (.mp3).

    When you run this code, youtube_dl will download all the videos in the playlist and convert them to MP3 format with a bitrate of 128k. The output files will be saved in the same directory as the script. You can modify the options to suit your specific requirements, such as changing the output directory or the video format.
'''
import os
import youtube_dl

# Set the URL of the YouTube playlist
playlist_url = str(input("Enter the URL of the video you want to download: \n>> "))
#print('Number of videos in playlist: %s' % len(playlist_url.video_urls))

# Set the output directory
print("Enter the destination (leave blank for current directory)")
destination = str(input(">> ")) or '.'

# Set the options for downloading the playlist
options = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '128',
    }],
    'outtmpl': os.path.join(destination, '%(autonumber)03d %(title)s.%(ext)s'),
}

# Download the playlist using youtube_dl
with youtube_dl.YoutubeDL(options) as ydl:
    ydl.download([playlist_url])