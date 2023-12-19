import os
import toml
from pathlib import Path
from pytube import YouTube
from pytube.cli import on_progress
import moviepy.editor as mp
from moviepy.video.fx.all import crop


def downloadvid():
    Path("./assets/backgrounds/video/").mkdir(parents=True, exist_ok=True)
    if Path(r".\assets\backgrounds\video\minecraft.mp4").is_file():
        print("background video already downloaded")
        return
    else:
        yt = YouTube(
            "https://www.youtube.com/watch?v=aUOBDL9bsYo",
            use_oauth=True,
            allow_oauth_cache=True,
            on_progress_callback=on_progress,
        )

        video_stream = yt.streams.get_highest_resolution()

        print(f"Downloading: {yt.title}...")
        video_stream.download(output_path="./assets/backgrounds/video/", filename="minecraft.mp4")
        print("Download complete!")
