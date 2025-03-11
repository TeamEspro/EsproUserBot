import asyncio
import os
import yt_dlp

COOKIES_FILE = "cookies.txt"  # Cookies ka file path

async def download_media_file(link: str, media_type: str):
    """YouTube se Audio ya Video download karega, cookies ke saath."""
    
    loop = asyncio.get_running_loop()

    # Check agar valid media type hai
    if media_type not in ["Audio", "Video"]:
        raise ValueError("Invalid media type! Use 'Audio' or 'Video'.")

    # Download options
    ydl_opts = {
        "format": "bestaudio/best" if media_type == "Audio" else "(bestvideo[height<=?720][ext=mp4])+bestaudio[ext=m4a]",
        "outtmpl": "downloads/%(id)s.%(ext)s",
        "geo_bypass": True,
        "nocheckcertificate": True,
        "quiet": True,
        "no_warnings": True,
        "cookies": COOKIES_FILE,  # Cookies use karega
    }

    # Function to extract info
    def extract_info():
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            return ydl.extract_info(link, False)

    info = await loop.run_in_executor(None, extract_info)

    if not info:
        raise Exception("Failed to fetch video details!")

    file_path = os.path.join("downloads", f"{info.get('id', 'unknown')}.{info.get('ext', 'mp4')}")

    # Agar file already exist karti hai
    if os.path.exists(file_path):
        return file_path

    # Function to download
    def download():
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])

    await loop.run_in_executor(None, download)

    return file_path


