import telebot
bot = telebot.TeleBot("6346392949:AAE6qLPoVvnlpUMo7DaQutojLTwGiU5p_Sk")

#кнопки
aboutButton = telebot.types.KeyboardButton("О колледже")
mainInformationButton = telebot.types.KeyboardButton("Основная информация")
missionOfColledgeButton = telebot.types.KeyboardButton("Миссия колледжа")
mainKeyboardButton = telebot.types.KeyboardButton("Главное меню")
contactsButton = telebot.types.KeyboardButton("Контакты")
phoneButton = telebot.types.KeyboardButton("Номер телефона")
adressButton = telebot.types.KeyboardButton("Адрес")
emailButton = telebot.types.KeyboardButton("Email")
#клавиатуры
mainKeyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
mainKeyboard.add(aboutButton, contactsButton)

aboutKeyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
aboutKeyboard.add(mainInformationButton, missionOfColledgeButton).add(mainKeyboardButton)

contactsKeyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
contactsKeyboard.add(phoneButton, adressButton, emailButton).add(mainKeyboardButton)


#хэндлеры
@bot.message_handler(commands=['start'])
def startMessage(message):
    bot.reply_to(message, f"Привет {message.from_user.first_name}, я информационный бот Костанайского Колледжа Автомобильного Транспорта!", reply_markup=mainKeyboard)
@bot.message_handler()
def unknownCommandReply(message):
    if message.text == "Главное меню":
        bot.reply_to(message, "Вы в главном меню", reply_markup=mainKeyboard)
    elif message.text == "О колледже":
        bot.reply_to(message, "Какую информацию вы хотите получить?", reply_markup=aboutKeyboard)
    elif message.text == "Основная информация":
        bot.reply_to(message, "Костанайский колледж автомобильного транспорта (ККАТ) — одно из старейших учебных заведений Костанайской области, обучение ведется по 9 специальностям и 11 квалификациям. Сотрудничество с предприятиями и современная материально-техническая база обеспечивают качественное обучение и хорошее трудоустройство выпускников.", reply_markup=aboutKeyboard)
    elif message.text == "Миссия колледжа":
        bot.reply_to(message, "Миссия колледжа - заключается в предоставлении образования через удовлетворение потребностей общества и бизнеса в конкурентоспособных специалистах рабочих профессий и среднего звена технического профиля для инновационного развития, соответствующих потребностям рынка труда, задачам индустриально-инновационного развития страны и региона.", reply_markup=aboutKeyboard)
    elif message.text == "Контакты":
        bot.reply_to(message, "Как вы желаете связаться с нашим колледжом?", reply_markup=contactsKeyboard)
    elif message.text == "Адрес":
        bot.send_location(message.chat.id, "53.227123", "63.637152")
    else:
        bot.reply_to(message, "Я не знаю этой команды")

bot.infinity_polling()
