import asyncio
import yt_dlp
from typing import Union

from pyrogram.types import Audio, Voice, Video, VideoNote
from pytgcalls.types import MediaStream
from pytgcalls.types.raw import AudioParameters, VideoParameters
from youtubesearchpython.__future__ import VideosSearch


# Function to Get Audio File Name
def get_audio_name(audio: Union[Audio, Voice]) -> str:
    try:
        file_name = (
            audio.file_unique_id
            + "."
            + (audio.file_name.split(".")[-1] if not isinstance(audio, Voice) else "ogg")
        )
    except:
        file_name = audio.file_unique_id + ".ogg"
        
    return file_name


# Function to Get Video File Name
def get_video_name(video: Union[Video, VideoNote]) -> str:
    try:
        file_name = video.file_unique_id + "." + video.file_name.split(".")[-1]
    except:
        file_name = video.file_unique_id + ".mp4"
    
    return file_name


# Function to Get Details of YouTube Video
async def get_media_info(vidid: str, query: str):
    url = f"https://www.youtube.com/watch?v={vidid}" if vidid else None
    search = url if url else query
    results = VideosSearch(search, limit=1)

    for result in (await results.next())["result"]:
        videoid = vidid if vidid else result["id"]
        videourl = url if url else result["link"]

    return [videoid, videourl]


# Function to Get Direct Streaming Link from YouTube
async def get_stream_link(link: str):
    proc = await asyncio.create_subprocess_exec(
        "yt-dlp",
        "-g",
        "-f",
        "bestvideo+bestaudio/best",
        link,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await proc.communicate()
    links = stdout.decode().split('\n')
    
    return links[0], links[1] if len(links) > 1 else None


# Function to Create Media Stream for PyTgCalls
async def get_media_stream(media: str, stream_type: str):
    if stream_type == "Audio":
        stream = MediaStream(
            media_path=media,
            video_flags=MediaStream.IGNORE,
            audio_parameters=AudioParameters(
                frame_duration=60,  # Frame Duration in ms
                frequency=48000,    # Audio Frequency
                bitrate=128000      # Audio Bitrate
            ),
        )
    elif stream_type == "Video":
        stream = MediaStream(
            media_path=media,
            audio_parameters=AudioParameters(
                frame_duration=60,
                frequency=48000,
                bitrate=128000
            ),
            video_parameters=VideoParameters(
                width=1280,  # Video Width
                height=720,  # Video Height
                fps=30       # Frames Per Second
            ),
        )
            
    return stream
