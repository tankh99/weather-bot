from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
# from constants import START, EXIT
import constants

def gen_start_markup():
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton("Check Weather", callback_data=constants.START),
        InlineKeyboardButton("Exit", callback_data=constants.EXIT)
    )
    return markup