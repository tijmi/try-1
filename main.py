import getreddittop as redtop
import getaudiofile as aufile
import firsttime as ft
import toml

def main():

    with open('config.toml', 'r') as f:
        config = toml.load(f)

    if config['settings']['firsttime'] == "yes":
        ft.firsttime
        
    toppost = redtop.reddittop(config["preferances"]["subreddit"])
    print(toppost)
    aufile.tts(toppost[1],toppost[0],config['tiktok']['session_id'])


if __name__ == "__main__":
    main()
