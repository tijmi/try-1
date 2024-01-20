from textwrap import TextWrapper
import re


URL_REGEX = r"((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*"
SPECIALCHARACTER_REGEX = r"(!?[^A-Za-z0-9 ])"

def checkifstringlong(text: str, maxlength: int) -> list[str]:
    numofcharacters = len(text)
    print(numofcharacters)
    w = TextWrapper(maxlength, break_long_words=False)
    return w.wrap(text)


def preparetext(text: str, title: str) -> str:
    text = f"{title}{text}"
    text = re.sub(URL_REGEX, " ", text)
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

def preparetitle(title: str) -> str:
    title = re.sub(SPECIALCHARACTER_REGEX, "", title)
    title = title.replace(" ", "_")
    title = title.replace(".", "")
    w = TextWrapper(30, break_long_words=True)
    title = w.wrap(title)
    return title