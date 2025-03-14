import asyncio, pyrogram

from EsproUser import app, bot, call
from EsproUser import call_decorators
from EsproUser.plugins import load_plugins


loop = asyncio.get_event_loop()

async def init():
    print("Starting all clients ...")
    try:
        await app.start()
        print("User client started.")
        await bot.start()
        print("Bot client started.")
        await call.start()
        print("PyTgCalls client started.")
        await load_plugins()
        print("All plugins loaded.")
        await call_decorators()
    except Exception as e:
        return print(
            f"Error: {e}"
        )
    print("EsproUser Now Started !!")
    await pyrogram.idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    print("EsproUser Now Stopped !!")

