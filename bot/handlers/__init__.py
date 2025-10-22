from bot.handlers.handler import Handler
from bot.handlers.database import Database
from bot.handlers.ensure_user_exists import EnsureUserExists
from bot.handlers.message_start import MessageStart

def get_handlers() -> list[Handler]:
    return [
        Database(),
        EnsureUserExists(),
        MessageStart(),
    ]