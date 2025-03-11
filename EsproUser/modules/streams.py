import asyncio
import yt_dlp

from EsproUser import config
from pyrogram.types import Audio, Voice, Video, VideoNote
from pytgcalls.types import AudioQuality, VideoQuality, MediaStream
from typing import Union
from youtubesearchpython.__future__ import VideosSearch


# 🎵 Audio File Name Generator
def get_audio_name(audio: Union[Audio, Voice]):
    try:
        file_name = (
            audio.file_unique_id + "." +
            (audio.file_name.split(".")[-1] if not isinstance(audio, Voice) else "ogg")
        )
    except:
        file_name = audio.file_unique_id + ".ogg"

    return file_name


# 🎥 Video File Name Generator
def get_video_name(video: Union[Video, VideoNote]):
    try:
        file_name = video.file_unique_id + "." + video.file_name.split(".")[-1]
    except:
        file_name = video.file_unique_id + ".mp4"

    return file_name


# 📌 Get YouTube Video Details (Fixed next() issue)
async def get_media_info(vidid: str, query: str):
    url = f"https://www.youtube.com/watch?v={vidid}" if vidid else None
    search = url if url else query
    
    results = VideosSearch(search, limit=1)  # Object create karo
    search_results = await results.next()  # next() method async call karo
    
    if search_results["result"]:
        result = search_results["result"][0]
        videoid = vidid if vidid else result["id"]
        videourl = url if url else result["link"]
        return [videoid, videourl]
    
    return None


# 🔗 Get Direct Streaming Link (With Cookies Support)
async def get_stream_link(link: str, cookies_path: str = "cookies.txt"):
    proc = await asyncio.create_subprocess_exec(
        "yt-dlp", "-g", "-f", "bestaudio[ext=webm]/bestaudio/best",
        "--cookies", cookies_path,  # Cookies file ka path
        link, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await proc.communicate()
    
    if stderr:
        print(f"yt-dlp error: {stderr.decode()}")

    links = stdout.decode().split("\n")
    return (links[0], links[1]) if len(links) > 1 else (links[0], None)


# 🔄 Alternative: Get Stream Link via Browser Session
async def get_stream_link_browser(link: str, browser: str = "chrome"):
    proc = await asyncio.create_subprocess_exec(
        "yt-dlp", "-g", "-f", "bestaudio[ext=webm]/bestaudio/best",
        "--cookies-from-browser", browser,  # Chrome ya Firefox session use karega
        link, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await proc.communicate()
    
    if stderr:
        print(f"yt-dlp error: {stderr.decode()}")

    links = stdout.decode().split("\n")
    return (links[0], links[1]) if len(links) > 1 else (links[0], None)


# 📡 Stream Using PyTgCalls
async def get_media_stream(media, type: str):
    if type == "Audio":
        return MediaStream(
            media_path=media,
            audio_parameters=AudioQuality.STUDIO,
        )
    elif type == "Video":
        return MediaStream(
            media_path=media,
            audio_parameters=AudioQuality.STUDIO,
            video_parameters=VideoQuality.HD_720p,
        )
    else:
        raise ValueError("Invalid media type. Use 'Audio' or 'Video'.")
