This code is a Telegram Bot implemented using the python telegram-bot library.

Features

The bot has two modes of operation, one using a database and another using OpenAI's GPT language model.
In database mode, the bot receives messages from the user, processes them and returns the best answer from the database.
In OpenAI mode, the bot interacts with the user using the GPT language model for better human-like conversation.
The bot has the ability to collect information from the user.
The bot has the ability to "like" or "dislike" answers and adjust the weight of the answer in the database accordingly.
Requirements

telegram
telegram-ext
Usage

Replace token in the Scripts/Token.py file with your Telegram Bot API token.
Run the script using python bot.py
Start chatting with your bot on Telegram.
Callbacks

collect_info: collects information from the user.
reseive_message: processes the user's message and returns the best answer from the database.
open_ai_init: switches the bot to OpenAI mode.
open_ai_deinit: switches the bot back to database mode.
present: returns a pre-defined message.
button: processes "like" or "dislike" button press.
