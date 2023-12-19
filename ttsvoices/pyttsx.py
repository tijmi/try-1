import pyttsx3


def pyttsx(text, titles):
    engine = pyttsx3.init()
    engine.save_to_file(text, rf".\assets\temp\{titles}\audio\{titles}.mp3")
    engine.runAndWait()
