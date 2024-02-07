import getreddittop as redtop
import getaudiofile as aufile
import backgroundvid as bg
import editvideo as ev
import cleanup as cl
import toml
from pathlib import Path
import re
from textwrap import TextWrapper
import ttsvoices.longstring as ls
import checkwifi
import checkconfig 


def main() -> None:
    with open("config.toml", "r") as f:
        config = toml.load(f)

    # checkwifi.internet_connection()
    cehckconfig = checkconfig.validation()
    cehckconfig.validatetoml()
    bg.downloadvid()
    toppost = redtop.reddittop()
    title = toppost[0]
    title = ls.preparetitle(title)

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
