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
#cursor.execute("SELECT * FROM main_cards")
cursor.execute("INSERT INTO main_carnumbers (Name, Surname, CarNumber, Country) VALUES ('Vany', 'null', 'null','null');")
result = cursor.fetchall()
print(result)

command = ''

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

def echo(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = update.message.text)

def Set_name(update, context):
    if  update.massege.text == 'setname':
        command = 'setname'
        context.bot.send_message(chat_id = update.effectiv_chat.id, text = "you write setname")

def PutName(update, context):
    if command == 'setname':
    	coursor.execute("INSERT INTO main_carnumbers (Name,Surename, CarNumber, Country) VALUES (update.massege.text, 'null', 'null', 'null');")
#def PutDataNumber(update, context):
#    coursor.execute("INSERT INTO main_numbers

echo_handler = MessageHandler(Filters.text, echo)
#dispatcher.add_handler(echo_handler)
putn = MessageHandler(Filters.text, PutName)
dispatcher.add_handler(putn)
#from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
set_comm = CommandHandler('setname', Set_name)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(set_comm)


updater.start_polling()

