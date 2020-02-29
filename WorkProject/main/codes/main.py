from telegram.ext import Updater
from telegram.ext import CommandHandler, MessageHandler
from telegram.ext import Filters
import logging
import sqlite3

#CONST
TOKEN  = '506889620:AAEu2LhOhwYf0jcLLPnX2v3t0p38679198o'
COMMAND = ''

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)


updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

#Init work functions
def Start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

def AddName(update, context):
    COMMAND = 'AddName'
    print('write addname')

def GetText(update, context):
    print('write text')

#Set Handlers
StartHandler = CommandHandler('start', Start)
AddNameHandler = CommandHandler('addName', AddName) 
GetText = MessageHandler(Filters.text, GetText)

dispatcher.add_handler(StartHandler)
dispatcher.add_handler(AddNameHandler)
dispatcher.add_handler(GetText)



updater.start_polling()