import getreddittop as redtop
import getaudiofile as aufile
import firsttime as ft
import backgroundvid as bg
import editvideo as ev
import cleanup as cl
import toml
from pathlib import Path
import re
from textwrap import TextWrapper


def main() -> None:
    with open("config.toml", "r") as f:
        config = toml.load(f)

    if config["settings"]["firsttime"] == "yes":
        ft.firsttime

    bg.downloadvid()
    toppost = redtop.reddittop(config["preferances"]["subreddit"])
    title = toppost[0]
    specialcharacters = r"(!?[^A-Za-z0-9 ])"
    title = re.sub(specialcharacters, "", title)
    title = title.replace(" ", "_")
    title = title.replace(".", "")
    w = TextWrapper(30, break_long_words=True)
    title = w.wrap(title)

    print(title[0])
    aufile.tts(toppost[1], toppost[0], title[0])
    ev.finalvideo(
        rf".\assets\temp\{title[0]}\audio\{title[0]}.mp3",
        rf".\outputs\{title[0]}.mp4",
        title[0],
    )
    if Path(rf".\outputs\{title[0]}.mp4").is_file():
        cl.cleanup(title[0])


if __name__ == "__main__":
    main()
