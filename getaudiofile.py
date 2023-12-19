from textwrap import TextWrapper
from tqdm import tqdm
from pydub import AudioSegment
from pathlib import Path
import toml
import ttsvoices.pyttsx as pptts
import re
import ttsvoices.streamlabspolly as streamlabs
import random
import time


with open("config.toml", "r") as f:
    config = toml.load(f)


def checkifstringlong(text, maxlength=int):
    numofcharacters = len(text)
    print(numofcharacters)
    if numofcharacters > maxlength:
        w = TextWrapper(maxlength, break_long_words=False)
        return w.wrap(text)
    return text


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


def tts(texts, titles, text_speaker: str = "en_us_002"):
    AudioSegment.converter = r"C:\PATH_Programs\ffmpeg.exe"
    tottext = preparetext(texts, titles)
    specialcharacters = r"(!?[^A-Za-z0-9 ])"
    titles = re.sub(specialcharacters, " ", titles)
    print(titles)
    titles = titles.replace(" ", "_")
    titles = titles.replace(".", "")
    path = Path(rf"./assets/temp/{titles}/audio")
    path.mkdir(parents=True, exist_ok=True)
    # if config["settings"]["voice"] == "tiktok":   
    #     text = checkifstringlong(tottext)
    #     for idx, texts in enumerate(tqdm(text)):
    #         if idx != 0:
    #             title = titles + str(idx)
    #             print(titles)
    #             ttstomp3tt(texts, title, text_speaker)
    #             part1 = AudioSegment.from_mp3(f"./assets/temp/{titles}/audio/{titles}.mp3")
    #             part2 = AudioSegment.from_mp3(f"./assets/temp/{titles}/audio/{title}.mp3")
    #             complete = part1 + part2
    #             complete.export(f".assets/temp/{titles}/audio/{titles}.mp3", format="mp3")

    #         else:
    #             ttstomp3tt(texts, titles, text_speaker)
    if config["preferances"]["voice"] == "pyttsx3":
        pptts.pyttsx(tottext, titles)
    elif config["preferances"]["voice"] == "streamlabspolly":
        streamlabs.streamlabspolly(tottext, f"{path}/{titles}.mp3")
