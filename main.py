from telegram.ext import Updater
from telegram.ext import CommandHandler, MessageHandler, Filters
import logging
import sqlite3

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

TOKEN  = '506889620:AAEu2LhOhwYf0jcLLPnX2v3t0p38679198o'

updater = Updater(token = TOKEN, use_context = True)
dispatcher = updater.dispatcher

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()
cursor.execute("SELECT * FROM main_cards")
result = cursor.fechall()
print(result)



def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

def echo(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = update.message.text)

echo_handler = MessageHandler(Filters.text, echo)
#dispatcher.add_handler(echo_handler)

#from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


updater.start_polling()

