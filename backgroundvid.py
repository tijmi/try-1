import os
from pytube import YouTube
import toml

def downloadvid():
    try:
        yt = YouTube(video_url)
        video_title = yt.title
        video_stream = yt.streams.filter(file_extension='mp4', res='720p').first()
        output_file_path = os.path.join(output_path, f"{video_title}.mp4")
        print(f"Downloading '{video_title}'...")
        video_stream.download(output_path)
        print(f"Video downloaded successfully to '{output_file_path}'.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")