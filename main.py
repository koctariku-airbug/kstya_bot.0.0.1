#bot kstya
from config import load_token
from handlers.commands import show_menu
from handlers.commands import help_command
from handlers.commands import time, game, wiki, joke
from handlers.text_hand import text_handler
from time import asctime
from telegram import __version__ as tg_ver
from telegram.ext import Application, CommandHandler, MessageHandler, filters

TOKEN = load_token()

async def start(update, context):
    user = update.effective_user
    await update.message.reply_text(f'Здарова, {user.first_name}!\n'
                                    'набери /menu или /help')
#логика
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("menu", show_menu))
    app.add_handler(CommandHandler("time", time))
    app.add_handler(CommandHandler("game", game))
    app.add_handler(CommandHandler("wiki", wiki))
    app.add_handler(CommandHandler("joke", joke))


    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, text_handler))
    app.run_polling()
if __name__ == '__main__':
    main()