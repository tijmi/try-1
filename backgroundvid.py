import toml
from pathlib import Path
import pytube
from pytube.cli import on_progress
import json
import urllib.error


def downloadvid():
    with open("config.toml", "r") as f:
        config = toml.load(f)

    with open("background_videos.json", "r") as f:
        videos = json.load(f)

    background = config["settings"]["background"]
    url = videos[background]
    Path("./assets/backgrounds/video/").mkdir(parents=True, exist_ok=True)
    YouTube = pytube.YouTube
    if Path(rf".\assets\backgrounds\video\{background}.mp4").is_file():
        print("background video already downloaded")
        return
    else:
        try:
            yt = YouTube(
                url[0],
                use_oauth=True,
                allow_oauth_cache=True,
                on_progress_callback=on_progress,
            )

            video_stream = yt.streams.get_highest_resolution()

            print(f"Downloading: {yt.title}...")
            video_stream.download(
                output_path="./assets/backgrounds/video/", filename=f"{background}.mp4"
            )
            print("Download complete!")
        except urllib.error.URLError:
            raise RuntimeError('no ethernet connecton')
