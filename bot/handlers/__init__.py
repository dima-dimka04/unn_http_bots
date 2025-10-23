from bot.handlers.handler import Handler
from bot.handlers.database import Database
from bot.handlers.ensure_user_exists import EnsureUserExists
from bot.handlers.message_start import MessageStart
from bot.handlers.pizza_name import PizzaSelectionHandler
from bot.handlers.pizza_size import PizzaSizeHandler
from bot.handlers.drinks import PizzaDrinksHandler
from bot.handlers.order_approval import OrderApprovalHandler

def get_handlers() -> list[Handler]:
    return [
        Database(),
        EnsureUserExists(),
        MessageStart(),
        PizzaSelectionHandler(),
        PizzaSizeHandler(),
        PizzaDrinksHandler(),
        OrderApprovalHandler()
    ]