import telebot
from telebot import types

TOKEN = "8604417571:AAG0xq-2E-yPdV9Vwvutlz1MmNCvDizqYUo"
bot = telebot.TeleBot(TOKEN)

# --- DATA ---
user_test = {}
test_mode = {}

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
    if message.chat.id in test_mode:
        del test_mode[message.chat.id]
    show_menu(message)

# --- SUBJECT INFO ---
@bot.message_handler(func=lambda message: message.text in ["Орыс тілі","Қазақ тілі","Математика","Физика","География","Биология","Ағылшын"] and message.chat.id not in test_mode)
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
# 🔥 ТЕСТ
# =======================

@bot.message_handler(func=lambda message: message.text == "🧠 Тест")
def test(message):
    test_mode[message.chat.id] = True  # включаем режим теста

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
    if message.chat.id in test_mode:
        user_test[message.chat.id] = {"subject": message.text, "q": 0, "score": 0}
        del test_mode[message.chat.id]
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

# --- МАТЕМАТИКА ---
elif "интеграл" in text:
    bot.send_message(message.chat.id, "Интеграл — функцияның жинақталған мәні.")
elif "туынды" in text:
    bot.send_message(message.chat.id, "Туынды — функцияның өзгеру жылдамдығы.")
elif "логарифм" in text:
    bot.send_message(message.chat.id, "Логарифм — дәрежені табу амалы.")
elif "теңдеу" in text:
    bot.send_message(message.chat.id, "Теңдеу — белгісізі бар теңдік.")
elif "процент" in text:
    bot.send_message(message.chat.id, "Процент — жүзден бір бөлік (%).")

# --- ФИЗИКА ---
elif "гравитация" in text:
    bot.send_message(message.chat.id, "Гравитация — денелердің тартылуы.")
elif "күш" in text:
    bot.send_message(message.chat.id, "Күш — денеге әсер ететін физикалық шама.")
elif "энергия" in text:
    bot.send_message(message.chat.id, "Энергия — жұмыс істеу қабілеті.")
elif "жылдамдық" in text:
    bot.send_message(message.chat.id, "Жылдамдық — қозғалыс шапшаңдығы (s/t).")
elif "масса" in text:
    bot.send_message(message.chat.id, "Масса — дененің инерттілік өлшемі.")

# --- БИОЛОГИЯ ---
elif "жасуша" in text:
    bot.send_message(message.chat.id, "Жасуша — тіршіліктің ең кіші бөлігі.")
elif "днк" in text:
    bot.send_message(message.chat.id, "ДНҚ — генетикалық ақпарат тасымалдаушы.")
elif "организм" in text:
    bot.send_message(message.chat.id, "Организм — тірі ағза.")
elif "қан" in text:
    bot.send_message(message.chat.id, "Қан — оттегін және қоректік заттарды тасымалдайды.")
elif "жүрек" in text:
    bot.send_message(message.chat.id, "Жүрек — қан айдайтын негізгі орган.")

# --- ГЕОГРАФИЯ ---
elif "жер" in text:
    bot.send_message(message.chat.id, "Жер — Күн жүйесіндегі үшінші планета 🌍")
elif "материк" in text:
    bot.send_message(message.chat.id, "Материк — үлкен құрлық бөлігі.")
elif "мұхит" in text:
    bot.send_message(message.chat.id, "Мұхит — ең үлкен су айдыны.")
elif "астана" in text:
    bot.send_message(message.chat.id, "Қазақстанның астанасы — Астана.")
elif "климат" in text:
    bot.send_message(message.chat.id, "Климат — белгілі бір жердің ауа райы ерекшелігі.")

# --- ҚАЗАҚ ТІЛІ (ЕСІМДЕР) ---
elif "зат есім" in text:
    bot.send_message(message.chat.id, "Зат есім — заттың, құбылыстың, адамның атын білдіреді.")
elif "жалқы есім" in text:
    bot.send_message(message.chat.id, "Жалқы есім — жеке атаулар (Астана, Айжан).")
elif "жалпы есім" in text:
    bot.send_message(message.chat.id, "Жалпы есім — жалпы атаулар (қала, адам, кітап).")
elif "сын есім" in text:
    bot.send_message(message.chat.id, "Сын есім — заттың сынын, сапасын білдіреді.")
elif "сапалық сын есім" in text:
    bot.send_message(message.chat.id, "Сапалық сын есім — тікелей сапаны білдіреді (жақсы, әдемі).")
elif "қатыстық сын есім" in text:
    bot.send_message(message.chat.id, "Қатыстық сын есім — басқа сөздер арқылы жасалады (темірдей, таулы).")
elif "сан есім" in text:
    bot.send_message(message.chat.id, "Сан есім — заттың санын, ретін білдіреді.")
elif "есептік сан есім" in text:
    bot.send_message(message.chat.id, "Есептік сан есім — нақты санды білдіреді (бір, екі, үш).")
elif "реттік сан есім" in text:
    bot.send_message(message.chat.id, "Реттік сан есім — ретті білдіреді (бірінші, екінші).")
elif "жинақтық сан есім" in text:
    bot.send_message(message.chat.id, "Жинақтық сан есім — топты білдіреді (екеу, үшеу).")
elif "болжалдық сан есім" in text:
    bot.send_message(message.chat.id, "Болжалдық сан есім — шамамен сан (жүздей, мыңға жуық).")
elif "бөлшектік сан есім" in text:
    bot.send_message(message.chat.id, "Бөлшектік сан есім — бөлшек сан (жарты, үштен бір).")
elif "есімдік" in text:
    bot.send_message(message.chat.id, "Есімдік — заттың атын атамай, оның орнына қолданылады.")
elif "жіктеу есімдігі" in text:
    bot.send_message(message.chat.id, "Жіктеу есімдігі — мен, сен, ол, біз, сіз, олар.")
elif "сілтеу есімдігі" in text:
    bot.send_message(message.chat.id, "Сілтеу есімдігі — бұл, сол, анау.")
elif "сұрау есімдігі" in text:
    bot.send_message(message.chat.id, "Сұрау есімдігі — кім? не? қай?")
elif "өздік есімдік" in text:
    bot.send_message(message.chat.id, "Өздік есімдік — өзім, өзің, өзі.")
elif "жалпылау есімдігі" in text:
    bot.send_message(message.chat.id, "Жалпылау есімдігі — бәрі, барлығы.")
elif "болымсыздық есімдігі" in text:
    bot.send_message(message.chat.id, "Болымсыздық есімдігі — ешкім, ештеңе.")
elif "анықтауыш есімдік" in text:
    bot.send_message(message.chat.id, "Анықтауыш есімдік — әркім, кейбір, барлық.")

# --- АҒЫЛШЫН ---
elif "english" in text or "ағылшын" in text:
    bot.send_message(message.chat.id, "English is an international language 🌍")
elif "hello" in text:
    bot.send_message(message.chat.id, "Hello! How are you? 😊")
elif "thanks" in text:
    bot.send_message(message.chat.id, "You're welcome! 👍")

# --- ОБЩЕЕ ---
elif "рахмет" in text:
    bot.send_message(message.chat.id, "Сізге де рахмет! 😊")
elif "көмек" in text:
    bot.send_message(message.chat.id, "Мен пәндер мен тест бойынша көмектесе аламын 📚")

# --- ЕСЛИ НЕ ПОНЯЛ ---
else:
    bot.send_message(message.chat.id,
                     "🤔 Сұрақты нақтырақ қойыңыз немесе пән таңдаңыз 📚")

bot.polling()
      

