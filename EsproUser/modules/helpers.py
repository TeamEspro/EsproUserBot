import os
import yt_dlp

# Download folder ensure kare
DOWNLOAD_FOLDER = "downloads"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

# Cookies file ka path
COOKIES_FILE = "cookies.txt"

def download_with_cookies(url, media_type):
    """ YouTube se login-based content download karega cookies ke saath """

    ydl_opts = {
        "cookiefile": COOKIES_FILE,
        "outtmpl": os.path.join(DOWNLOAD_FOLDER, "%(id)s.%(ext)s"),
        "geo_bypass": True,
        "nocheckcertificate": True,
        "quiet": True,
        "no_warnings": True,
    }

    if media_type.lower() == "audio":
        ydl_opts.update({
            "format": "bestaudio",
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }],
        })
    elif media_type.lower() == "video":
        ydl_opts["format"] = "(bestvideo[height<=?720][width<=?1280][ext=mp4])+(bestaudio[ext=m4a])"
    else:
        raise ValueError("Invalid media type! Use 'Audio' or 'Video'.")

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    
    print(f"✅ {media_type} Downloaded Successfully!")

# Example Usage
video_url = "https://www.youtube.com/watch?v=PRIVATE_VIDEO_ID"
download_with_cookies(video_url, "Audio")  # Ya "Video"
