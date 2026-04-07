import telebot
from telebot import types

TOKEN = "8604417571:AAG0xq-2E-yPdV9Vwvutlz1MmNCvDizqYUo"
bot = telebot.TeleBot(TOKEN)

# --- START ---
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("📚 Пәндер", "🧠 Тест")

    bot.send_message(message.chat.id,
                     "Сәлем! Мен БілімКөмек ботымын 📚\nПәнді таңдаңыз:",
                     reply_markup=markup)

# --- MENU ---
def show_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("📚 Пәндер", "🧠 Тест")
    bot.send_message(message.chat.id, "Меню", reply_markup=markup)

# --- SUBJECTS ---
@bot.message_handler(func=lambda message: message.text == "📚 Пәндер")
def subjects(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    subjects_list = ["Орыс тілі", "Қазақ тілі", "Математика", "Физика", "География", "Биология", "Ағылшын"]
    for sub in subjects_list:
        markup.add(sub)

    markup.add("🔙 Артқа")
    bot.send_message(message.chat.id, "Пәнді таңдаңыз:", reply_markup=markup)

# --- BACK ---
@bot.message_handler(func=lambda message: message.text == "🔙 Артқа")
def back(message):
    show_menu(message)

# --- SUBJECT INFO ---
@bot.message_handler(func=lambda message: message.text in ["Орыс тілі","Қазақ тілі","Математика","Физика","География","Биология","Ағылшын"])
def subject_info(message):
    answers = {
        "Орыс тілі": "Орыс тілі — грамматика мен жазу ережелерін үйретеді.",
        "Қазақ тілі": "Қазақ тілі — мемлекеттік тіл, сөйлеу мен жазуды үйретеді.",
        "Математика": "Математика — сандар мен формулалар ғылымы.",
        "Физика": "Физика — табиғат заңдарын зерттейді.",
        "География": "География — жер мен табиғатты зерттейді.",
        "Биология": "Биология — тірі ағзаларды зерттейді.",
        "Ағылшын": "Ағылшын тілі — халықаралық қарым-қатынас тілі."
    }
    bot.send_message(message.chat.id, answers[message.text])

# --- SMART ANSWER ---
@bot.message_handler(func=lambda message: True)
def smart_answer(message):
    text = message.text.lower()

    # сәлем
    if "сәлем" in text:
        bot.send_message(message.chat.id, "Сәлем! 👋 Қалай көмектесем?")
    
    # математика
    elif "интеграл" in text:
        bot.send_message(message.chat.id, "Интеграл — шексіз аз шамалардың қосындысы.")
    elif "туынды" in text:
        bot.send_message(message.chat.id, "Туынды — функцияның өзгеру жылдамдығы.")
    elif "логарифм" in text:
        bot.send_message(message.chat.id, "Логарифм — дәреже көрсеткіші.")
    
    # физика
    elif "гравитация" in text:
        bot.send_message(message.chat.id, "Гравитация — денелердің тартылу күші.")
    elif "күш" in text:
        bot.send_message(message.chat.id, "Күш — денеге әсер ететін шама.")
    
    # биология
    elif "жасуша" in text:
        bot.send_message(message.chat.id, "Жасуша — тіршіліктің ең кіші бірлігі.")
    elif "днк" in text:
        bot.send_message(message.chat.id, "ДНҚ — генетикалық ақпарат сақтайды.")
    
    # география
    elif "жер" in text:
        bot.send_message(message.chat.id, "Жер — Күн жүйесіндегі үшінші планета 🌍")
    
    # тілдер
    elif "етістік" in text:
        bot.send_message(message.chat.id, "Етістік — қимылды білдіреді.")
    elif "зат есім" in text:
        bot.send_message(message.chat.id, "Зат есім — заттың атын білдіреді.")
    
    # если не понял
    else:
        bot.send_message(message.chat.id,
                         "🤔 Сұрақты нақтырақ қойыңыз немесе пән таңдаңыз 📚")

# --- TEST ---
user_test = {}

# --- ТЕСТ ВЫБОР ПРЕДМЕТА ---
@bot.message_handler(func=lambda message: message.text == "🧠 Тест")
def test(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    subjects = ["Математика", "Физика", "Биология", "География", "Қазақ тілі"]
    for sub in subjects:
        markup.add(sub)

    markup.add("🔙 Артқа")
    bot.send_message(message.chat.id, "Тест пәнін таңдаңыз:", reply_markup=markup)

# --- ВОПРОСЫ ---
questions = {
    "Математика": [
        ("2+2=?", ["3", "4", "5"], "4"),
        ("5*2=?", ["10", "8", "6"], "10"),
        ("10/2=?", ["2", "5", "10"], "5"),
        ("3^2=?", ["6", "9", "3"], "9"),
        ("7-3=?", ["4", "3", "5"], "4"),
    ],
    "Физика": [
        ("Күш деген не?", ["энергия", "әсер", "жылдамдық"], "әсер"),
        ("Жылдамдық формуласы?", ["s/t", "t/s", "s*t"], "s/t"),
        ("Энергия не?", ["жұмыс", "қуат", "күш"], "жұмыс"),
        ("Гравитация?", ["итерлу", "тарту", "айналу"], "тарту"),
        ("SI бірлігі?", ["Ньютон", "Метр", "Секунд"], "Ньютон"),
    ],
    "Биология": [
        ("Жасуша деген не?", ["орган", "бірлік", "ұлпа"], "бірлік"),
        ("ДНҚ не?", ["ақпарат", "су", "жасуша"], "ақпарат"),
        ("Адам не?", ["жануар", "өсімдік", "саңырауқұлақ"], "жануар"),
        ("Тіршілік белгісі?", ["өсу", "ұйқы", "ойын"], "өсу"),
        ("Организм?", ["жүйе", "тірі дене", "зат"], "тірі дене"),
    ],
    "География": [
        ("Жер не?", ["планета", "жұлдыз", "ай"], "планета"),
        ("Материк?", ["су", "құрлық", "ауа"], "құрлық"),
        ("Мұхит?", ["үлкен су", "тау", "орман"], "үлкен су"),
        ("Карта не?", ["сурет", "сызба", "фото"], "сызба"),
        ("Астана?", ["Алматы", "Астана", "Шымкент"], "Астана"),
    ],
    "Қазақ тілі": [
        ("Зат есім?", ["қимыл", "зат", "сипат"], "зат"),
        ("Етістік?", ["зат", "қимыл", "сан"], "қимыл"),
        ("Сын есім?", ["сипат", "зат", "әрекет"], "сипат"),
        ("Сөйлем?", ["сөз", "ой", "әріп"], "ой"),
        ("Әріп?", ["дыбыс", "таңба", "сөз"], "таңба"),
    ]
}

# --- СТАРТ ТЕСТА ---
@bot.message_handler(func=lambda message: message.text in questions.keys())
def start_test(message):
    user_test[message.chat.id] = {"subject": message.text, "q": 0, "score": 0}
    ask_question(message)

# --- ЗАДАТЬ ВОПРОС ---
def ask_question(message):
    data = user_test[message.chat.id]
    subject = data["subject"]
    q_index = data["q"]

    question, options, correct = questions[subject][q_index]

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for opt in options:
        markup.add(opt)

    bot.send_message(message.chat.id, question, reply_markup=markup)

# --- ОТВЕТ ---
@bot.message_handler(func=lambda message: message.chat.id in user_test)
def check_answer(message):
    data = user_test[message.chat.id]
    subject = data["subject"]
    q_index = data["q"]

    correct = questions[subject][q_index][2]

    if message.text == correct:
        data["score"] += 1
        bot.send_message(message.chat.id, "✅ Дұрыс!")
    else:
        bot.send_message(message.chat.id, f"❌ Қате! Дұрыс жауап: {correct}")

    data["q"] += 1

    if data["q"] < len(questions[subject]):
        ask_question(message)
    else:
        bot.send_message(message.chat.id,
                         f"🎉 Тест аяқталды!\nНәтиже: {data['score']} / 5")
        del user_test[message.chat.id]
        show_menu(message)

bot.polling()


