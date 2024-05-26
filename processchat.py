from config import BOT_USER
from handler import handle_file, handle_resp
from telegram import Update
from telegram.ext import ContextTypes


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text
    print(f'User({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == "group":
        if BOT_USER in text:
            new_text: str = text.replace(BOT_USER, '').strip()
            response: str = handle_resp(new_text)
        else:
            return
    else:
        response: str = handle_resp(text)

    print(f'Bot: {response}')
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} cause error {context.error}')

async def process_image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file_id = update.message.photo[-1].file_id
    file = await context.bot.get_file(file_id)
    #await file.download_to_drive()
    flink = file.file_path
    resptext: str = handle_file(flink)
    await update.message.reply_text(resptext)
   # await update.message.reply_text(handle_file)

async def process_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file_id = update.message.document.file_id
    file = await context.bot.get_file(file_id)
    #await file.download_to_drive()
    flink = file.file_path
    # print(flink)
    resptext: str = handle_file(flink)
    await update.message.reply_text(resptext)