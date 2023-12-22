from pydub import AudioSegment
from pathlib import Path
import toml
import ttsvoices.pyttsx as pptts
import re
import ttsvoices.streamlabspolly as streamlabs
from ttsvoices.longstring import preparetext


with open("config.toml", "r") as f:
    config = toml.load(f)


def preparetext(text, title):
    regex_urls = r"((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*"
    text = title + text
    text = re.sub(regex_urls, " ", text)
    text = text.replace("\n", ". ")
    text = re.sub(r"\bAI\b", "A.I", text)
    text = re.sub(r"\bAGI\b", "A.G.I", text)
    if text[-1] != ".":
        text += "."
    text = text.replace(". . .", ".")
    text = text.replace(".. . ", ".")
    text = text.replace(". . ", ".")
    text = re.sub(r'\."\.', '".', text)
    return text

ttsengines = [
    (lambda x: config["preferances"]["voice"] == "pyttsx3", pptts.pyttsx),
    (lambda x: config["preferances"]["voice"] == "streamlabspolly", streamlabs.streamlabspolly)
]


def tts(texts, titles,):
    AudioSegment.converter = r"C:\PATH_Programs\ffmpeg.exe"
    tottext = preparetext(texts, titles)
    specialcharacters = r"(!?[^A-Za-z0-9 ])"
    titles = re.sub(specialcharacters, " ", titles)
    print(titles)
    titles = titles.replace(" ", "_")
    titles = titles.replace(".", "")
    path = Path(rf"./assets/temp/{titles}/audio")
    path.mkdir(parents=True, exist_ok=True)
    for check, function in ttsengines:
                if check(ttsengines):
                    function(tottext, path, titles)
                    break

