from services.time import get_time
from services.game import get_game
from services.wiki import get_wiki
from services.joke import get_joke
from keyboards.menu import main_menu

async def help_command(update, context):
    await update.message.reply_text(
        'Что я умею:\n'
        '/start - поздороваться как мужик\n'
        '/help - помогу тебе разобраться в коммандах\n'
        '/menu - покажу тебе кнопки\n'
        '/time - подскажу время\n'
        '/joke - локальный мемчик\n'
        '/game - выбросить кубик\n'
        '/wiki - подскажет что-нибудь интересное'
)

async def show_menu(update, context):
    await update.message.reply_text(
        "Разберись 👇",
        reply_markup=main_menu()
    )

async def time(update, context):
    await update.message.reply_text(f"Сейчас: {get_time()}")

async def game(update, context):
    await update.message.reply_text(f"Ты бросил кубик.\n"
                                    f"🎲 Выпало: {get_game()}")

async def joke(update, context):
    await update.message.reply_text(get_joke())

async def wiki(update, context):
    if not context.args:
        await update.message.reply_text("Напиши, например, /wiki USA")
        return

    query = "_".join(context.args)
    data = get_wiki(query)

    if not data:
        await update.message.reply_text("Ничего не нашёл")
        return
    if data is None:
        await update.message.reply_text("Не удалось получить данные")
        return

    await update.message.reply_text(f"*{data['title']}*\n\n{data['text']}", parse_mode="Markdown")