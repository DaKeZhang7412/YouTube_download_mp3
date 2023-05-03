import os
from pydub import AudioSegment

# Set the directory path
dir_path = 'path/to/folder'

# Iterate over all files in the directory
for filename in os.listdir(dir_path):
    # Load the audio file and append it to the list
    audio = AudioSegment.from_file(os.path.join(dir_path, filename))
    
    # Set the bitrate to 128 kbps
    bitrate = "128k"

    # Export the audio as an MP3 file with the specified bitrate
    audio.export('output.mp3', format='mp3', bitrate=bitrate)

