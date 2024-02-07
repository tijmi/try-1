import requests
import base64
import argparse
import os
import ttsvoices.longstring as longstring
import toml

with open("config.toml", "r") as f:
    config = toml.load(f)


def tiktoktts(text: str, path: str, title: str, voice: str = "en_us_00"):
    text = longstring.checkifstringlong(text, 500)

    session_id = config["tiktok"]["tiktok_session_id"]

    headers = {
        "User-Agent": "com.zhiliaoapp.musically/2022600030 (Linux; U; Android 7.1.2; es_ES; SM-G988N; Build/NRD90M;tt-ok/3.12.13.1)",
        "Cookie": f"sessionid={session_id}",
    }
    url = f"https://api16-normal-useast5.us.tiktokv.com/media/api/text/speech/invoke/?text_speaker={voice}&req_text={text}&speaker_map_type=0&aid=1233"

    r = requests.post(url, headers=headers)

    if r.json()["message"] == "Couldn't load speech. Try again.":
        output_data = r.json()["message"]
        print(output_data)
        return output_data

    vstr = [r.json()["data"]["v_str"]][0]

    b64d = base64.b64decode(vstr)

    with open(rf"{path}/{title}.mp3", "wb") as f:
        f.write(b64d)
