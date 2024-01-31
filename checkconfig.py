import toml

with open("config.toml", "r") as f:
        config = toml.load(f)

def validatetoml():
    match config:
          case {
                "settings":{}
          }:
                pass
          case _:
                pass        