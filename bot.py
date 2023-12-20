import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler,MessageHandler,filters

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=
    f"""
    Hi , bro
    {update.message.chat.id}

    """
        )

    


if __name__ == '__main__':
    application = ApplicationBuilder().token('6628818385:AAHAYls8JmByYGIRsCe7ZlGDa7bZnY3ElwM').build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    
    application.run_polling()