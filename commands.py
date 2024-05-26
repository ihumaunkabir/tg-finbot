from telegram import Update
from telegram.ext import ContextTypes

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello from start button, start your conversation')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Browse help.')

async def info_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Get information at your convenience.')