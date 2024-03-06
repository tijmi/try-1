import pyttsx3
import ttsvoices.longstring as longstring
 

def pyttsx(text, path, titles):
    engine = pyttsx3.init()
    engine.save_to_file(text, rf"{path}/{titles}.mp3")
    engine.runAndWait()
