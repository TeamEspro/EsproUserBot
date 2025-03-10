from EsproUser import config
from EsproUser.modules import queues
from EsproUser.modules.clients import app, call
from EsproUser.modules.streams import get_media_stream
from pyrogram import filters
from pyrogram.types import Message
from pytgcalls.types import Update
from pytgcalls.types.stream import StreamAudioEnded
from typing import Union, List


def cdx(commands: Union[str, List[str]]):
    return filters.command(commands, config.COMMAND_PREFIXES)

def cdz(commands: Union[str, List[str]]):
    return filters.command(commands, config.COMMAND_HANDLERS)


async def eor(message: Message, *args, **kwargs) -> Message:
    try:
        msg = (
            message.edit_text
            if bool(message.from_user and message.from_user.is_self or message.outgoing)
            else (message.reply_to_message or message).reply_text
        )
    except:
        msg = (
            message.edit_text
            if bool(message.from_user and message.outgoing)
            else (message.reply_to_message or message).reply_text
        )
    
    return await msg(*args, **kwargs)


async def call_decorators():
    @call.on_update
    async def update_handler(client, update: Update):
        if isinstance(update, StreamAudioEnded):
            chat_id = update.chat_id
            await queues.task_done(chat_id)
            queue_empty = await queues.is_queue_empty(chat_id)
            if queue_empty:
                try:
                    await call.leave_group_call(chat_id)
                except Exception as e:
                    print(f"Error leaving group call: {e}")
            else:
                check = await queues.get_from_queue(chat_id)
                media = check["media"]
                type = check["type"]
                stream = await get_media_stream(media, type)
                await call.change_stream(chat_id, stream)
                await app.send_message(chat_id, "Streaming ...")
