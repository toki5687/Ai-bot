import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
import openai

# Set your OpenAI API key here
openai.api_key = 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

# Telegram bot token from BotFather
TELEGRAM_TOKEN = 7672233224:AAF7rbKaIcJWH-hsiCOJK619icaZbCyleZo

# Enable logging
logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I'm your AI bot 🤖. Ask me anything.")

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_message}]
    )
    reply = response.choices[0].message.content
    await update.message.reply_text(reply)

app = ApplicationBuilder().token(7672233224:AAF7rbKaIcJWH-hsiCOJK619icaZbCyleZo).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))

app.run_polling()

