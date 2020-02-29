from telegram.ext import Updater
from telegram.ext import CommandHandler, MessageHandler
from telegram.ext import Filters
import logging
import sqlite3

#CONST
TOKEN  = '506889620:AAEu2LhOhwYf0jcLLPnX2v3t0p38679198o'
DB_DIR = './../../db.sqlite3'

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)


updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

conn = sqlite3.connect()
cursor = conn.cursor()

#Init work functions
def Start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

def AddNumber(update, context):
    cursor.execute("INSERT INTO main_carnumbers VALUES \
        ((SELECT count(id) FROM main_carnumbers) + 1,\
        '{0}','{1}','{2}','{3}')".format('null', 'null', str(context.args[0])'null'))
    
    print('write addnumber')

def GetText(update, context):
    print('write text')

#Set Handlers
StartHandler = CommandHandler('start', Start)
AddNumberHandler = CommandHandler('addNumber', AddNumber) 
GetText = MessageHandler(Filters.text, GetText)

dispatcher.add_handler(StartHandler)
dispatcher.add_handler(AddNumberHandler)
dispatcher.add_handler(GetText)



updater.start_polling()