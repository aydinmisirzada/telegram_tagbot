import os
import telegram
from telegram import Message
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.updater import Updater
from telegram.ext.dispatcher import Dispatcher
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.bot import Bot
from telegram.parsemode import ParseMode
import random
import db


API_TOKEN = os.environ['TELEGRAM_TOKEN']

updater = Updater(API_TOKEN,use_context=True)

dispatcher = updater.dispatcher

def tag(update: Update, context: CallbackContext):
    msg = ""
    users = db.select(update.effective_chat.id)
    for i in users:
        msg += i[0] + " "

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=
        msg,
        disable_notification=False,
        parse_mode="Markdown",
    )

def add(update: Update, context: CallbackContext):
    users = []
    user = update.effective_user
    id = user['id']
    msg = ""

    #check if already in users.txt
    users = db.check(user.mention_markdown(),update.effective_chat.id)
    if len(users) != 0:
        msg = "You've already been added!"
        context.bot.send_message(
                    chat_id=update.effective_chat.id,
                    text=
                    msg,
                    reply_to_message_id=update.effective_message.message_id,
                    parse_mode="Markdown",
        )
        return

    db.insert(user.mention_markdown(),update.effective_chat.id)

    msg = "You've been added! Please start me personally to get notified @invisibletagbot."

    context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=
                msg,
                reply_to_message_id=update.effective_message.message_id,
                parse_mode="Markdown",
    )



dispatcher.add_handler(CommandHandler("tag", tag))
dispatcher.add_handler(CommandHandler("add", add))

updater.start_polling()
# updater.idle()
