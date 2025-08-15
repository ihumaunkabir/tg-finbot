from telegram import Update
from telegram.ext import ContextTypes

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('HI I\'m ChottoBondhuAI created by BoroBhai, how can I help you?')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('You need to ask through messages, please wait a bit for response.')

async def info_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Get information at your convenience.')