import asyncio
import os
import yt_dlp


async def download_media_file(link: str, media_type: str):
    loop = asyncio.get_running_loop()

    # Common yt-dlp Options
    ydl_opts = {
        "outtmpl": "downloads/%(id)s.%(ext)s",
        "geo_bypass": True,
        "nocheckcertificate": True,
        "quiet": True,
        "no_warnings": True,
        "cookiefile": ".youtube.com	TRUE	/	TRUE	1775469618	PREF	f6=40000000&tz=Asia.Calcutta&f7=100
.youtube.com	TRUE	/	TRUE	1740911396	GPS	1
.youtube.com	TRUE	/	TRUE	1772445598	__Secure-1PSIDTS	sidts-CjIBEJ3XV1J4ipYlopZ_yakN9aom9HQHGhwbmZBfAj57wYa04K1-tKcdz-8HItGrS11rhRAA
.youtube.com	TRUE	/	TRUE	1772445598	__Secure-3PSIDTS	sidts-CjIBEJ3XV1J4ipYlopZ_yakN9aom9HQHGhwbmZBfAj57wYa04K1-tKcdz-8HItGrS11rhRAA
.youtube.com	TRUE	/	TRUE	0	__Secure-3PAPISID	Ub4WxUlg8oom9kzr/A9qd0nZqVWDcxgvnd
.youtube.com	TRUE	/	TRUE	0	__Secure-3PSID	g.a000uQimMN6zxhTC6nEQm1fvel7gKcApU-S0huO4pOtsZnAqAtgZBLyQH2f5bcR1Ne1FofP8mAACgYKAc0SARMSFQHGX2MifKS5WU1iOQUSsWj9d7S5hhoVAUF8yKoee8OLBk2fZcDkmfs5_-I00076
.youtube.com	TRUE	/	TRUE	1775469598	LOGIN_INFO	AFmmF2swRgIhAMdSqQcOFQcDyMJBUFS0ehn0_sAIudO_Ff-4l2zR6pWMAiEAgn4JBpkGkQqFkH8hBIc4tSkXqflxibdKpzrsIjvy-S8:QUQ3MjNmeFdaNEtOd1FzRUhFOGJabmt3UmNJbmdWNDdXeGdrVTFlTmtYVkM2OHhmZ1YzRzZyZl9GU0ZsYWxRbWNGQzhXZ0NKamxRSm1HS3JCTktkdGowWkFXM1NrQnlmWHAxT1Q3cktSOWhnbU9scTNBcjdpVVNUMUU5bE5TU0x5Umd5U1ZVWjR2cVJOVXUtRnJRYmh5cklOcTlkeXg2bTVR
.youtube.com	TRUE	/	TRUE	1740910230	CONSISTENCY	AKreu9si1aIKeYF_-tr92doFE8jo9HsJ1Ztj-E8j_rnwLQxt3WY7aGFclq_7NMnK41JXsdKeeBw_WMldkBoYJan7uBvBDAgZz66UWR_Xfin7GHb8NC4tQzU4rqA
.youtube.com	TRUE	/	TRUE	1772445823	__Secure-3PSIDCC	AKEyXzUtBhSstT2kKxfnK7qUH0FWqmILzJ6gJOvUG7mMPp5S62zcV-8qVa83HoUcmcu5yosQ0A",  # Cookies Support Added
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
