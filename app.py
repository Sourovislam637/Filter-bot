import telebot

bot = telebot.TeleBot("7553146028:AAH9VDdtnQTXNE3BsdAk1LDcdhhpR3VuhY0")  # Replace with your token

@bot.message_handler(func=lambda _: True)
def reply(message):
    bot.reply_to(message, "I'm alive 24/7! 🚀")

bot.polling(none_stop=True)  # Keeps the bot running
