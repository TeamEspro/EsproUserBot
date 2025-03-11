import asyncio
import os
import yt_dlp

COOKIES_FILE = "cookies.txt"
async def download_media_file(link: str, media_type: str):
    loop = asyncio.get_running_loop()

    # Common yt-dlp Options
    ydl_opts = {
        "outtmpl": "downloads/%(id)s.%(ext)s",
        "geo_bypass": True,
        "nocheckcertificate": True,
        "quiet": True,
        "no_warnings": True,
        "cookiefile": COOKIES_FILE,  # Cookies Support Added
        "http_headers": {  # Custom Headers
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9",
        },
    }

    # Audio Download
    if media_type.lower() == "audio":
        ydl_opts["format"] = "bestaudio/best"

    # Video Download
    elif media_type.lower() == "video":
        ydl_opts["format"] = "(bestvideo[height<=?720][width<=?1280][ext=mp4])+(bestaudio[ext=m4a])"

    x = yt_dlp.YoutubeDL(ydl_opts)

    try:
        info = await loop.run_in_executor(None, lambda: x.extract_info(link, download=False))
        file = os.path.join("downloads", f"{info['id']}.{info['ext']}")

        if os.path.exists(file):
            return file

        await loop.run_in_executor(None, x.download, [link])
        return file

    except yt_dlp.utils.DownloadError as e:
        print(f"Download Error: {e}")
        return None

    except Exception as e:
        print(f"Unexpected Error: {e}")
        return None
