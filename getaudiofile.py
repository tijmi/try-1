import pyttsx3
import os
import requests
import base64
from textwrap import TextWrapper
from tqdm import tqdm
from pydub import AudioSegment

voices = [
    # DISNEY VOICES
    "en_us_ghostface",  # Ghost Face
    "en_us_chewbacca",  # Chewbacca
    "en_us_c3po",  # C3PO
    "en_us_stitch",  # Stitch
    "en_us_stormtrooper",  # Stormtrooper
    "en_us_rocket",  # Rocket
    # ENGLISH VOICES
    "en_au_001",  # English AU - Female
    "en_au_002",  # English AU - Male
    "en_uk_001",  # English UK - Male 1
    "en_uk_003",  # English UK - Male 2
    "en_us_001",  # English US - Female (Int. 1)
    "en_us_002",  # English US - Female (Int. 2)
    "en_us_006",  # English US - Male 1
    "en_us_007",  # English US - Male 2
    "en_us_009",  # English US - Male 3
    "en_us_010",  # English US - Male 4
    # EUROPE VOICES
    "fr_001",  # French - Male 1
    "fr_002",  # French - Male 2
    "de_001",  # German - Female
    "de_002",  # German - Male
    "es_002",  # Spanish - Male
    # AMERICA VOICES
    "es_mx_002",  # Spanish MX - Male
    "br_001",  # Portuguese BR - Female 1
    "br_003",  # Portuguese BR - Female 2
    "br_004",  # Portuguese BR - Female 3
    "br_005",  # Portuguese BR - Male
    # ASIA VOICES
    "id_001",  # Indonesian - Female
    "jp_001",  # Japanese - Female 1
    "jp_003",  # Japanese - Female 2
    "jp_005",  # Japanese - Female 3
    "jp_006",  # Japanese - Male
    "kr_002",  # Korean - Male 1
    "kr_003",  # Korean - Female
    "kr_004",  # Korean - Male 2
    # SINGING VOICES
    "en_female_f08_salut_damour"  # Alto
    "en_male_m03_lobby"  # Tenor
    "en_female_f08_warmy_breeze"  # Warmy Breeze
    "en_male_m03_sunshine_soon"  # Sunshine Soon
    # OTHER
    "en_male_narration"  # narrator
    "en_male_funny"  # wacky
    "en_female_emotional",  # peaceful
]


def ttstomp3(text, titles, session_id, text_speaker: str = "en_us_002"):
    texts = "".join(text)
    texts = texts.replace("+", "plus")
    texts = texts.replace(" ", "+")
    texts = texts.replace("&", "and")

    headers = {
        "User-Agent": "com.zhiliaoapp.musically/2022600030 (Linux; U; Android 7.1.2; es_ES; SM-G988N; Build/NRD90M;tt-ok/3.12.13.1)",
        "Cookie": f"sessionid={session_id}",
    }

    url = f"https://api16-normal-v6.tiktokv.com/media/api/text/speech/invoke/?text_speaker={text_speaker}&req_text={texts}&speaker_map_type=0&aid=1233"
    r = requests.post(url, headers=headers)

    if r.json()["message"] == "Couldn't load speech. Try again.":
        output_data = {"status": "Session ID is invalid", "status_code": 5}
        print(output_data)
        return output_data

    vstr = [r.json()["data"]["v_str"]][0]
    msg = [r.json()["message"]][0]
    scode = [r.json()["status_code"]][0]
    log = [r.json()["extra"]["log_id"]][0]

    dur = [r.json()["data"]["duration"]][0]
    spkr = [r.json()["data"]["speaker"]][0]

    b64d = base64.b64decode(vstr)
    titles = titles.replace(" ", "_")
    with open(f"./audio/{titles}.mp3", "wb") as out:
        out.write(b64d)

    output_data = {
        "status": msg.capitalize(),
        "status_code": scode,
        "duration": dur,
        "speaker": spkr,
        "log": log,
    }

    return output_data


def checkifstringlong(text):
    numofcharacters = len(text)
    print(numofcharacters)
    if numofcharacters > 200:
        w = TextWrapper(200, break_long_words=False)
        return w.wrap(text)
    return text


def tts(texts, titles, session_id, text_speaker: str = "en_us_002"):
    AudioSegment.converter = r"C:\\Users\\thijm\\AppData\\Local\\Microsoft\\WinGet\\Packages\\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\\ffmpeg-6.1-full_build\\bin\\ffmpeg.exe"
    tottext = texts + titles
    text = checkifstringlong(tottext)
    for idx, texts in enumerate(tqdm(text)):
        title = titles
        if idx != 0:
            title = titles + str(idx)
            title.join(e for e in title if e.isalnum())
            title = title.replace(" ", "_")
            titles = titles.replace(" ", "_")
            print(titles)
            ttstomp3(texts, title, session_id, text_speaker)
            part1 = AudioSegment.from_mp3(f".\\audio\\{titles}.mp3")
            part2 = AudioSegment.from_mp3(f".\\audio\\{title}.mp3")
            complete = part1 + part2
            complete.export(f"./audio/{titles}.mp3", format="mp3")

        else:
            ttstomp3(texts, title, session_id, text_speaker)
