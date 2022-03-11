class TelegramTypeError(Exception):
    def __init__(
        self,
        function_name: str,
        message: str,
        expected_type: type,
        got_type: type
    ):
        self.source_message = 'Got "TypeError" in function "{}"\n'.format(
            function_name
        )
        self.message = '{}. Expected {} type, but got {}\n'.format(
            message,
            expected_type,
            got_type
        )

    def __str__(self):
        return self.source_message + self.message


class TelegramArgumentEmpty(Exception):
    def __init__(
        self,
        function_name: str,
        message: str,
        expected_type: type,
    ):
        self.source_message = 'Got "ArgumentError" in function "{}"\n'.format(
            function_name
        )
        self.message = '{}. Invalid type of argument. Expected type {}'.format(
            message,
            expected_type,
        )

    def __str__(self):
        return self.source_message + self.message
