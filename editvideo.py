import moviepy.editor as mpe
from pydub import AudioSegment
import os
from moviepy.editor import AudioFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.video.fx.all import crop
import random


def combine_audio(vidname, audname, outname, fps=60):
    background = mpe.VideoFileClip(vidname)
    audio = mpe.AudioFileClip(audname)
    final_clip = background.set_audio(audio)
    final_clip.write_videofile(outname, fps=fps)
    background.close()
    audio.close()
    final_clip.close()


def cut_video_to_mp3_length(video_path, mp3_path, output_path):
    AudioSegment.converter = r"C:\\PATH_Programs\\ffmpeg.exe"
    audio = AudioFileClip(mp3_path)
    background = mpe.VideoFileClip(video_path)
    print(background.duration)
    print(audio.duration)
    begintime = random.uniform(0, background.duration - audio.duration)
    print(begintime)
    ffmpeg_extract_subclip(
        video_path, begintime, begintime + audio.duration, targetname=output_path
    )
    audio.close()


def make_video_916(video_path, output_path):
    video = mpe.VideoFileClip(video_path)
    width, height = video.size
    new_width = (height / 16) * 9
    width_margin = int((width - new_width) / 2)

    cropped_clip = crop(
        video, x1=width_margin, y1=0, x2=width_margin + new_width, y2=height
    )
    cropped_clip.write_videofile(
        output_path,
        codec="libx264",
        audio_codec="aac",
    )
    video.close()
    cropped_clip.close()


def editvideo(vidname, audname, outname, title):
    os.path.abspath(audname)
    cut_video_to_mp3_length(vidname, audname, rf".\assets\temp\{title}\tempbackground.mp4")
    make_video_916(rf".\assets\temp\{title}\tempbackground.mp4", rf".\assets\temp\{title}\background.mp4")
    combine_audio(rf".\assets\temp\{title}\background.mp4", audname, outname)
