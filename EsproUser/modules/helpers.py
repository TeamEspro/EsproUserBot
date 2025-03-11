import asyncio, os, yt_dlp, ssl

# Disable SSL verification (Temporary fix)
ssl._create_default_https_context = ssl._create_unverified_context

async def download_media_file(link: str, type: str):
    loop = asyncio.get_running_loop()
    
    if type == "Audio":
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": "downloads/%(title)s.%(ext)s",
            "geo_bypass": True,
            "nocheckcertificate": True,
            "quiet": True,
            "no_warnings": True,
        }

    elif type == "Video":
        ydl_opts = {
            "format": "(bestvideo[height<=?720][width<=?1280][ext=mp4])+(bestaudio[ext=m4a])",
            "outtmpl": "downloads/%(title)s.%(ext)s",
            "geo_bypass": True,
            "nocheckcertificate": True,
            "quiet": True,
            "no_warnings": True,
        }
    
    x = yt_dlp.YoutubeDL(ydl_opts)
    
    info = x.extract_info(link, download=False)
    if "id" not in info or "ext" not in info:
        return None  

    file_path = x.prepare_filename(info)

    if os.path.exists(file_path):
        return file_path

    await loop.run_in_executor(None, x.download, [link])
    
    return file_path
