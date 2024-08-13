from pyrogram import Client, filters
from pyrogram.types import Message

from EsproUser import SUDO_USER
from config import *

R = "𝐋ɪʟʏ 𝐔sᴇʀʙᴏᴛ 𝐂ᴍᴅs"

@Client.on_message(filters.command(["help"], ".") & (filters.me | filters.user(SUDO_USER)))
async def help(client: Client, message: Message):
    C = "https://graph.org/file/0d67f6f9439af27bdb52d.jpg"
    CD = """
   ʟɪʟʏ ᴜsᴇʀʙᴏᴛ ʜᴇʟᴘ ᴍᴇɴᴜ
________________________________
           ʙᴏᴛ
`.alive` - ᴄʜᴇᴋ ʙᴏᴛ ᴀʟɪᴠᴇ ᴏʀ ɴᴏᴛ
`.ping` - ᴄʜᴇᴋ ʙᴏᴛ ᴘɪɴɢ
`.restart` - ʀᴇsᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ
`.help` - ᴛᴏ ɢᴇᴛ ᴄᴏᴍᴍᴀɴᴅs

           ʙʀᴏᴀᴅᴄᴀsᴛ
`.gcast` [ᴛᴇxᴛ/ʀᴇᴘʟʏ] - sᴇɴᴅɪɴɢ ɢʟᴏʙᴀʟ ʙʀᴏᴀᴅᴄᴀsᴛ ᴍᴇssᴀɢᴇs ᴛᴏ ᴀʟʟ ɢʀᴏᴜᴘs.
`.gucast` [ᴛᴇxᴛ/ʀᴇᴘʟʏ] - sᴇɴᴅɪɴɢ ɢʟᴏʙᴀʟ ʙʀᴏᴀᴅᴄᴀsᴛ ᴍᴇssᴀɢᴇs ᴛᴏ ᴀʟʟ ɪɴᴄᴏᴍɪɴɢ ᴘʀɪᴠᴀᴛᴇ ᴍᴀssᴀɢᴇs.        

           ᴄʟᴏɴᴇ
`.clone` - ʀᴇᴘʟʏ_ᴍᴇssᴀɢᴇ ғᴏʀ ᴄʟᴏɴᴇ ɪ'ᴅ
`.revert` - ʀᴇᴘʟʏ_ᴍᴇssᴀɢᴇ ᴛᴏ ᴄʟᴏɴᴇʀ to ɢᴇᴛ ʙᴀᴄᴋ

           ᴇᴍᴏᴊɪ
`.emoji` - .ᴇᴍᴏᴊɪ (ɴᴀᴍᴇ)
`.cmoji` - .ᴄᴍᴏᴊɪ (ᴇᴍᴏᴊɪ or ᴛᴇxᴛ) (ɴᴀᴍᴇ)

           ʜᴀɴɢ
 `.hang` - .ʜᴀɴɢ (ɪɴᴛᴇɢᴇʀ)       

           ɪɴᴠɪᴛᴇ
 `.invitesall` - .ɪɴᴠɪᴛᴇsᴀʟʟ @groupusername

           ʀᴀɪᴅ 
`.raid` - .ʀᴀɪᴅ (ᴄᴏᴜɴᴛ) (ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ʀᴇᴘʟʏ_ᴍᴇssᴀɢᴇ)
`.dmraid` - .ᴅᴍʀᴀɪᴅ (ᴄᴏᴜɴᴛ) (ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ʀᴇᴘʟʏ_ᴍᴇssᴀɢᴇ)
`.replyraid` - .ʀᴇᴘʟʏʀᴀɪᴅ (ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ʀᴇᴘʟʏ_ᴍᴇssᴀɢᴇ)
`.lraid` - .ʟʀᴀɪᴅ (ᴄᴏᴜɴᴛ) (ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ʀᴇᴘʟʏ_ᴍᴇssᴀɢᴇ)
`.dmlraid` - .ᴅᴍʟʀᴀɪᴅ (ᴄᴏᴜɴᴛ) (ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ʀᴇᴘʟʏ_ᴍᴇssᴀɢᴇ)

           sᴘᴀᴍ
`.spam` - .sᴘᴀᴍ (ᴄᴏᴜɴᴛ) (ᴍᴇssᴀɢᴇ)
`.sspam` - .ssᴘᴀᴍ (ᴄᴏᴜɴᴛ) (ʀᴇᴘʟʏ_ᴍᴇᴅɪᴀ)
`.delayspam` - .ᴅᴇʟᴀʏsᴘᴀᴍ (ᴛɪᴍᴇ ɪɴ sᴇᴄᴏɴᴅ) (ᴄᴏᴜɴᴛ) (ᴛᴇxᴛ)

           ᴛᴀɢɢᴇʀ
 `.all` - .ᴀʟʟ (ᴍᴇssᴀɢᴇ) - ᴛᴏ sᴛᴀʀᴛ ᴜsᴇʀᴛᴀɢɢᴇʀ
`.cancel` - ᴛᴏ sᴛᴏᴘ ᴛᴀɢɢᴇʀ

            ᴛᴇʟᴇɢʀᴀᴘʜ
`.tm` - .tm (ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏ ᴍᴇᴅɪᴀ) - ᴛᴏ ᴄʀᴇᴀᴛᴇ ᴛᴇʟɪɢʀᴀᴘʜ ʟɪɴᴋ                
"""
    await message.delete()
    await message.reply_photo(photo=C, caption=R)
