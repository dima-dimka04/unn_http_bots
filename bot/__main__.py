import time
from bot.dispatcher import Dispatcher
from bot.handlers import get_handlers
from bot.long_polling import start_long_polling
from bot.infrastructure.messenger_telegram import MessengerTelegram
from bot.infrastructure.storage_sqlite import StorageSqlite 


def main() -> None:
    try:
        storage = StorageSqlite()
        storage.recreate_database()
        messenger: Messenger = MessengerTelegram()
        dispatcher = Dispatcher(storage, messenger)
        dispatcher.add_handler(*get_handlers())
        start_long_polling(dispatcher, messenger)
    except KeyboardInterrupt:
        print("\nBye:)")


if __name__ == "__main__":
    main()
