import requests
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackQueryHandler
)
from settings import *
from details.handlers import *


updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

def register_handlers():

    dispatcher.add_handler(CommandHandler("start", start)),
    dispatcher.add_handler(MessageHandler(Filters.photo, add_photo)),
    dispatcher.add_handler(MessageHandler(Filters.text, text)),
    dispatcher.add_handler(CallbackQueryHandler(button_callback)),
    dispatcher.add_handler(MessageHandler(Filters.video, add_video))

    updater.start_polling()
    updater.idle()
register_handlers()