async def text_handler(update, context):
    text = update.message.text.lower()

    if text == "привет":
        await update.message.reply_text("здарова 👋")
    elif text == "спасибо":
        await update.message.reply_text("без проблем")
    elif text == 'о великом мне':
        await update.message.reply_text('я бесподобный бот, который покроет твои хотелки')
    elif text == 'помощь':
        await update.message.reply_text('напиши /help')
    elif text == 'поздороваться с уважаемым ботом':
        await update.message.reply_text('сао брат')
    elif text == 'шутка от скуки':
        await update.message.reply_text('напиши /joke')
    elif 'купи' in text:
        await update.message.reply_text('я не могу, у меня нет средств, ведь я просто робот')
    else:
        await update.message.reply_text("не понял, напиши /help")
