from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, CallbackContext, MessageHandler, filters

async def start(update: Update, context: CallbackContext) -> None:
    # Inline keyboard (tugma)
    inline_keyboard = [
        [InlineKeyboardButton("Button 1", callback_data='1')],
        [InlineKeyboardButton("Button 2", callback_data='2')],
    ]
    inline_reply_markup = InlineKeyboardMarkup(inline_keyboard)
    await update.message.reply_text('Please choose:', reply_markup=inline_reply_markup)
    
    # Reply keyboard (tugma)
    reply_keyboard = [
        [KeyboardButton("Replay Button 1")],
        [KeyboardButton("Replay Button 2")]
    ]
    reply_markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    await update.message.reply_text('Please choose a reply button:', reply_markup=reply_markup)

async def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()
    choice = query.data
    await query.edit_message_text(text=f"Selected option: {choice}")

async def handle_reply(update: Update, context: CallbackContext) -> None:
    # Replay buttonni qabul qilish
    text = update.message.text
    if text == "Replay Button 1":
        await update.message.reply_text("You pressed Replay Button 1")
    elif text == "Replay Button 2":
        await update.message.reply_text("You pressed Replay Button 2")

def main():
    application = Application.builder().token("7360860001:AAFbi5rv064Za5lPDjOTnqfXs7mArRDSRJs").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_reply))

    application.run_polling()

if __name__ == '__main__':
    main()
