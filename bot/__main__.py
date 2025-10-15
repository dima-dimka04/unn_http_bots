import time
import bot.telegram_client
import bot.database_client
from bot.dispatcher import Dispatcher
from bot.handlers.message_echo import MessageEcho
from bot.long_polling import start_long_polling

def get_next_offset(updates: dict) -> int:
    next_offset = 0
    for update in updates:
        next_offset = max(next_offset, update["update_id"] + 1)
    return next_offset

def main() -> None:
    try:
        dispatcher = Dispatcher()
        dispatcher.add_handler(MessageEcho())
        start_long_polling(dispatcher)
    except KeyboardInterrupt:
        print("\nBye:)")

if __name__ == "__main__":
    main()