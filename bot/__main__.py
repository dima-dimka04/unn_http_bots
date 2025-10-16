import time
import bot.telegram_client
import bot.database_client
from bot.dispatcher import Dispatcher
from bot.handlers.database import Database
from bot.handlers.message_echo import MessageEcho
from bot.handlers.photo_echo import PhotoEcho
from bot.long_polling import start_long_polling

def get_next_offset(updates: dict) -> int:
    next_offset = 0
    for update in updates:
        next_offset = max(next_offset, update["update_id"] + 1)
    return next_offset

def main() -> None:
    try:
        dispatcher = Dispatcher()
        # add database handler
        dispatcher.add_handler(Database())
        dispatcher.add_handler(MessageEcho())
        dispatcher.add_handler(PhotoEcho())
        # add photo handler
        start_long_polling(dispatcher)
    except KeyboardInterrupt:
        print("\nBye:)")

if __name__ == "__main__":
    main()