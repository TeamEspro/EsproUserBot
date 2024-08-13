import os
import shutil
import asyncio
from pyrogram.types import Message
from pyrogram import filters, Client
from EsproUser import SUDO_USER

@Client.on_message(filters.command(["restart", "reload", "rs", "rl"], ".") & (filters.me | filters.user(SUDO_USER)))
async def restart(client: Client, message: Message):
    reply = await message.reply_text("**𝐉ᴀᴀɴ 𝐇ᴏ 𝐑ᴀʜᴀ 𝐑ᴇsᴛᴀʀᴛ...**")
    await message.delete()
    await reply.edit_text("Successfully 𝐑ᴇsᴛᴀʀᴛᴇᴅ 𝐋ɪʟʏ 𝐔sᴇʀʙᴏᴛ...\n\n🐼 𝟏-𝟐 𝐌ɪɴ 𝐒ᴀʙᴀʀ 𝐊ᴀʀᴏ\n𝐏ʟᴜɢɪɴs 𝐋ᴏᴀᴅ 𝐇ᴏ 𝐑ᴀʜᴇ...</b>")
    os.system(f"kill -9 {os.getpid()} && python3 -m EsproUser")
