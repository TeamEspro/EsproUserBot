import os
import sys
import asyncio
from random import choice
from pyrogram import Client, filters
from pyrogram.types import Message

from EsproUser import SUDO_USER
from EsproUser.helper.data import *


@Client.on_message(filters.command(["raid", "r"], ".") & (filters.me | filters.user(SUDO_USER)))
async def raid(app: Client, m: Message):  
      EsproUser = "".join(m.text.split(maxsplit=1)[1:]).split(" ", 2)
      if len(EsproUser) == 2:
        counts = int(EsproUser[0])
        username = EsproUser[1]
        if not counts:
          await m.reply_text(f"𝐑ᴀɪᴅ 𝐋ɪᴍɪᴛ 𝐍ᴏᴛ 𝐅ᴏᴜɴᴅ 𝐏ʟᴇᴀsᴇ 𝐆ɪᴠᴇ 𝐂ᴏᴜɴᴛ!")
          return       
        if not username:
          await m.reply_text("𝐘ᴏᴜ 𝐍ᴇᴇᴅ 𝐓ᴏ 𝐒ᴘᴇᴄɪғʏ 𝐀ɴ 𝐔sᴇʀ! 𝐑ᴇᴘʟʏ 𝐓ᴏ 𝐀ɴʏ 𝐔𝐬ᴇʀ 𝐎ʀ 𝐆ɪᴠᴇ 𝐈ᴅ/𝐔𝐬ᴇʀɴᴀᴍᴇ")
          return
        try:
           user = await app.get_users(EsproUser[1])
        except:
           await m.reply_text("**𝐋ᴇʟᴇ 𝐋ᴀᴜᴅᴀ 𝐄ʀʀᴏʀ 𝐀ᴀɢʏᴀ:** 𝐔sᴇʀ 𝐍ᴏᴛ 𝐅ᴏᴜɴᴅ 𝐎ʀ 𝐌ᴀʏ 𝐁ᴇ 𝐃ᴇʟᴇᴛᴇᴅ!")
           return
      elif m.reply_to_message:
        counts = int(EsproUser[0])
        try:
           user = await app.get_users(m.reply_to_message.from_user.id)
        except:
           user = m.reply_to_message.from_user 
      else:
        await m.reply_text("𝐔sᴀɢᴇ: .𝐑ᴀɪᴅ 𝐂ᴏᴜɴᴛ 𝐔sᴇʀɴᴀᴍᴇ 𝐎ʀ 𝐑ᴇᴘʟʏ")
        return
      if int(m.chat.id) in GROUP:
         await m.reply_text("**𝐒ᴏʀʀʏ || 𝐏ᴀʀ 𝐘ᴀʜᴀ 𝐒ᴘᴀᴍ 𝐍ʜɪ 𝐇ᴏ 𝐒ᴀᴋᴛᴀ.**")
         return
      if int(user.id) in VERIFIED_USERS:
         await m.reply_text("𝐒ᴏʀʀʏ 𝐀ᴘ 𝐀ᴘɴᴇ 𝐁ᴀᴀᴘ 𝐏ᴀʀ 𝐑ᴀɪᴅ 𝐍ʜɪ 𝐊ᴀʀ 𝐒ᴀᴋᴛᴇ")
         return
      if int(user.id) in SUDO_USER:
         await m.reply_text("𝐒ᴜᴅᴏ 𝐑ᴀɴᴅɪ 𝐏ᴀʀ 𝐑ᴀɪᴅ 𝐍ʜɪ 𝐇ᴏɢᴀ.")
         return
      mention = user.mention
      for _ in range(counts): 
         r = f"{mention} {choice(RAID)}"
         await app.send_message(m.chat.id, r)
         await asyncio.sleep(0.3)


@Client.on_message(filters.command(["dmraid", "dmr"], ".") & (filters.me | filters.user(SUDO_USER)))
async def draid(app: Client, m: Message):  
      EsproUser = "".join(m.text.split(maxsplit=1)[1:]).split(" ", 2)
      if len(EsproUser) == 2:
        counts = int(EsproUser[0])
        username = EsproUser[1]
        if not counts:
          await m.reply_text(f"𝐑ᴀɪᴅ 𝐋ɪᴍɪᴛ 𝐍ᴏᴛ 𝐅ᴏᴜɴᴅ 𝐏ʟᴇᴀsᴇ 𝐆ɪᴠᴇ 𝐂ᴏᴜɴᴛ!")
          return       
        if not username:
          await m.reply_text("𝐘ᴏᴜ 𝐍ᴇᴇᴅ 𝐓ᴏ 𝐒ᴘᴇᴄɪғʏ 𝐀ɴ 𝐔sᴇʀ! 𝐑ᴇᴘʟʏ 𝐓ᴏ 𝐀ɴʏ 𝐔sᴇʀ 𝐎ʀ 𝐆ɪᴠᴇ 𝐈ᴅ/𝐔sᴇʀɴᴀᴍᴇ")
          return
        try:
           user = await app.get_users(EsproUser[1])
        except:
           await m.reply_text("**𝐋ᴇʟᴇ 𝐋ᴀᴜᴅᴀ 𝐀ᴀɢʏᴀ 𝐄ʀʀᴏʀ:** 𝐔sᴇʀ 𝐍ᴏᴛ 𝐅ᴏᴜɴᴅ 𝐎ʀ 𝐌ᴀʏ 𝐁ᴇ 𝐃ᴇʟᴇᴛᴇᴅ!")
           return
      elif m.reply_to_message:
        counts = int(EsproUser[0])
        try:
           user = await app.get_users(m.reply_to_message.from_user.id)
        except:
           user = m.reply_to_message.from_user 
      else:
        await m.reply_text("𝐔sᴀɢᴇ: .𝐃ᴍʀᴀɪᴅ 𝐂ᴏᴜɴᴛ 𝐔sᴇʀɴᴀᴍᴇ 𝐎ʀ 𝐑ᴇᴘʟʏ")
        return
      if int(user.id) in VERIFIED_USERS:
         await m.reply_text("𝐒ᴏʀʀʏ 𝐀ᴘ 𝐀ᴘɴᴇ ʙᴀᴀᴘ 𝐏ᴀʀ 𝐒ᴘᴀᴍ 𝐍ʜɪ 𝐊ᴀʀ 𝐒ᴀᴋᴛᴇ")
         return
      if int(user.id) in SUDO_USER:
         await m.reply_text("𝐋ᴇʟᴇ 𝐋ᴀᴜᴅᴀ 𝐀ᴀɢʏᴀ 𝐄ʀʀᴏʀ.")
         return
      mention = user.mention
      await m.reply_text("𝐃ᴍ 𝐌ᴇ 𝐂ʜᴜᴅᴀɪ 𝐒ʜᴜʀᴜ 𝐇ᴏ 𝐆ʏᴀ..")
      for _ in range(counts): 
         r = f"{choice(RAID)}"
         await app.send_message(user.id, r)
         await asyncio.sleep(0.3)
