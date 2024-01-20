import requests
from requests.exceptions import JSONDecodeError
import ttsvoices.longstring as longstring
from tqdm import tqdm
from pydub import AudioSegment
import time

voices = [
    "Brian",
    "Emma",
    "Russell",
    "Joey",
    "Matthew",
    "Joanna",
    "Kimberly",
    "Amy",
    "Geraint",
    "Nicole",
    "Justin",
    "Ivy",
    "Kendra",
    "Salli",
    "Raveena",
]


def streamlabspolly(text, path, title, voice="Matthew"):
    text = longstring.checkifstringlong(text, 500)
    print(text)
    url = "https://streamlabs.com/polly/speak"
    for idx, texts in enumerate(tqdm(text)):
        body = {"voice": voice, "text": texts, "service": "polly"}
        response = requests.post(url, data=body)
        try:
            voice_data = requests.get(response.json()["speak_url"])
            if idx != 0:
                with open(rf"{path}/{title}{idx}.mp3", "wb") as f:
                    f.write(voice_data.content)
                part1 = AudioSegment.from_mp3(f"{path}/{title}.mp3")
                part2 = AudioSegment.from_mp3(f"{path}/{title}{idx}.mp3")
                complete = part1 + part2
                complete.export(f"{path}/{title}.mp3", format="mp3")
            else:
                with open(rf"{path}/{title}.mp3", "wb") as f:
                    f.write(voice_data.content)
        except (KeyError, JSONDecodeError):
            try:
                if response.json()["error"] == "No text specified!":
                    raise ValueError("Please specify a text to convert to speech.")
            except (KeyError, JSONDecodeError):
                print("Error occurred calling Streamlabs Polly")

