from telethon import TelegramClient
import asyncio
from telethon.tl.types import InputMessagesFilterPhotos


async def get_images(
    session_name: str,
    api_id: int,
    api_hash: str,
    chat_id: str,
    limit: int,
    absolute_path: str
):
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
                temp = await client.download_media(
                    message.media,
                    apply_path(absolute_path, 'images/')
                )
                result[message.id] = temp

        return result


def apply_path(abs_path, img_path):
    return '{}{}'.format(abs_path, img_path)


async def __get_media_by_id(
    session_name,
    api_id,
    api_hash,
    chat_id,
    message_id
):
    client = TelegramClient(session_name, api_id, api_hash)
    async with client:
        await client.start()
        await client.get_messages(chat_id, ids=message_id)

        result = list()
        message = await client.get_messages(chat_id, ids=message_id)
        if message.grouped_id is None:
            if message.media is not False:
                temp = await client.download_media(
                    message.media,
                    'images/'
                )
                result.append(temp)
        else:
            grouped_id = message.grouped_id
            while message.grouped_id == grouped_id:
                if message.media is not False:
                    temp = await client.download_media(
                        message.media,
                        'images/'
                    )
                    result.append(temp)
                message_id += 1
                message = await client.get_messages(chat_id, ids=message_id)

        return result


def get_media_by_id(session_name, api_id, api_hash, chat_id, message_id):
    return asyncio.run(__get_media_by_id(
        api_hash=api_hash,
        api_id=api_id,
        session_name=session_name,
        chat_id=chat_id,
        message_id=message_id
    ))


def run_get_images(
    api_hash,
    api_id,
    session_name,
    chat_id,
    limit,
    absolute_path
):
    return asyncio.run(get_images(
        api_hash=api_hash,
        api_id=api_id,
        session_name=session_name,
        chat_id=chat_id,
        limit=limit,
        absolute_path=absolute_path
    ))


if __name__ == '__main__':
    # run_get_images(
    #     api_hash='3778859a51ffe2951f3abe886d03d0f1',
    #     api_id=7212719,
    #     session_name='session',
    #     chat_id='https://t.me/moodnight_af',
    #     limit=5
    # )

    res = get_media_by_id(
        api_hash='3778859a51ffe2951f3abe886d03d0f1',
        api_id=7212719,
        session_name='session',
        chat_id='https://t.me/moodnight_af',
        message_id=114
    )
    print(res)

    # grouped_id=13176146443563802
    # grouped_id=13176146443563802
