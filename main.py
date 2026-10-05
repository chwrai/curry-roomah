import asyncio
from telethon import TelegramClient, utils
import os
from sqlalchemy import create_engine, table, Column, Integer, String, DateTime, Text, insert
from sqlalchemy.ext.declarative import declarative_base

# Replace these values with your own credentials from my.telegram.org
API_ID = int(os.environ['TELEGRAM_API_ID'])
API_HASH = os.environ['TELEGRAM_API_HASH']
PHONE_NUM = os.environ['PHONE_NUM']

# Public group username (without @ or with @) or its invite link (e.g., 'https://t.me/group_username')
GROUP_USERNAME = '@RoomahMY'

# Initialize the client session
client = TelegramClient('anona', API_ID, API_HASH).start(phone=PHONE_NUM)

async def main():

    # iter_messages iterates through the message history.
    # Specify limit to control how many recent messages to fetch.
    messages: list[dict] = []
    async for message in client.iter_messages(GROUP_USERNAME, limit=3):
        # Inspect message details
        # sender = await message.get_sender()
        sender = message.sender
        sender_name = utils.get_display_name(sender)
        # print(f'{sender_name} at {message.date}')

        messages.append({
            "datetime" : message.date,
            "sender_name" : sender_name,
            "message" : message.text})
    
    Base = declarative_base()
    class StgListingData(Base):
        tablename__ = 'stg_listing_data'

        # Note: SQLAlchemy requires at least one primary key column on declarative models
        id = Column(Integer, primary_key=True, autoincrement=True)

        datetime = Column(DateTime, comment='YYYY-MM-DD HH:mm:ss')
        sender_name = Column(String, comment='sender name of the message')
        message = Column(Text, comment='the message')
    
    engine = create_engine("postgresql+psycopg://user:pass@localhost/mydb")
    Base.metadata.create_all(engine)

    with engine.begin() as conn:
            conn.execute(insert(StgListingData), messages)
            
# Run the async main function
with client:
    client.loop.run_until_complete(main())