import re
import logging
from EsproUser import app, call, cdz, eor
from EsproUser import add_to_queue
from EsproUser import download_media_file
from EsproUser import get_media_info, get_media_stream
from pyrogram import filters
from pytgcalls.exceptions import AlreadyJoinedError, GroupCallNotFound, NoActiveGroupCall

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.on_message(cdz(["ply", "play", "vply", "vplay"]) & ~filters.private)
async def start_stream(client, message):
    if message.sender_chat:
        return

    aux = await eor(message, "**🔄 Processing ...**")
    chat_id = message.chat.id
    user_id = message.from_user.id
    mention = message.from_user.mention
    replied = message.reply_to_message

    # Determine media type and download
    media = None
    type = None
    if replied:
        if replied.audio or replied.voice:
            media = await client.download_media(replied)
            type = "Audio"
        elif replied.video or replied.document:
            media = await client.download_media(replied)
            type = "Video"
    else:
        if len(message.command) < 2:
            return await aux.edit("**🥀 Give Me Some Query To Stream Audio Or Video❗...**")
        
        query = message.text.split(None, 1)[1]
        if "https://" in query:
            base = r"(?:https?:)?(?:\/\/)?(?:www\.)?(?:youtu\.be\/|youtube(?:\-nocookie)?\.(?:[A-Za-z]{2,4}|[A-Za-z]{2,3}\.[A-Za-z]{2})\/)?(?:shorts\/|live\/)?(?:watch|embed\/|vi?\/)*(?:\?[\w=&]*vi?=)?([^#&\?\/]{11}).*$"
            resu = re.findall(base, query)
            vidid = resu[0] if resu else None
        else:
            vidid = None

        results = await get_media_info(vidid, query)
        link = str(results[1])
        type = "Video" if message.command[0][0] == "v" else "Audio"
        media = await download_media_file(link, type)

    if not media:
        return await aux.edit("**❌ No Media Found To Stream!**")

    try:
        call_info = await call.get_call(chat_id)
        if call_info.status == "not_playing":
            stream = await get_media_stream(media, type)
            await call.change_stream(chat_id, stream)
            await add_to_queue(chat_id, media=media, type=type)
            await aux.edit("**🎶 Streaming Started!**")
        elif call_info.status in ["playing", "paused"]:
            position = await add_to_queue(chat_id, media=media, type=type)
            await aux.edit(f"**📥 Added to Queue At Position {position}**")
    except GroupCallNotFound:
        try:
            stream = await get_media_stream(media, type)
            await call.join_group_call(chat_id, stream, auto_start=False)
            await add_to_queue(chat_id, media=media, type=type)
            await aux.edit("**🎶 Streaming Started!**")
        except NoActiveGroupCall:
            await aux.edit("**❌ No Active Voice Chat Found!**")
        except AlreadyJoinedError:
            await aux.edit("**🤖 Assistant Already in Voice Chat!**")
        except Exception as e:
            logger.error(f"Error during streaming: {e}")
            await aux.edit("**❌ An Error Occurred. Please Try Again!**")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        await aux.edit("**❌ An Unexpected Error Occurred!**")
