import os
from telethon import TelegramClient, events
from dotenv import load_dotenv
from plugins import load_plugins

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
SESSION = os.getenv("SESSION")

client = TelegramClient(SESSION, API_ID, API_HASH)

client.start()

prefixes = [r'\.', r'\/', r'!', r'\$', r'~', r'∆', r'\?']
prefix_pattern = f"^[{''.join(prefixes)}]"

@client.on(events.NewMessage(pattern=f'{prefix_pattern}start'))
async def start_handler(event):
    await event.reply("Hello! I'm AlphaX, your Telethon-based userbot. Type a command to get started!")

load_plugins(client)
client.run_until_disconnected()
