from urllib.request import urlopen
from config import TOKEN, BOT_USER
from handler import handle_file, handle_resp
from commands import start_command, help_command, info_command
from processchat import handle_message, process_file, process_image
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes


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
    file_id = update.message.document.file_id  # Change to audio, video, etc., based on the file type
    file = await context.bot.get_file(file_id)
    #await file.download_to_drive()
    flink = file.file_path
    # print(flink)
    resptext: str = handle_file(flink)
    await update.message.reply_text(resptext)

if __name__ == '__main__':
    print('Bot started...')
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('info', info_command))
    app.add_handler(MessageHandler(filters.PHOTO, process_image))
    app.add_handler(MessageHandler(filters.Document.PDF, process_file))
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    app.add_error_handler(error)

    print('Bot polling...')
    app.run_polling(poll_interval=3)