import asyncio
import os
import yt_dlp


COOKIES_FILE = "cookies.txt"  # Change path as needed

async def download_media_file(link: str, media_type: str):
    loop = asyncio.get_running_loop()
    
    # Common options
    ydl_opts = {
        "outtmpl": "downloads/%(title)s.%(ext)s",
        "geo_bypass": True,
        "nocheckcertificate": True,
        "quiet": True,
        "no_warnings": True,
        "cookiefile": "cookies.txt",  # Cookie support added
    }

    # Format selection based on type
    if media_type.lower() == "audio":
        ydl_opts.update({
            "format": "bestaudio/best",
            "merge_output_format": "mp3",
        })
    elif media_type.lower() == "video":
        ydl_opts.update({
            "format": "(bestvideo[height<=?720][ext=mp4])+bestaudio[ext=m4a]/best[ext=mp4]",
            "merge_output_format": "mp4",
        })
    else:
        return None  # Invalid media type
    
    # Function to run in executor
    def download():
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(link, download=True)
            return ydl.prepare_filename(info)  # Returns correct filename
    
    downloaded_file = await loop.run_in_executor(None, download)
    return downloaded_file

# Example usage:
# asyncio.run(download_media_file("https://www.youtube.com/watch?v=VIDEO_ID", "Audio"))
