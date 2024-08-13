import os
import sys
import asyncio
from time import time
from datetime import datetime
from pyrogram import __version__, filters, Client
from pyrogram.types import Message
from platform import python_version
from EsproUser import SUDO_USER
from config import*

START_TIME = datetime.utcnow()
TIME_DURATION_UNITS = (
    ('Week', 60 * 60 * 24 * 7),
    ('Day', 60 * 60 * 24),
    ('Hour', 60 * 60),
    ('Min', 60),
    ('Sec', 1)
)
async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)


@Client.on_message(filters.command(["alive"], ".") & (filters.me | filters.user(SUDO_USER)))
async def alive(client: Client, message: Message):
    start = time()
    current_time = datetime.utcnow()
    ping = time() - start
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    txt = (
        f"❥︎• 𝐀ʟ𝐈ᴠ𝐄 \n\n"
        f"❥︎• 𝐕ᴇ𝐑s𝐈ᴏ𝐍 2.0\n"
        f"❥︎• 𝐏ɪ𝐍ɢ {ping * 1000:.3f}𝐌s\n"
        f"❥︎• 𝐒ᴛ𝐀ʀ𝐓•~•𝐓ɪ𝐌ᴇ {uptime}\n"
        f"❥︎• 𝐏ʏ𝐓ʜ𝐎ɴ {python_version()}`\n"
        f"❥︎• 𝐏ʏ𝐑ᴏ𝐆ʀ𝐀ᴍ {__version__}\n"
        f"❥︎• 𝐃ᴇ𝐕ᴇ𝐋ᴏ𝐏ᴇ𝐑 {client.me.mention}"    
    )
    await message.delete()
    await message.reply_photo(photo=ALIVE_PIC, caption=txt)

@Client.on_message(filters.command(["ping"], ".") & (filters.me | filters.user(SUDO_USER)))
async def ping(client: Client, message: Message):
    r = await message.reply_text("**𝐏ᴏ𝗡ɢ**")
    start = time()
    current_time = datetime.utcnow()
    ping = time() - start
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.delete()
    await r.edit(
        f"★𝐖ᴇ𝐋ᴄ𝐎ᴍ𝐄★𝐊ᴀ𝐑ᴏ★𝐁ᴀ𝐀ᴘ★𝐀ᴀ𝐘ᴀ★𝐓ᴜ𝐌ʜ𝐀ʀ𝐀★\n\n"
        f"❥︎• 𝐏ɪ𝐍ɢ {ping * 1000:.3f}𝐌s\n"
        f"❥︎• 𝐒ᴛ𝐀ʀ𝐓•~•𝐓ɪ𝐌ᴇ {uptime}\n"
        f"❥︎• 𝐃ᴇ𝐕ᴇ𝐋ᴏ𝐏ᴇ𝐑 {client.me.mention}"
    )
