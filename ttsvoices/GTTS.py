from gtts import gTTS
from pathlib import Path
import ttsvoices.longstring as longstring


def gtts(text: str, path: str, title: str, lang: str = "en"):
    text = longstring.checkifstringlong(text, 500)
    tts = gTTS(text=text, path=path, lang=lang, slow=False)
    tts.save(Path(path) / f"{title}.mp3")
