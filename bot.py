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
departmentsButton = telebot.types.KeyboardButton("Отделения")
departmentsIndustrialButton = telebot.types.KeyboardButton("Индустриальное отделение")
departmentsTechniacalButton = telebot.types.KeyboardButton("Техническое отделение")
departmentsCorrespondenceButton = telebot.types.KeyboardButton("Заочное отделение")
departmentsEngineeringButton = telebot.types.KeyboardButton("Машиностроительное отделение")
departmentsProfessionalButton = telebot.types.KeyboardButton("Профессиональная школа")
#клавиатуры
mainKeyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
mainKeyboard.add(aboutButton, contactsButton, departmentsButton)

aboutKeyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
aboutKeyboard.add(mainInformationButton, missionOfColledgeButton).add(mainKeyboardButton)

contactsKeyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
contactsKeyboard.add(phoneButton, adressButton, emailButton).add(mainKeyboardButton)

departmentsKeyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
departmentsKeyboard.add(departmentsIndustrialButton, departmentsTechniacalButton, departmentsCorrespondenceButton, departmentsEngineeringButton, departmentsProfessionalButton).add(mainKeyboardButton)


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
        bot.send_location(message.chat.id, "53.227123", "63.637152", reply_markup=contactsKeyboard)
    elif message.text == "Номер телефона":
        bot.reply_to(message, "87142579770", reply_markup=contactsKeyboard)
    elif message.text == "Email":
        bot.reply_to(message, "kkat311@mail.ru", reply_markup=contactsKeyboard)
    elif message.text == "Отделения":
        bot.reply_to(message, "В колледже есть 5 отделений:\n-Индустриальное отделение\n-Техническое отделение\n-Заочное отделение\n-Машиностроительное отделение\n-Профессиональная школа\n\nПро какое вы хотите узнать?", reply_markup=departmentsKeyboard)
#    elif message.text == "Отделения":
#        bot.reply_to(message, "В колледже есть 5 отделений:\n-Индустриальное отделение\n-Техническое отделение\n-Заочное отделение\n-Машиностроительное отделение\n-Профессиональная школа\n\nПро какое вы хотите узнать?", reply_markup=departmentsKeyboard)
#    elif message.text == "Отделения":
#        bot.reply_to(message, "В колледже есть 5 отделений:\n-Индустриальное отделение\n-Техническое отделение\n-Заочное отделение\n-Машиностроительное отделение\n-Профессиональная школа\n\nПро какое вы хотите узнать?", reply_markup=departmentsKeyboard)
#    elif message.text == "Отделения":
#        bot.reply_to(message, "В колледже есть 5 отделений:\n-Индустриальное отделение\n-Техническое отделение\n-Заочное отделение\n-Машиностроительное отделение\n-Профессиональная школа\n\nПро какое вы хотите узнать?", reply_markup=departmentsKeyboard)
#    elif message.text == "Отделения":
#        bot.reply_to(message, "В колледже есть 5 отделений:\n-Индустриальное отделение\n-Техническое отделение\n-Заочное отделение\n-Машиностроительное отделение\n-Профессиональная школа\n\nПро какое вы хотите узнать?", reply_markup=departmentsKeyboard)
#    elif message.text == "Отделения":
#        bot.reply_to(message, "В колледже есть 5 отделений:\n-Индустриальное отделение\n-Техническое отделение\n-Заочное отделение\n-Машиностроительное отделение\n-Профессиональная школа\n\nПро какое вы хотите узнать?", reply_markup=departmentsKeyboard)
    else:
        bot.reply_to(message, "Я не знаю этой команды")

bot.infinity_polling()
