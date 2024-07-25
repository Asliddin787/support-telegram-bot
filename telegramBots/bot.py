from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Salom {update.effective_user.first_name}')


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'{update.effective_user.last_name} {update.effective_user.first_name}')

async def message(update: Update, context: ContextTypes.DEFAULT_TYPE): 
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')


app = ApplicationBuilder().token("6854655697:AAGIDdep6B7n_C20L2_o1qBVFbDFNSMP1Eg").build()

app.add_handler(CommandHandler("start", start))

app.run_polling()