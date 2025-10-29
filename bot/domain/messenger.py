from abc import ABC, abstractmethod

class Messenger(ABC):
    @abstractmethod
    def getUpdates(self, **params) -> dict:
        pass
    
    @abstractmethod
    def sendMessage(self, chat_id: int, text: str, **params) -> dict:
        pass
    
    @abstractmethod
    def sendPhoto(self, chat_id: int, photo: str, **params) -> dict:
        pass

    @abstractmethod
    def answerCallbackQuery(self, callback_query_id: str, **kwargs) -> dict:
        pass
