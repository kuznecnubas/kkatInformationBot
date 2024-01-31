# Создаем объект, умеющий работать с телеграм API и сразу же передаем ему токен для подключения к боту
bot = telebot.TeleBot("6437951339:AAHzQBQonTezuyVNJAf6kD9ztMuXrqWJGzA")

@bot.message_handler()
def echo_all(message):
    # Команда боту ответить на сообщение, текстом из сообщения
    bot.reply_to(message, message.text)

# Запуск бота, на регулярную отправку запросов новых сообщений с сервера
bot.infinity_polling()
