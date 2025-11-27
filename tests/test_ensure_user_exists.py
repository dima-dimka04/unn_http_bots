import pytest
from bot.dispatcher import Dispatcher
from bot.handlers.ensure_user_exists import EnsureUserExists
from tests.mocks import Mock


@pytest.mark.asyncio
async def test_ensure_user_exists_handler():
    test_update = {
        "update_id": 111,
        "message": {
            "from": {
                "id": 999,
                "first_name": "TestUser",
            },
            "text": "any text",
        },
    }

    ensure_user_called = False

    async def ensure_user_exists(telegram_id: int):
        nonlocal ensure_user_called
        ensure_user_called = True
        assert telegram_id == 999

    async def get_user(telegram_id: int) -> dict | None:
        assert telegram_id == 999
        return None

    mock_storage = Mock(
        {"ensure_user_exists": ensure_user_exists, "get_user": get_user}
    )
    mock_messenger = Mock({})

    dispatcher = Dispatcher(mock_storage, mock_messenger)
    handler = EnsureUserExists()
    dispatcher.add_handler(handler)

    await dispatcher.dispatch(test_update)

    assert ensure_user_called
