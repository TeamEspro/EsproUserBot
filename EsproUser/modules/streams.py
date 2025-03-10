import asyncio
import os
import re
import yt_dlp

from EsproUser import config
from pyrogram.types import Audio, Voice, Video, VideoNote
from pytgcalls.types import AudioQuality, VideoQuality, MediaStream
from typing import Union
from youtubesearchpython.__future__ import VideosSearch


# 📌 Get File Name for Audio
def get_audio_name(audio: Union[Audio, Voice]):
    try:
        file_name = (
            audio.file_unique_id
            + "."
            + (
                (audio.file_name.split(".")[-1])
                if (not isinstance(audio, Voice))
                else "ogg"
            )
        )
    except:
        file_name = audio.file_unique_id + ".ogg"
        
    return file_name


# 📌 Get File Name for Video
def get_video_name(video: Union[Video, VideoNote]):
    try:
        file_name = (
            video.file_unique_id
            + "."
            + (video.file_name.split(".")[-1])
        )
    except:
        file_name = video.file_unique_id + ".mp4"
    
    return file_name
    

# 🔍 Get YouTube Video Details
async def get_media_info(vidid: str, query: str):
    url = f"https://www.youtube.com/watch?v={vidid}" if vidid else None
    search = url if url else query
    results = VideosSearch(search, limit=1)

    for result in (await results.next())["result"]:
        videoid = vidid if vidid else result["id"]
        videourl = url if url else result["link"]

    return [videoid, videourl]


# 🎥 Get Direct YouTube Stream Link
async def get_stream_link(link: str):
    proc = await asyncio.create_subprocess_exec(
        "yt-dlp",
        "-g",
        "-f",
        "bestaudio/best",
        f"{link}",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await proc.communicate()
    links = stdout.decode().split('\n')
    
    return links[0], links[1]


# 📥 **Download Media from YouTube**
async def download_media_file(url: str, type: str):
    """
    Given a YouTube URL, download the media file as audio or video.
    """
    output_path = "downloads/"  # Ensure this folder exists
    os.makedirs(output_path, exist_ok=True)

    filename = "%(title)s.%(ext)s"
    
    ydl_opts = {
        "format": "bestaudio/best" if type == "Audio" else "best",
        "outtmpl": os.path.join(output_path, filename),
        "quiet": True,
        "no_warnings": True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            downloaded_file = ydl.prepare_filename(info)
        return downloaded_file
    except Exception as e:
        print(f"Download Error: {e}")
        return None


# 🎵 Stream Using PyTgCalls
async def get_media_stream(media, type: str):
    if type == "Audio":
        stream = MediaStream(
            media_path=media,
            video_flags=MediaStream.IGNORE,
            audio_parameters=AudioQuality.STUDIO,
        )
    elif type == "Video":
        stream = MediaStream(
            media_path=media,
            audio_parameters=AudioQuality.STUDIO,
            video_parameters=VideoQuality.HD_720p,
        )
            
    return stream
