import urllib.request
import os
import json
from dotenv import load_dotenv

load_dotenv()

def make_request(method: str, **kwargs) -> dict:
    json_data = json.dumps(kwargs).encode('utf-8')

    request = urllib.request.Request(
        method='POST',
        url=f"{os.getenv("TELEGRAM_BASE_URI")}/{method}",
        data=json_data,
        headers={
            'Content-Type': 'application/json',
        },
    )

    with urllib.request.urlopen(request) as response:
        response_body = response.read().decode('utf-8')
        response_json = json.loads(response_body)
        assert response_json["ok"] == True
        return response_json["result"] 

def getUpdates(**params) -> dict:
    return make_request("getUpdates", **params)

def sendMessage(chat_id: int, text: str, **params) -> dict:
    return make_request("sendMessage", chat_id=chat_id, text=text, **params)

def sendPhoto(chat_id: int, photo: str, **params) -> dict:
    return make_request("sendPhoto", chat_id=chat_id, photo=photo, **params)

def answerCallbackQuery(callback_query_id: str, **kwargs) -> dict:
    return make_request("answerCallbackQuery", callback_query_id=callback_query_id, **kwargs)

def deleteMessage(chat_id: int, message_id: int) -> dict:
    return make_request("deleteMessage", chat_id=chat_id, message_id=message_id)

def getMe() -> dict:
    return make_request("getMe")