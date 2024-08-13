import asyncio
import random
import asyncio
import time
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from pyrogram import filters, Client

from EsproUser.helper.data import *
from EsproUser import SUDO_USER

@Client.on_message(filters.command(["pornspam", "psm"], ".") & (filters.me | filters.user(SUDO_USER)))
async def prns(client: Client, message: Message):
    r = await message.reply_text("`𝐒ᴀʙᴀʀ 𝐊ᴀʀ 𝐃ᴀʟʟᴇ..`")
    quantity = message.command[1]
    failed = 0
    quantity = int(quantity)
    await r.delete()
    if int(message.chat.id) in GROUP:
        await message.reply_text("`𝐁ᴀᴀᴘ 𝐊ᴇ 𝐆ᴄ 𝐌ᴇ 𝐍ʜɪ 𝐇ᴏɢᴀ 𝐘ᴇ!`")
        return
    for _ in range(quantity):
        try:
            file = random.choice(PORM)            
            await client.send_video(chat_id=message.chat.id, video=file)
        except FloodWait as e:
            await asyncio.sleep(e.x)
