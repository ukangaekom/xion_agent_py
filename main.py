from typing import Final
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler, CallbackContext
from dotenv import load_dotenv
import os
import hr_ai

load_dotenv()
TOKEN: Final = os.getenv("BOT_API_KEY") 
BOT_USERNAME: Final = "@hr_agentic_bot"



# print(TOKEN, BOT_USERNAMEL)


# using async await to create bot functions

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello Welcome to xion help desk. Reply /help '
                                    ' to know more about flamingo services')


# More commands can be written below


# Handling responsess
def handle_response(text: str) -> str:

    return hr_ai.aiagent(text)


async def handle_message(update: Update, context: CallbackContext):

    
    response: str = handle_response(update.message.text)

    print('BOT', response)
    await update.message.reply_text(response, parse_mode='Markdown')


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} cause error {context.error}')





if __name__ == '__main__':
    print('Program is starting')
   
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start_command))

    #  message handlers
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # error
    app.add_error_handler(error)

    # Printing polling
    print('polling ....')
    app.run_polling(poll_interval=3)
