import telegram
import asyncio


async def get_channel_messages():
    # Create a bot instance with your API token
    bot = telegram.Bot(token='6093000872:AAEq5nIqK4YisVNCjBxNP5trD4gM3Wb4GYg')

    # Get the channel ID
    channel_id = '-1001704783944'

    # Get the latest messages from the channel
    messages = await bot.get_chat_messages(channel_id)
    for message in messages:
        print(message.text)


asyncio.run(get_channel_messages())
