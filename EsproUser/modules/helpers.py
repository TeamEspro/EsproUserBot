import os
import yt_dlp

# Cookies file ka path
COOKIES_FILE = "cookies.txt"

def download_media_file(url, download_audio=False, output_dir="downloads"):
    """
    YouTube ya kisi bhi site se video/audio download karega cookies ke support ke saath.

    Parameters:
    - url (str): Video ka URL
    - download_audio (bool): Agar True hai to sirf audio download hoga, warna video.
    - output_dir (str): Downloaded file ka folder

    Returns:
    - str: Downloaded file ka path ya error message.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Download options
    ydl_opts = {
        "outtmpl": f"{output_dir}/%(title)s.%(ext)s",
        "geo_bypass": True,
        "nocheckcertificate": True,
        "quiet": False,
        "no_warnings": True,
        "cookiefile": COOKIES_FILE,  # Cookies ka support
    }

    # Audio mode agar True hai to
    if download_audio:
        ydl_opts["format"] = "bestaudio/best"
        ydl_opts["postprocessors"] = [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ]
    else:
        ydl_opts["format"] = "bestvideo+bestaudio/best"

    # Download start
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            file_path = ydl.prepare_filename(info_dict)
            return f"Downloaded: {file_path}"
    except Exception as e:
        return f"Error: {str(e)}"

# Example Usage:
video_url = input("Enter the video URL: ")
mode = input("Download Audio only? (yes/no): ").strip().lower()
download_audio = mode == "yes"

result = download_video_audio(video_url, download_audio)
print(result)
