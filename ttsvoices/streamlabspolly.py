import requests
from requests.exceptions import JSONDecodeError

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

def streamlabspolly(text,path,voice = "Matthew"):
    url = "https://streamlabs.com/polly/speak"
    body = {"voice": voice, "text": text, "service": "polly"}
    response = requests.post(url, data=body)
    try:
        voice_data = requests.get(response.json()["speak_url"])
        with open(path, "wb") as f:
            f.write(voice_data.content)
    except (KeyError, JSONDecodeError):
        try:
            if response.json()["error"] == "No text specified!":
                raise ValueError("Please specify a text to convert to speech.")
        except (KeyError, JSONDecodeError):
            print("Error occurred calling Streamlabs Polly")
    