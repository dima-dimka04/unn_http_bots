from bot.handler import Handler
import bot.telegram_client

class PhotoEcho(Handler):
    def can_handle(self, update: dict) -> bool:
        return "message" in update and "photo" in update["message"]

    def handle(self, update: dict) -> bool:
        chat_id = update["message"]["chat"]["id"]
        photos = update["message"]["photo"]
        best_photo = photos[-1]
        file_id = best_photo["file_id"]

        bot.telegram_client.sendPhoto(chat_id=chat_id, photo=file_id)
        return False