import asyncio
import os
import ssl
import yt_dlp
import certifi

# ✅ SSL FIX: Set correct SSL certificate file
ssl._create_default_https_context = ssl._create_unverified_context  # Temporary fix
os.environ["SSL_CERT_FILE"] = certifi.where()

async def download_media_file(link: str, media_type: str):
    """YouTube se video/audio download karta hai cookies aur SSL fix ke saath."""
    
    loop = asyncio.get_running_loop()
    cookies_path = "cookies.txt"  # Ensure yeh file exist karti hai
    
    # ✅ yt-dlp options (SSL Fix + Cookies)
    ydl_opts = {
        "format": "bestaudio/best" if media_type == "Audio" else "(bestvideo[height<=?720][width<=?1280][ext=mp4])+(bestaudio[ext=m4a])",
        "outtmpl": "downloads/%(title)s.%(ext)s",
        "geo_bypass": True,
        "nocheckcertificate": True,  # ✅ SSL Verify Bypass
        "quiet": True,
        "no_warnings": True,
        "cookiefile": cookies_path,  # ✅ YouTube Authentication
    }

    x = yt_dlp.YoutubeDL(ydl_opts)
    
    try:
        # ✅ Extract info without downloading (to get correct filename)
        info = x.extract_info(link, download=False)

        if "id" not in info or "ext" not in info:
            return None  # Invalid URL ya format

        file_path = x.prepare_filename(info)

        # ✅ Check if file already exists
        if os.path.exists(file_path):
            return file_path

        # ✅ Async download
        await loop.run_in_executor(None, x.download, [link])

        return file_path

    except yt_dlp.utils.DownloadError as e:
        print(f"Download Error: {e}")
        return None
