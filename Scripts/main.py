from typing import List
from uuid import uuid4

from html import escape

from telegram import Update, InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardButton, \
    ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup
from telegram.constants import ParseMode
from telegram.ext import filters, ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, InlineQueryHandler, \
    CallbackQueryHandler
import Data
from Scripts.Token import token


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Hi I'm a bot")


async def reseiveMessage(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("👍🏻", callback_data="1"),
            InlineKeyboardButton("👎🏻", callback_data="2"),
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await context.bot.send_message(chat_id=update.effective_chat.id, text=resieve(update.message.text), reply_markup=reply_markup)


def resieve(message):
    return find_best(message)

def find_best(message):
    weights: List[Data.Weight] = []

    d = Data.DataWeight()
    data = d.load_from_json()

    user_splited_message = []
    for weight in data:
        user_splited_message = weight.value.lower().split("&")
        strip_message = [x.strip() for x in user_splited_message]

        if not strip_message:
            for value in strip_message:
                if " " + value + " " in " " + message + " ":
                    weights.append(weight)
        else:
            for value in strip_message:
                if " " + value + " " in " " + message + " ":
                    weights.append(weight)
            else:
                print("Not Found")

    weights.sort(key=lambda x: x.weight)
    if not weights:
        return "Sorry, I was born recently, I don't know much, but I love to learn"
    else:
        return weights[-1].answer

def bubblesort(elements):
    swapped = False
    for n in range(len(elements)-1, 0, -1):
        for i in range(n):
            if elements[i] > elements[i + 1]:
                swapped = True

                elements[i], elements[i + 1] = elements[i + 1], elements[i]
        if not swapped:
            # exiting the function if we didn't make a single swap
            # meaning that the array is already sorted.
            return

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query

    await query.answer()

    await query.edit_message_text(text=f"Selected option: {query.data}")

if __name__ == '__main__':
    application = ApplicationBuilder().token(token).build()

    buttons = [["👍🏻", "👎🏻"]]

    greet_kb = ReplyKeyboardMarkup(
        buttons, one_time_keyboard=True,
        resize_keyboard=True
    )

    start_handler = CommandHandler('start', start)
    receiveMessage = MessageHandler(filters.TEXT & (~filters.COMMAND), reseiveMessage)

    application.add_handler(start_handler)
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(receiveMessage)

    application.run_polling()


