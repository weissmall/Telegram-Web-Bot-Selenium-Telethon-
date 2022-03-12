import errors
from telethon import TelegramClient
import asyncio


class TelegramBot():

    def __init__(
        self,
        session_name: str = 'default_session',
        api_id: int = 123,
        api_hash: str = 'None'
    ):

        if api_id is None:
            raise errors.TelegramArgumentEmpty(
                '__init__()',
                'Need to enter valid "api_id"',
                int
            )

        if not isinstance(api_id, int):
            raise errors.TelegramTypeError(
                '__init__()',
                'Incorrect type of "messages" arg',
                int,
                type(api_id)
            )

        if api_hash is None:
            raise errors.TelegramArgumentEmpty(
                '__init__()',
                'Need to enter valid "api_hash"',
                str
            )

        if not isinstance(api_hash, str):
            raise errors.TelegramTypeError(
                '__init__()',
                'Incorrect type of "messages" arg',
                str,
                type(api_hash)
            )

        if not isinstance(session_name, str):
            raise errors.TelegramTypeError(
                '__init__()',
                'Incorrect type of "session_name" arg',
                str,
                type(session_name)
            )

        self.session_name = session_name
        self.api_id = api_id
        self.api_hash = api_hash

    async def start_session(self):
        self.client = TelegramClient(
            self.session_name,
            self.api_id,
            self.api_hash
        )

        await self.client.start()

    def __get_messages_list(self, group_id: int | str):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(
            self.__get_messages_list(group_id)
        )

    async def get_messages_list(self, group_id: int | str) -> list:
        if not isinstance(group_id, int) and not isinstance(group_id, str):
            raise errors.TelegramTypeError(
                'get_messages_list()',
                'Incorrect type of "group_id"',
                str,
                type(group_id)
            )

        result = list()
        async with self.client:
            async for message in self.client.get_messages(group_id):
                result.append(message)

        return result

    def get_images_src_dict(self, messages: list) -> dict:
        if not isinstance(messages, list):
            raise errors.TelegramTypeError(
                'get_images_src_dict()',
                'Incorrect type of "messages" arg',
                list,
                type(messages)
            )

        output_dict = dict()
        for message in messages:
            try:
                output_dict[message.id] = message.img.src
            except AttributeError:
                raise errors.TelegramTypeError(
                    'get_images_src_dict()',
                    'Incorrect type of "messages" arg',
                    list,
                    type(messages)
                )

        return output_dict


async def main():
    bot = TelegramBot(
        api_id=7212719,
        api_hash='3778859a51ffe2951f3abe886d03d0f1',
        session_name='session'
    )
    await bot.start_session()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(bot.get_messages_list(
        'https://t.me/gray_kardinal_chat'
    ))


if __name__ == '__main__':
    asyncio.run(main())
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())
    # main()
