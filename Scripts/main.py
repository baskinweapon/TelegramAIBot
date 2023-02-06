from typing import List

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import filters, ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, InlineQueryHandler, \
    CallbackQueryHandler
import Data
from Scripts.Token import token

async def collect_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=collect(update.message.text))

# Save info about user and sent to call center
def collect(message):
    # add send your call center information
    print(message)
    return "Thank you, our call center call you in monday at 12:00"

async def reseive_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=resieve(update.message.text),
                                   reply_markup=reply_markup)

def callback_dislike():
    current_weight.weight -= 1
    for weight in data:
        if id(weight) == id(current_weight):
            weight.weight = current_weight.weight
    d.load_to_json(data)
    return "🔎Search more"


def callback_like():
    current_weight.weight += 1
    for weight in data:
        if id(weight) == id(current_weight):
            weight.weight = current_weight.weight
    d.load_to_json(data)
    return "🫡Thank you for answer"


def resieve(message):
    return find_best(message)


def find_best(message):
    weights.clear()

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

    weights.sort(key=lambda x: x.weight)
    if not weights:
        return "Sorry, I was born recently, I don't know much, but I love to learn"
    else:
        current_weight = weights[-1]
        return weights[-1].answer


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query

    await query.answer()

    colect_info = False
    if update.callback_query.data == "0":
        answer = callback_like()
    else:
        answer = callback_dislike()
        text = ""
        if len(weights) > 2:
            text = weights[-2]
        else:
            colect_info = True
            text = "Sorry i can't find information, please write your problem and i send it to Call Center"
        answer += "\n" + text
    await query.edit_message_text(text=f"{answer}")
    if colect_info:
        application.remove_handler(receiveMessage)
        application.add_handler(collectInfo)

if __name__ == '__main__':
    # load from data
    d = Data.DataWeight()
    data = d.load_from_json()

    weights: List[Data.Weight] = []

    current_weight = data[0]

    keyboard = [
        [
            InlineKeyboardButton("👍🏻", callback_data="0"),
            InlineKeyboardButton("👎🏻", callback_data="1"),
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    # start bot
    application = ApplicationBuilder().token(token).build()

    receiveMessage = MessageHandler(filters.TEXT & (~filters.COMMAND), reseive_message)
    collectInfo = MessageHandler(filters.TEXT, collect_info)
    application.add_handler(receiveMessage)
    application.add_handler(CallbackQueryHandler(button))

    application.run_polling()
