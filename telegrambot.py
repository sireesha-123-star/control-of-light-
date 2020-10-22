!pip install adafruit-io
from Adafruit_IO import Client,Data
import os

ADAFRUIT_IO_USERNAME = os.getenv('Sireesha_123')
ADAFRUIT_IO_KEY = os.getenv('aio_OmnI11Ua7yad5mHqonaxCUoG45qN')
TOKEN = os.getenv('1399937407:AAHNUzeL8RGKXYe2NabUEB7Ah1fDhhqt7J0')
aio = Client(ADAFRUIT_IO_USERNAME,ADAFRUIT_IO_KEY)
!pip install python-telegram-bot
  
from telegram.ext import Updater,CommandHandler,MessageHandler,Filters
import os
def off(update, context):
  context.bot.send_message(chat_id=update.effective_chat.id, text="Light is turning off")
  context.bot.send_photo(chat_id=update.effective_chat.id,photo='https://www.123rf.com/photo_12676342_filament-lamp-on-a-white-background-illustration-for-design.html')
  send_value(0)
def on(update, context):
  context.bot.send_message(chat_id=update.effective_chat.id, text="Light is turning on")
  context.bot.send_photo(chat_id=update.effective_chat.id,photo='https://www.123rf.com/photo_48123160_stock-vector-bright-glowing-incandescent-light-bulb-on-a-white-background.html')
  send_value(1)

def send_value(value):
  feed = aio.feeds('bot')
  aio.send_data(feed.key,value)

def input_message(update, context):
  text=update.message.text
  if text == 'on':
    send_value(1)
    context.bot.send_message(chat_id=update.effective_chat.id,text="Light is turning on")
    context.bot.send_photo(chat_id=update.effective_chat.id,photo='https://www.123rf.com/photo_48123160_stock-vector-bright-glowing-incandescent-light-bulb-on-a-white-background.html')
  elif text == 'off':
    send_value(0)
    context.bot.send_message(chat_id=update.effective_chat.id,text="Light is turning off")
    context.bot.send_photo(chat_id=update.effective_chat.id,photo='https://www.123rf.com/photo_12676342_filament-lamp-on-a-white-background-illustration-for-design.html')

    
def start(update,context):
  start_message='''
/off :To turn OFF the Light
/on :To turn ON the Light
'''
  context.bot.send_message(chat_id=update.effective_chat.id, text=start_message)


updater =Updater('1399937407:AAHNUzeL8RGKXYe2NabUEB7Ah1fDhhqt7J0')
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('off',off))
dispatcher.add_handler(CommandHandler('on',on))
dispatcher.add_handler(CommandHandler('start',start))
dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command),input_message))
updater.start_polling
updater.idle()
