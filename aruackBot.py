from telethon import TelegramClient, events
from datetime import datetime


api_id = 12074809 
api_hash = "5a4375075d75333d63684a9afd80852e" 

client = TelegramClient("startup", api_id, api_hash)


aruackGif = "https://telegra.ph/file/42724a16f927fc339dc6c.mp4"
aruackAlive = f"""
Aruack Bot Iz Alive\n
La La La! La La La!\n
 Version:- 1.0

Aruack Bot Is Running Properly
"""

@client.on(events.NewMessage(outgoing=True, pattern=".alive"))
async def alive(event):
    chat = event.chat_id
    await client.send_file(chat, aruackGif, caption=aruackAlive)
    await event.delete()


@client.on(events.NewMessage(outgoing=True, pattern=".ping"))
async def ping(event):
    start = datetime.now()
    testPing = await client.edit_message(event.message, "AruackBot Ping")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    aruackPing = f"Aruack Bot Ping Here\nPing:- {ms}"
    await event.client.send_file(event.chat_id, aruackGif, caption=AruackPing)
    await event.delete()


client.start()
client.run_until_disconnected()