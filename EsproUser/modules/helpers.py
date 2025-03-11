import asyncio, os, yt_dlp

async def download_media_file(link: str, type: str):
    loop = asyncio.get_running_loop()

    cookies_path = "cookies.txt"  # Ensure this file exists in the same directory
    
    if type == "Audio":
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": "downloads/%(title)s.%(ext)s",
            "geo_bypass": True,
            "nocheckcertificate": True,
            "quiet": True,
            "no_warnings": True,
            "cookiefile": cookies_path  # Using cookies for authentication
        }

    elif type == "Video":
        ydl_opts = {
            "format": "(bestvideo[height<=?720][width<=?1280][ext=mp4])+(bestaudio[ext=m4a])",
            "outtmpl": "downloads/%(title)s.%(ext)s",
            "geo_bypass": True,
            "nocheckcertificate": True,
            "quiet": True,
            "no_warnings": True,
            "cookiefile": cookies_path  # Using cookies for authentication
        }

    x = yt_dlp.YoutubeDL(ydl_opts)
    
    # Fetch video info
    info = x.extract_info(link, download=False)
    if "id" not in info or "ext" not in info:
        return None  

    file_path = x.prepare_filename(info)

    if os.path.exists(file_path):
        return file_path

    await loop.run_in_executor(None, x.download, [link])
    
    return file_path
