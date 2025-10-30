from bot.dispatcher import Dispatcher
from bot.handlers.pizza_name import PizzaSelectionHandler
from tests.mocks import Mock


def test_pizza_selection_handler():
    test_update = {
        "callback_query": {
            "id": "123",
            "from": {"id": 12345},
            "data": "pizza_margherita",
            "message": {"chat": {"id": 54321}, "message_id": 10},
        }
    }

    update_order_called = False
    update_state_called = False
    delete_message_called = False
    send_message_called = False

    def update_user_order_json(telegram_id: int, order_json: dict):
        nonlocal update_order_called
        update_order_called = True
        assert telegram_id == 12345
        assert order_json == {"pizza_name": "Margherita"}

    def update_user_state(telegram_id: int, state: str):
        nonlocal update_state_called
        update_state_called = True
        assert telegram_id == 12345
        assert state == "WAIT_FOR_PIZZA_SIZE"

    def deleteMessage(chat_id: int, message_id: int):
        nonlocal delete_message_called
        delete_message_called = True
        assert chat_id == 54321
        assert message_id == 10

    def sendMessage(chat_id: int, text: str, **kwargs):
        nonlocal send_message_called
        send_message_called = True
        assert chat_id == 54321
        assert "Please select pizza size" in text
        return {"ok": True}

    def get_user(telegram_id: int) -> dict | None:
        assert telegram_id == 12345
        return {"state": "WAIT_FOR_PIZZA_NAME", "order_json": "{}"}

    mock_storage = Mock(
        {
            "update_user_order_json": update_user_order_json,
            "update_user_state": update_user_state,
            "get_user": get_user,
        }
    )
    mock_messenger = Mock({"deleteMessage": deleteMessage, "sendMessage": sendMessage})

    dispatcher = Dispatcher(mock_storage, mock_messenger)
    handler = PizzaSelectionHandler()
    dispatcher.add_handler(handler)

    dispatcher._storage.get_user

    dispatcher.dispatch(test_update)

    assert update_order_called
    assert update_state_called
    assert delete_message_called
    assert send_message_called
