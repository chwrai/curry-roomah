import asyncio
from telethon import TelegramClient, utils
import os

# Replace these values with your own credentials from my.telegram.org
API_ID = int(os.environ['API_ID'])
API_HASH = os.environ['API_HASH']
PHONE_NUM = os.environ['PHONE_NUM']

# Public group username (without @ or with @) or its invite link (e.g., 'https://t.me/group_username')
GROUP_USERNAME = '@RoomahMY'

# Initialize the client session
client = TelegramClient('anona', API_ID, API_HASH).start(phone=PHONE_NUM)

async def main():

    # iter_messages iterates through the message history.
    # Specify limit to control how many recent messages to fetch.
    async for message in client.iter_messages(GROUP_USERNAME, limit=3):
        # Inspect message details
        # sender = await message.get_sender()
        sender = message.sender
        sender_name = utils.get_display_name(sender)
        print(f'{sender_name}')
        
        # print(f"[{message.date}] {sender_name} (ID {message.id}):")
        # print(f"  {message.text}")
        # print("-" * 40)

# Run the async main function
with client:
    client.loop.run_until_complete(main())