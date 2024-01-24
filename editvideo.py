import moviepy.editor as mpe
from pydub import AudioSegment
import os
from moviepy.editor import AudioFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.video.fx.all import crop
import random
import toml
from pathlib import Path


class editvideo:
    def __init__(self, audname: str, outname: str, title: str):
        with open("config.toml", "r") as f:
            config = toml.load(f)

        self.background = config["settings"]["background"]
        self.pathbackground = Path("./assets/backgrounds/video/")
        self.backgroundvid = self.pathbackground.joinpath(f"{self.background}.mp4")
        self.audname = audname
        self.outname = outname
        self.title = title
        self.path = Path(f"./assets/temp/{self.title}/")
        self.backgroundvidtot = self.path.joinpath(f"{self.background}.mp4")
        self.backgroundvidmp3 = self.path.joinpath("tempbackground.mp4")

    def combine_audio(self, fps: int = 60) -> None:
        background = mpe.VideoFileClip(str(self.backgroundvidtot))
        audio = mpe.AudioFileClip(str(self.audname))
        final_clip = background.set_audio(audio)
        final_clip.write_videofile(str(self.outname), fps=fps)
        background.close()
        audio.close()
        final_clip.close()

    def cut_video_to_mp3_length(self) -> None:
        AudioSegment.converter = r"C:\\PATH_Programs\\ffmpeg.exe"
        audio = mpe.AudioFileClip(str(self.audname))
        background = mpe.VideoFileClip(str(self.backgroundvid))
        print(background.duration)
        print(audio.duration)
        begintime = random.uniform(0, background.duration - audio.duration)
        print(begintime)
        ffmpeg_extract_subclip(
            str(self.backgroundvid),
            begintime,
            begintime + audio.duration,
            targetname=self.backgroundvidmp3,
        )
        audio.close()

    def make_video_916(self) -> None:
        video = mpe.VideoFileClip(str(self.backgroundvidmp3))
        width, height = video.size
        new_width = (height / 16) * 9
        width_margin = int((width - new_width) / 2)

        cropped_clip = crop(
            video, x1=width_margin, y1=0, x2=width_margin + new_width, y2=height
        )
        cropped_clip.write_videofile(
            str(self.backgroundvidtot),
            codec="libx264",
            audio_codec="aac",
        )
        video.close()
        cropped_clip.close()


def finalvideo(audname, outname, title) -> None:
    video = editvideo(audname, outname, title)
    video.cut_video_to_mp3_length()
    video.make_video_916()
    video.combine_audio()
