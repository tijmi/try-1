import getreddittop as redtop
import getaudiofile as aufile
import firsttime as ft
import backgroundvid as bg
import editvideo as ev
import cleanup as cl
import toml
from pathlib import Path
import re


def main():
    with open("config.toml", "r") as f:
        config = toml.load(f)

    if config["settings"]["firsttime"] == "yes":
        ft.firsttime

    bg.downloadvid()
    toppost = redtop.reddittop(config["preferances"]["subreddit"])
    aufile.tts(toppost[1], toppost[0])
    title = toppost[0]
    specialcharacters = r"(!?[^A-Za-z0-9 ])"
    title = re.sub(specialcharacters, " ", title)   
    title = title.replace(" ", "_")
    title = title.replace(".", "")
    print(title)
    ev.editvideo(   
        r".\assets\backgrounds\video\minecraft.mp4",
        rf".\assets\temp\{title}\audio\{title}.mp3",
        rf".\outputs\{title}.mp4",
        title,
    )
    if Path(rf".\outputs\{title}.mp4").is_file():
        cl.cleanup(title)
    

if __name__ == "__main__":
    main()
