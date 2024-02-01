import telebot
bot = telebot.TeleBot("6346392949:AAE6qLPoVvnlpUMo7DaQutojLTwGiU5p_Sk")

#кнопки
aboutButton = telebot.types.KeyboardButton("О колледже")
mainInformationButton = telebot.types.KeyboardButton("Основная информация")
missionOfColledgeButton = telebot.types.KeyboardButton("Миссия колледжа")
siteButton = telebot.types.KeyboardButton("Сайт")
LicenseButton = telebot.types.KeyboardButton("Лицензия")
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

managementButton = telebot.types.KeyboardButton("Руководство")
directorButton = telebot.types.KeyboardButton("Директор")
managersButton = telebot.types.KeyboardButton("Заведующие")
managersProfessionalButton = telebot.types.KeyboardButton("Проф. школа")
managersTechnicalButton = telebot.types.KeyboardButton("Техническое")
managersIndustrialButton = telebot.types.KeyboardButton("Индустриальное")
managersEngineeringButton = telebot.types.KeyboardButton("Машиностроительное")
#клавиатуры
mainKeyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
mainKeyboard.add(aboutButton, contactsButton).add(departmentsButton, managementButton)

aboutKeyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
aboutKeyboard.add(mainInformationButton, missionOfColledgeButton).add(siteButton, LicenseButton).add(mainKeyboardButton)

contactsKeyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
contactsKeyboard.add(phoneButton, adressButton, emailButton).add(mainKeyboardButton)

departmentsKeyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
departmentsKeyboard.add(departmentsIndustrialButton, departmentsTechniacalButton, departmentsCorrespondenceButton, departmentsEngineeringButton, departmentsProfessionalButton).add(mainKeyboardButton)

managementKeyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
managementKeyboard.add(directorButton, managersButton).add(mainKeyboardButton)

managersKeyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
managersKeyboard.add(managersIndustrialButton, managersTechnicalButton).add(managersEngineeringButton, managersProfessionalButton).add(managementButton).add(mainKeyboardButton)


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
    elif message.text == "Сайт":
        bot.reply_to(message, "https://kkat.edu.kz/", reply_markup=aboutKeyboard)
    elif message.text == "Лицензия":
        bot.send_document(message.chat.id, "https://kkat.edu.kz/storage/files/%D0%9A%D0%9A%D0%90%D0%A2%20-%D0%9B%D0%B8%D1%86%D0%B5%D0%BD%D0%B7%D0%B8%D1%8F%20%D0%9D%D0%9E%D0%92%D0%90%D0%AF-%D1%80%D1%83%D1%81.pdf", reply_markup=aboutKeyboard)
    elif message.text == "Контакты":
        bot.reply_to(message, "Как вы желаете связаться с нашим колледжом?", reply_markup=contactsKeyboard)
    elif message.text == "Адрес":
        bot.send_location(message.chat.id, "53.227123", "63.637152", reply_markup=contactsKeyboard)
    elif message.text == "Номер телефона":
        bot.reply_to(message, "87142579770", reply_markup=contactsKeyboard)
    elif message.text == "Email":
        bot.reply_to(message, "kkat311@mail.ru", reply_markup=contactsKeyboard)
    elif message.text == "Отделения":
        bot.reply_to(message, "В колледже есть 5 отделений:\n- Индустриальное отделение\n- Техническое отделение\n- Заочное отделение\n- Машиностроительное отделение\n- Профессиональная школа\n\nПро какое вы хотите узнать?", reply_markup=departmentsKeyboard)
    elif message.text == "Индустриальное отделение":
        bot.reply_to(message, "К индустриальному отделению относятся такие специальности как:\n- Учет и аудит \n- Вычислительная техника и ПО \n- Организация перевозок \n- Геодезия и картография", reply_markup=departmentsKeyboard)
    elif message.text == "Техническое отделение":
        bot.reply_to(message, "К техническому отделению относятся такие специальности как:\n- ТО, ремонт и эксплуатация автотранспорта \n- Строительство и эксплуатация автодорог \n- ТЭ дорожно-строительных машин", reply_markup=departmentsKeyboard)
    elif message.text == "Заочное отделение":
        bot.reply_to(message, "Данное отделение занимается обучением всех специальностей, но в заочном формате \n(не официальная информация)", reply_markup=departmentsKeyboard)
    elif message.text == "Машиностроительное отделение":
        bot.reply_to(message, "К машиностроительному отделению относятся такие специальности как:\n- Инженер-конструктор \n- Техник по машиностроению\n(не официальная информация)", reply_markup=departmentsKeyboard)
    elif message.text == "Профессиональная школа":
        bot.reply_to(message, "К профессиональной школе относятся такие специальности как:\n- ТО и ремонт сельскохозяйственной техники \n- Слесарь по ремонту автомобилей\n- Электрик автомобильного электрооборудования \n- Электрогазосварщик", reply_markup=departmentsKeyboard)
    elif message.text == "Руководство":
        bot.reply_to(message, "Про кого из руководства вы хотите узнать?", reply_markup=managementKeyboard)
    elif message.text == "Директор":
        bot.send_photo(message.chat.id, "https://azamat-kostanai.e-orda.kz/img/cachedImages/icon/2%C2%A0474-2-111.jpg", reply_markup=managementKeyboard)
        bot.reply_to(message, "Павленко Дмитрий Иванович")
    elif message.text == "Заведующие":
        bot.reply_to(message, "Про заведующего какого отделения вы хотите узнать?", reply_markup=managersKeyboard)
    elif message.text == "Индустриальное":
        bot.send_photo(message.chat.id, "https://azamat-kostanai.e-orda.kz/img/cachedImages/icon/3%C2%A0253-2-111.jpg", reply_markup=managersKeyboard)
        bot.reply_to(message, "Сарбасов Марат Бейбитович")
    elif message.text == "Техническое":
        bot.send_photo(message.chat.id, "https://azamat-kostanai.e-orda.kz/img/cachedImages/icon/3%C2%A0244-2-111.jpg", reply_markup=managersKeyboard)
        bot.reply_to(message, "Мергенбаев Акылдос Айдарханович")
    elif message.text == "Машиностроительное":
        bot.send_photo(message.chat.id, "https://azamat-kostanai.e-orda.kz/img/cachedImages/icon/3%C2%A0252-2-111.jpg", reply_markup=managersKeyboard)
        bot.reply_to(message, "Салимов Русланбек Ануарбекович")
    elif message.text == "Проф. школа":
        bot.send_photo(message.chat.id, "https://azamat-kostanai.e-orda.kz/img/cachedImages/icon/3%C2%A0236-1-111.jpg", reply_markup=managersKeyboard)
        bot.reply_to(message, "Альмагамбетов Талгат Минайдарович")
    else:
        bot.reply_to(message, "Я не знаю этой команды")

bot.infinity_polling()

