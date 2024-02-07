from gtts import gTTS
from pathlib import Path
import ttsvoices.longstring as longstring


# def gtts(text: str, path: str, title: str, lang: str = "en"):
#     text = longstring.checkifstringlong(text, 500)
#     tts = gTTS(text)
#     saveplace = f"{path}/{title}.mp3"
#     tts.save(saveplace)
def gtts(text, path, title):
        tts = gTTS(
            text=text,
            lang="en",
            slow=False,
        )
        filepath = Path(path, f"{title}.mp3")
        tts.save(filepath)