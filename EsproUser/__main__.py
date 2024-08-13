import asyncio
from pyrogram import Client, idle
from EsproUser import client, app

async def start_bot():
    try:
        await app.start()
        print("𝐋ᴏɢ: 𝐅ᴏᴜɴᴅᴇᴅ 𝐁ᴏᴛ 𝐓ᴏᴋᴇɴ 𝐁ᴏᴏᴛɪɴɢ..")
        print("𝐋ɪʟʏ 𝐔sᴇʀʙᴏᴛ 𝐒ᴛᴀʀᴛᴇᴅ")
        await client.start()
        await idle()
    except Exception as e:
        print(f"Error: {e}")

# Run the start_bot coroutine
asyncio.run(start_bot())
