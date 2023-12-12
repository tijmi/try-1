import getreddittop as redtop
import getaudiofile as aufile


def main():
    toppost = redtop.reddittop("tifu")
    print(toppost)
    aufile.tts(toppost[1],toppost[0],"54e28104b2b95545bdb4ed911b9e08ab")


if __name__ == "__main__":
    main()
