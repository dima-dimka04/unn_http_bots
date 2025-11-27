from abc import ABC, abstractmethod


class Messenger(ABC):
    @abstractmethod
    async def getUpdates(self, **params) -> dict:
        pass

    @abstractmethod
    async def sendMessage(self, chat_id: int, text: str, **params) -> dict:
        pass

    @abstractmethod
    async def sendPhoto(self, chat_id: int, photo: str, **params) -> dict:
        pass

    @abstractmethod
    async def answerCallbackQuery(self, callback_query_id: str, **kwargs) -> dict:
        pass
