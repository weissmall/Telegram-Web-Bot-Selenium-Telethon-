from telethon import TelegramClient
import asyncio
from telethon.tl.types import InputMessagesFilterPhotos


async def get_images(session_name, api_id, api_hash, chat_id, limit):
    result = dict()

    client = TelegramClient(session_name, api_id, api_hash)
    async with client:
        await client.start()
        async for message in client.iter_messages(
            chat_id,
            filter=InputMessagesFilterPhotos,
            limit=limit
        ):
            if message.media is not False:
                temp = await client.download_media(message.media, 'images/')
                result[message.id] = temp

        return result


def run_get_images():
    result = asyncio.run(get_images(
        api_hash='3778859a51ffe2951f3abe886d03d0f1',
        api_id=7212719,
        session_name='session',
        chat_id='https://t.me/moodnight_af',
        limit=5
    ))

    return result


if __name__ == '__main__':
    run_get_images()
