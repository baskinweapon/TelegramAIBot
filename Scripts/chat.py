import openai
from telegram import Update
from telegram.ext import ContextTypes

from Scripts.Token import openai_api_key

openai.api_key = openai_api_key

def generate_response(message):
    model_engine = "text-davinci-003"

    completion = openai.Completion.create(
        engine=model_engine,
        prompt=message,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    response = completion.choices[0].text
    return response

async def recieve_GPT(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=generate_response(update.message.text))




