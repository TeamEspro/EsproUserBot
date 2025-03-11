import asyncio, os, yt_dlp

# ✅ Cookies file ka path set karein
COOKIES_FILE = "cookies.txt"  # Change this if needed


async def download_media_file(link: str, media_type: str):
    loop = asyncio.get_running_loop()

    # ✅ Ensure downloads folder exists
    os.makedirs("downloads", exist_ok=True)

    # ✅ YT-DLP options with cookies support
    ydl_opts = {
        "outtmpl": "downloads/%(id)s.%(ext)s",
        "geo_bypass": True,
        "nocheckcertificate": True,
        "quiet": True,
        "no_warnings": True,
        "cookiefile": COOKIES_FILE if os.path.exists(COOKIES_FILE) else None,
    }

    if media_type.lower() == "audio":
        ydl_opts.update({"format": "bestaudio/best"})
    elif media_type.lower() == "video":
        ydl_opts.update(
            {"format": "(bestvideo[height<=?720][width<=?1280][ext=mp4])+(bestaudio[ext=m4a])"}
        )

    async with loop.run_in_executor(None, yt_dlp.YoutubeDL, ydl_opts) as x:
        info = await loop.run_in_executor(None, x.extract_info, link, False)
        file = f"downloads/{info['id']}.{info['ext']}"

        if os.path.exists(file):
            return file

        await loop.run_in_executor(None, x.download, [link])
        return file
