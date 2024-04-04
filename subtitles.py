import math
import moviepy.editor as mpe
from faster_whisper import WhisperModel
from moviepy.video.tools.subtitles import SubtitlesClip
from moviepy.editor import TextClip, CompositeVideoClip, VideoFileClip
from pathlib import Path


class subtitles:
    def __init__(self, inputvid, audiofile, title, promt) -> None:
        self.title = title
        self.path = Path(f"./assets/temp/{self.title}/")
        self.input_video = self.path.joinpath(f"{inputvid}.mp4")
        self.subtitle_file = f"./assets/temp/{title}/subtitles.en.srt"
        self.audiofile = audiofile
        self.output = f"assets/temp/{title}/{title}_captions.mp4"
        self.promt = promt

    def transcribe(self):
        model = WhisperModel("medium")
        segments, info = model.transcribe(self.audiofile, initial_prompt=self.promt)
        language = info[0]
        print("Transcription language", info[0])
        self.segments = list(segments)
        for segment in self.segments:
            # print(segment)
            print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))

    def format_time(self, seconds):

        hours = math.floor(seconds / 3600)
        seconds %= 3600
        minutes = math.floor(seconds / 60)
        seconds %= 60
        milliseconds = round((seconds - math.floor(seconds)) * 1000)
        seconds = math.floor(seconds)
        formatted_time = f"{hours:02d}:{minutes:02d}:{seconds:01d},{milliseconds:03d}"

        return formatted_time

    def generate_subtitle_file(self):

        text = ""
        for index, segment in enumerate(self.segments):
            segment_start = self.format_time(segment.start)
            segment_end = self.format_time(segment.end)
            text += f"{str(index+1)} \n"
            text += f"{segment_start} --> {segment_end} \n"
            text += f"{segment.text} \n"
            text += "\n"
        f = open(self.subtitle_file, "w")
        f.write(text)
        f.close()

    def add_subtitle_to_video(
        self,
    ):
        video_input_stream = mpe.VideoFileClip(str(self.input_video))
        generator = lambda txt: TextClip(
            txt,
            font="arial",
            fontsize=40,
            stroke_color="black",
            color="white",
            method="caption",
            size=video_input_stream.size,
            align="Center",
            stroke_width=1.5
        )
        sub_clip = SubtitlesClip(self.subtitle_file, generator)
        result = CompositeVideoClip(
            (video_input_stream, sub_clip), size=video_input_stream.size
        )
        audio = mpe.AudioFileClip(str(self.audiofile))
        result = result.set_audio(audio)
        result.write_videofile(
            self.output,
            fps=video_input_stream.fps,
            temp_audiofile="temp-audio.m4a",
            remove_temp=True,
            codec="libx264",
            audio_codec="aac",
        )
        video_input_stream.close()


def add_subtitle(startvid, audiofile, title,text):
    captions = subtitles(startvid, audiofile, title,text)
    captions.transcribe()
    captions.generate_subtitle_file()
    captions.add_subtitle_to_video()
