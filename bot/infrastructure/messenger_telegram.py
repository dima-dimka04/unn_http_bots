import urllib.request
import os
import json
from dotenv import load_dotenv
from bot.domain.messenger import Messenger

load_dotenv()


class MessengerTelegram(Messenger):
    def make_request(self, method: str, **kwargs) -> dict:
        json_data = json.dumps(kwargs).encode("utf-8")

        request = urllib.request.Request(
            method="POST",
            url=f"{os.getenv("TELEGRAM_BASE_URI")}/{method}",
            data=json_data,
            headers={
                "Content-Type": "application/json",
            },
        )

        with urllib.request.urlopen(request) as response:
            response_body = response.read().decode("utf-8")
            response_json = json.loads(response_body)
            assert response_json["ok"] == True
            return response_json["result"]

    def getUpdates(self, **params) -> dict:
        return self.make_request("getUpdates", **params)

    def sendMessage(self, chat_id: int, text: str, **params) -> dict:
        return self.make_request("sendMessage", chat_id=chat_id, text=text, **params)

    def sendPhoto(self, chat_id: int, photo: str, **params) -> dict:
        return self.make_request("sendPhoto", chat_id=chat_id, photo=photo, **params)

    def answerCallbackQuery(self, callback_query_id: str, **kwargs) -> dict:
        return self.make_request(
            "answerCallbackQuery", callback_query_id=callback_query_id, **kwargs
        )

    def deleteMessage(self, chat_id: int, message_id: int) -> dict:
        return self.make_request(
            "deleteMessage", chat_id=chat_id, message_id=message_id
        )

    def getMe(self) -> dict:
        return self.make_request("getMe")
