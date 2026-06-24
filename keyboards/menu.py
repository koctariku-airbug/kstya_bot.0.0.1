from telegram import ReplyKeyboardMarkup

def main_menu():
    keyboard = [
        ['О великом мне', 'Помощь'],
        ['Поздороваться с уважаемым ботом', 'Шутка от скуки']
    ]

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True,
        one_time_keyboard=False
    )
