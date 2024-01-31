import telebot
bot = telebot.TeleBot("6437951339:AAHzQBQonTezuyVNJAf6kD9ztMuXrqWJGzA")

#кнопки
aboutButton = telebot.types.KeyboardButton("О колледже")
mainInformationButton = telebot.types.KeyboardButton("Основная информация")
missionOfColledgeButton = telebot.types.KeyboardButton("Миссия колледжа")
#клавиатуры
mainKeyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
mainKeyboard.add(aboutButton)

aboutKeyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
aboutKeyboard.add(mainInformationButton, missionOfColledgeButton)


a =

#хэндлеры
@bot.message_handler(commands=['start'])
def startMessage(message):
    bot.reply_to(message, f"Привет {message.from.first_name}, я информационный бот Костанайского Колледжа Автомобильного Транспорта!", reply_markup=mainKeyboard)

@bot.message_handler()
def unknownCommandReply(message):
    if message.text == "О колледже":
        bot.reply_to(message, "Какую информацию вы хотите получить?", reply_markup=aboutKeyboard)
    elif message.text == "Основная информация":
        bot.reply_to(message, "Костанайский колледж автомобильного транспорта (ККАТ) — одно из старейших учебных заведений Костанайской области, обучение ведется по 9 специальностям и 11 квалификациям. Сотрудничество с предприятиями и современная материально-техническая база обеспечивают качественное обучение и хорошее трудоустройство выпускников.", reply_markup=aboutKeyboard)
    else:
        bot.reply_to(message, "Я не знаю этой команды")

bot.infinity_polling()
