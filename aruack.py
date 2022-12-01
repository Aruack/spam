import asyncio
import sys
from sys import argv
from telethon import TelegramClient, events


API_ID = 2184829
API_HASH = "6930b92388baabff4cb4a1d377085035"

async def main():
    main.AruackBot = TelegramClient("AruackSpamBot", api_id=API_ID, api_hash=API_HASH)
    await main.AruackBot.start()
    await main.AruackBot.send_message("me", "Auto Gameplay Bot Deployed Successfully!")

    @main.AruackBot.on(events.NewMessage(outgoing=True, pattern='.spam'))      
    async def spam(e):
        text = e.raw_text
        counts = int(text[6:9])
        spam = text[9:]
        message = str(spam)
        for i in range(counts):
            await main.AruackBot.send_message(e.chat_id, message)
            await asyncio.sleep(3)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())

if len(argv) not in (1, 3, 4):
    try:
        main.AruackBot.disconnect()
    except Exception as e:
        print(e)
        pass
else:
    try:
        main.AruackBot.run_until_disconnected()
    except Exception as e:
        print(e)
        pass
