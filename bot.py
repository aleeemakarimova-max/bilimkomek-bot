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
@bot.message_handler(func=lambda message: message.text in ["Орыс тілі","Қазақ тілі","Математика","Физика","География","Биология","Ағылшын"] and message.chat.id not in user_test)
def subject_info(message):
    answers = {
        "Орыс тілі": "Орыс тілі — грамматика, сөздік қор және дұрыс жазу ережелерін үйретеді.",
        "Қазақ тілі": "Қазақ тілі — мемлекеттік тіл, сөйлеу мәдениеті мен жазуды дамытады.",
        "Математика": "Математика — сандар, теңдеулер, функциялар және логикалық ойлау ғылымы.",
        "Физика": "Физика — табиғат құбылыстары мен заңдарын зерттейді.",
        "География": "География — жер, табиғат және климатты зерттейді.",
        "Биология": "Биология — тірі ағзалар мен олардың құрылысын зерттейді.",
        "Ағылшын": "Ағылшын тілі — халықаралық қарым-қатынас тілі."
    }
    bot.send_message(message.chat.id, answers[message.text])

# =======================
# 🔥 ТЕСТ БЛОГЫ
# =======================

user_test = {}

@bot.message_handler(func=lambda message: message.text == "🧠 Тест")
def test(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    subjects = ["Математика", "Физика", "Биология", "География", "Қазақ тілі"]
    for sub in subjects:
        markup.add(sub)

    markup.add("🔙 Артқа")
    bot.send_message(message.chat.id, "Тест пәнін таңдаңыз:", reply_markup=markup)

questions = {
    "Математика": [
        ("2+2=?", ["3", "4", "5"], "4"),
        ("5*3=?", ["15", "10", "8"], "15"),
        ("10/2=?", ["2", "5", "10"], "5"),
        ("3^2=?", ["6", "9", "3"], "9"),
        ("7-3=?", ["4", "3", "5"], "4"),
        ("√16=?", ["2", "4", "8"], "4"),
    ],
    "Физика": [
        ("Күш деген не?", ["энергия", "әсер", "жылдамдық"], "әсер"),
        ("Жылдамдық формуласы?", ["s/t", "t/s", "s*t"], "s/t"),
        ("Энергия деген не?", ["жұмыс", "қуат", "күш"], "жұмыс"),
        ("Гравитация?", ["итерлу", "тарту", "айналу"], "тарту"),
        ("SI бірлігі?", ["Ньютон", "Метр", "Секунд"], "Ньютон"),
        ("Жылдамдық бірлігі?", ["м/с", "кг", "Н"], "м/с"),
    ],
    "Биология": [
        ("Жасуша деген не?", ["орган", "бірлік", "ұлпа"], "бірлік"),
        ("ДНҚ не?", ["ақпарат", "су", "жасуша"], "ақпарат"),
        ("Адам қай класқа жатады?", ["жануар", "өсімдік", "саңырауқұлақ"], "жануар"),
        ("Тіршілік белгісі?", ["өсу", "ұйқы", "ойын"], "өсу"),
        ("Организм?", ["жүйе", "тірі дене", "зат"], "тірі дене"),
        ("Қан не тасымалдайды?", ["оттегі", "су", "май"], "оттегі"),
    ],
    "География": [
        ("Жер не?", ["планета", "жұлдыз", "ай"], "планета"),
        ("Материк?", ["су", "құрлық", "ауа"], "құрлық"),
        ("Мұхит?", ["үлкен су", "тау", "орман"], "үлкен су"),
        ("Карта не?", ["сурет", "сызба", "фото"], "сызба"),
        ("Қазақстан астанасы?", ["Алматы", "Астана", "Шымкент"], "Астана"),
        ("Ең үлкен мұхит?", ["Атлант", "Тынық", "Үнді"], "Тынық"),
    ],
    "Қазақ тілі": [
        ("Зат есім?", ["қимыл", "зат", "сипат"], "зат"),
        ("Етістік?", ["зат", "қимыл", "сан"], "қимыл"),
        ("Сын есім?", ["сипат", "зат", "әрекет"], "сипат"),
        ("Сөйлем?", ["сөз", "ой", "әріп"], "ой"),
        ("Әріп?", ["дыбыс", "таңба", "сөз"], "таңба"),
        ("Көптік жалғау?", ["-лар", "-ды", "-ға"], "-лар"),
    ]
}

@bot.message_handler(func=lambda message: message.text in questions.keys())
def start_test(message):
    user_test[message.chat.id] = {"subject": message.text, "q": 0, "score": 0}
    ask_question(message)

def ask_question(message):
    data = user_test[message.chat.id]
    subject = data["subject"]
    q_index = data["q"]

    question, options, correct = questions[subject][q_index]

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for opt in options:
        markup.add(opt)

    bot.send_message(message.chat.id, question, reply_markup=markup)

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
                         f"🎉 Тест аяқталды!\nНәтиже: {data['score']} / {len(questions[subject])}")
        del user_test[message.chat.id]
        show_menu(message)

# =======================
# 🚨 SMART ANSWER (САМЫЙ ПОСЛЕДНИЙ)
# =======================

@bot.message_handler(func=lambda message: True)
def smart_answer(message):
    text = message.text.lower()

    if "сәлем" in text:
        bot.send_message(message.chat.id, "Сәлем! 👋 Қалай көмектесем?")
    elif "интеграл" in text:
        bot.send_message(message.chat.id, "Интеграл — функцияның жинақталған мәні.")
    elif "туынды" in text:
        bot.send_message(message.chat.id, "Туынды — функцияның өзгеру жылдамдығы.")
    elif "логарифм" in text:
        bot.send_message(message.chat.id, "Логарифм — дәрежені табу амалы.")
    elif "гравитация" in text:
        bot.send_message(message.chat.id, "Гравитация — денелердің тартылуы.")
    elif "жасуша" in text:
        bot.send_message(message.chat.id, "Жасуша — тіршіліктің ең кіші бөлігі.")
    else:
        bot.send_message(message.chat.id,
                         "🤔 Сұрақты нақтырақ қойыңыз немесе пән таңдаңыз 📚")

bot.polling()
      

