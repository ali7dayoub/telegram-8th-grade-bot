import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

MATH_CHANNEL_LINK = "https://t.me/+Ro_s4Nf4UfQ5ZWI8"
SCIENCE_CHANNEL_LINK = "https://t.me/+lQ-_AQttauZiODRk"
ENGLISH_CHANNEL_LINK = "https://t.me/+-E_Ss-2CEKg1ODJk"

TEACHER_PHONE_NUMBER = "+969931313297"
TEACHER_FIRST_NAME = "Admin"
TEACHER_LAST_NAME = "Support"

def get_main_keyboard():
    keyboard = [
        ["Maths", "Science", "English"],
        ["Refresh", "Contact with teacher"]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome! Please choose an option:",
        reply_markup=get_main_keyboard()
    )

async def handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "Maths":
        await update.message.reply_text(f"Join our Math channel: {MATH_CHANNEL_LINK}")
    elif text == "Science":
        await update.message.reply_text(f"Join our Science channel: {SCIENCE_CHANNEL_LINK}")
    elif text == "English":
        await update.message.reply_text(f"Join our English channel: {ENGLISH_CHANNEL_LINK}")
    elif text == "Refresh":
        await update.message.reply_text("Menu refreshed!", reply_markup=get_main_keyboard())
    elif text == "Contact with teacher":
        await update.message.reply_contact(
            phone_number=TEACHER_PHONE_NUMBER,
            first_name=TEACHER_FIRST_NAME,
            last_name=TEACHER_LAST_NAME
        )
    else:
        await update.message.reply_text("Please choose a valid option from the menu.")

async def main():
    token = os.getenv("BOT_TOKEN")
    if not token:
        raise ValueError("BOT_TOKEN environment variable not set")
    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_buttons))
    print("Bot is running...")
    await app.run_polling()

if __name__ == "_main_":
    import asyncio
    asyncio.run(main())
