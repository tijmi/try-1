from pydub import AudioSegment
from pathlib import Path
import toml
from ttsvoices.pyttsx import pyttsx
import re
from ttsvoices.streamlabspolly import streamlabspolly
from ttsvoices.longstring import preparetext
from ttsvoices.tiktok import tiktoktts
from ttsvoices.GTTS import gtts


with open("config.toml", "r") as f:
    config = toml.load(f)


ttsengines = [
    (lambda x: config["preferances"]["voice"] == "pyttsx3", pyttsx),
    (
        lambda x: config["preferances"]["voice"] == "streamlabspolly",  
        streamlabspolly,
    ),
    (lambda x: config["preferances"]["voice"] == "tiktok", tiktoktts),
    (lambda x: config["preferances"]["voice"] == "gtts", gtts),
]


def tts(texts: str, titles: str, title: str) -> None:
    AudioSegment.converter = r"C:\PATH_Programs\ffmpeg.exe" 
    tottext = preparetext(texts, titles)
    path = Path(rf"./assets/temp/{title}/audio")    
    path.mkdir(parents=True, exist_ok=True)
    for check, function in ttsengines:
        if check(ttsengines):
            function(tottext, path, title)      
            break
                