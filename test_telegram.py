import pytest
from telegram import TelegramBot
import errors


@pytest.fixture
def telegram_class():
    return TelegramBot(
        api_id=554,
        api_hash='hwer43ter12',
        session_name='session'
    )


def test_telegram_class_init(telegram_class):
    assert isinstance(telegram_class, TelegramBot)


@pytest.mark.parametrize(
    ('api_id', 'api_hash', 'session_name'), [
        ('123456', 'hash', 'session'),
        (123456, 123456, 'session'),
        (123456, 'hash', 123456),
    ]
)
def test_telegram_class_init_exceptions(api_id, api_hash, session_name):
    with pytest.raises(errors.TelegramTypeError):
        TelegramBot(
            api_id=api_id,
            api_hash=api_hash,
            session_name=session_name
        )


@pytest.mark.parametrize(
    'input_type', [
        [1, 2, 3],
        24000,
        'test_string',
        24.156,
        TelegramBot(api_id=1, api_hash='hash', session_name='session')
    ]
)
def test_get_images_src_dict_exceptions(telegram_class, input_type):
    with pytest.raises(errors.TelegramTypeError):
        telegram_class.get_images_src_dict(input_type)


def test_get_images_src_dict(telegram_class):
    assert telegram_class.get_images_src_dict([]) == dict()
