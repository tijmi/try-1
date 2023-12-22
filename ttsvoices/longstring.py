from textwrap import TextWrapper
import re


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
