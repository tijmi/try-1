import toml
import json


class validation:
    def __init__(self):
        with open("config.toml", "r") as f:
            self.config = toml.load(f)

        with open("background_videos.json", "r") as f:
            self.videos = json.load(f)

        with open("configoptions.json", "r") as f:
            self.settingsfile = json.load(f)
    
    def writetoml(self) -> None:
        with open('config.toml', 'w') as f:
            toml.dump(self.config, f)


    def valueinput(self, setting: str,catagory: str(), options: bool = False) -> None:
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
            

    def validatetoml(self) -> None:
        match self.config:
            case {"settings": {"background": str()}} if self.config["settings"][
                "background"
            ] in self.videos:
                pass
            case _:
                self.valueinput("background", "settings", True)
        match self.config:
            case {"settings": {"background": str()}} if self.config["settings"][
                "background"
            ] in self.videos:
                pass
