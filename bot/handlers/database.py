from bot.handlers.handler import Handler, HandlerStatus
from bot.domain.storage import Storage
from bot.domain.messenger import Messenger


class Database(Handler):
    def can_handle(self, update: dict, state: str, order_json: dict, storage: Storage, messenger: Messenger) -> bool:
        return True

    def handle(self, update: dict, state: str, order_json: dict, storage: Storage, messenger: Messenger) -> HandlerStatus:
        storage.persist_updates([update])
        return HandlerStatus.CONTINUE
