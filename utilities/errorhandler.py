from telegram import Update
from telegram.ext import ContextTypes

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} cause error {context.error}')