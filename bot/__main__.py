import time
import bot.telegram_client
import bot.database_client
from bot.dispatcher import Dispatcher
from bot.handlers.database import Database
from bot.handlers.message_echo import MessageEcho
from bot.handlers.photo_echo import PhotoEcho
from bot.long_polling import start_long_polling

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