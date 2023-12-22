import pyttsx3


def pyttsx(text, path, titles):
    engine = pyttsx3.init()
    engine.save_to_file(text, rf"{path}/{titles}.mp3")
    engine.runAndWait()
