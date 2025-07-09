import telebot

bot = telebot.TeleBot("YOUR_BOT_TOKEN")  # Replace with your token

@bot.message_handler(func=lambda _: True)
def reply(message):
    bot.reply_to(message, "I'm alive 24/7! 🚀")

bot.polling(none_stop=True)  # Keeps the bot running
