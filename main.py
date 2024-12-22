import telebot

token = "7964786955:AAHaxi2iz13kLUJxKvVx6C4krDdAwjRUN_4"

# Замени 'TOKEN' на токен твоего бота
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот который расскажет тебе о проблеме глобального потепления.")

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

# Запускаем бота
bot.polling()
