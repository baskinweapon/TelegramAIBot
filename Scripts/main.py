from telegram import Update
from telegram.ext import filters, ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler
import Data
from Scripts.Token import token


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Hi I'm a bot")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

async def reseiveMessage(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=resieve(update.message.text))


def resieve(message):
    print(message)
    return find_best(message)

def find_best(message):
    d = Data.DataWeight()
    data = d.load_from_json()

    user_splited_message = []
    for weight in data:
        user_splited_message = weight.value.lower().split("&")
        strip = [x.strip() for x in user_splited_message]
        print(strip)

    return strip

if __name__ == '__main__':
    application = ApplicationBuilder().token(token).build()

    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    receiveMessage = MessageHandler(filters.TEXT & (~filters.COMMAND), reseiveMessage)

    application.add_handler(start_handler)
    # application.add_handler(echo_handler)
    application.add_handler(receiveMessage)

    application.run_polling()
