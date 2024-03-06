import toml
import json
import getreddittop as reddittop


class validation:
    def __init__(self):
        with open("config.toml", "r") as f:
            self.config = toml.load(f)

        with open("configoptions.json", "r") as f:
            self.settingsfile = json.load(f)

    def writetoml(self) -> None:
        with open("config.toml", "w") as f:
            toml.dump(self.config, f)

    def valueinput(self, setting: str, catagory: str, options: bool = False) -> None:
        while True:
            if options:
                possibilities = ", ".join(self.settingsfile[setting])
                choise = input(
                    f"""please choose a {setting} from the following options:
        {possibilities}
    """
                )

                if choise in self.settingsfile[setting]:
                    self.config[catagory][setting] = choise
                    self.writetoml()
                    break
            else:
                choise = input(
                    f"""please select a {setting}
"""
                )
                self.config[catagory][setting] = choise
                self.writetoml()
                break

    def validatenooptions(self, setting, catagory):
        match self.config:
            case {"settings": {"background": str()}} if self.config[catagory][setting]:
                pass
            case _:
                self.valueinput(setting, catagory)

    def ValidateOptions(self, setting, catagory):
        match self.config:
            case {"settings": {"background": str()}} if self.config[catagory][
                setting
            ] in self.settingsfile[setting]:
                pass
            case _:
                self.valueinput(setting, catagory, True)

    def validatetoml(self) -> None:
        self.ValidateOptions("background", "settings")

        redditlogin = [
            "client_id",
            "client_secret",
            "user_agent",
            "username",
            "password",
        ]
        for i in redditlogin:
            self.validatenooptions(i, "redditlogin")

        self.validatenooptions("subreddit", "preferances")
        while True:
            realsub = reddittop.sub_exists(self.config["preferances"]["subreddit"])
            if realsub:
                break
            else:
                print("subreddit not found")
                self.valueinput("subreddit", "preferances")

        self.ValidateOptions("ttsengine", "preferances")
        if self.config["preferances"]["ttsengine"] == "tiktok":
            print("Tiktok tts is very buggy do you want to continue? y/n")
            further = input()
            if further == "y":
                self.validatenooptions("sessionid", "tiktok_session_id")
            else:
                self.validateinput("sessionid", "tiktok_session_id", True)
