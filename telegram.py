import errors


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

    def get_messages_list(self) -> list:
        pass

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


# if __name__ == '__main__':
#     bot = TelegramBot(
#         api_id=100,
#         api_hash='asdfges432',
#         session_name='session'
#     )
#     bot.get_images_src_dict([])
