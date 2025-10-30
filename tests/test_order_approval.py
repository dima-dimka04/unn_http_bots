from bot.dispatcher import Dispatcher
from bot.handlers.order_approval import OrderApprovalHandler
from tests.mocks import Mock


def test_order_approval_handler_approve():
    test_update = {
        "callback_query": {
            "id": "q1",
            "from": {"id": 222},
            "data": "order_approve",
            "message": {"chat": {"id": 333}, "message_id": 444},
        }
    }

    update_state_called = False
    delete_message_called = False
    send_message_called = False

    def update_user_state(telegram_id: int, state: str):
        nonlocal update_state_called
        update_state_called = True
        assert telegram_id == 222
        assert state == "ORDER_FINISHED"

    def deleteMessage(chat_id: int, message_id: int):
        nonlocal delete_message_called
        delete_message_called = True
        assert chat_id == 333
        assert message_id == 444

    def sendMessage(chat_id: int, text: str, **kwargs):
        nonlocal send_message_called
        send_message_called = True
        assert chat_id == 333
        assert "✅ **Order Confirmed!**" in text
        return {"ok": True}

    def get_user(telegram_id: int) -> dict | None:
        assert telegram_id == 222
        return {"state": "WAIT_FOR_ORDER_APPROVE", "order_json": "{}"}

    mock_storage = Mock({"update_user_state": update_user_state, "get_user": get_user})
    mock_messenger = Mock({"deleteMessage": deleteMessage, "sendMessage": sendMessage})

    dispatcher = Dispatcher(mock_storage, mock_messenger)
    handler = OrderApprovalHandler()
    dispatcher.add_handler(handler)
    dispatcher._storage.get_user
    dispatcher.dispatch(test_update)

    assert update_state_called
    assert delete_message_called
    assert send_message_called


def test_order_approval_handler_restart():
    test_update = {
        "callback_query": {
            "id": "q2",
            "from": {"id": 777},
            "data": "order_restart",
            "message": {"chat": {"id": 888}, "message_id": 999},
        }
    }

    clear_called = False
    update_state_called = False
    send_message_called = False
    delete_message_called = False

    def get_user(telegram_id: int) -> dict | None:
        assert telegram_id == 777
        return {"state": "WAIT_FOR_ORDER_APPROVE", "order_json": "{}"}

    def clear_user_state_and_order(telegram_id: int):
        nonlocal clear_called
        clear_called = True
        assert telegram_id == 777

    def update_user_state(telegram_id: int, state: str):
        nonlocal update_state_called
        update_state_called = True
        assert telegram_id == 777
        assert state == "WAIT_FOR_PIZZA_NAME"

    def sendMessage(chat_id: int, text: str, **kwargs):
        nonlocal send_message_called
        send_message_called = True
        assert chat_id == 888
        assert "Please choose pizza type" in text
        return {"ok": True}

    def deleteMessage(chat_id: int, message_id: int):
        nonlocal delete_message_called
        delete_message_called = True
        assert chat_id == 888
        assert message_id == 999

    mock_storage = Mock(
        {
            "clear_user_state_and_order": clear_user_state_and_order,
            "update_user_state": update_user_state,
            "get_user": get_user,
        }
    )
    mock_messenger = Mock({"sendMessage": sendMessage, "deleteMessage": deleteMessage})

    dispatcher = Dispatcher(mock_storage, mock_messenger)
    handler = OrderApprovalHandler()
    dispatcher.add_handler(handler)
    dispatcher._storage.get_user
    dispatcher.dispatch(test_update)

    assert clear_called
    assert update_state_called
    assert send_message_called
    assert delete_message_called
