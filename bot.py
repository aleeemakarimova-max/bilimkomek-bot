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

    # --- ҚАЗАҚ ТІЛІ ---
    elif "зат есім" in text:
        bot.send_message(message.chat.id, "Зат есім — заттың атын білдіреді.")
    elif "сын есім" in text:
        bot.send_message(message.chat.id, "Сын есім — заттың сынын білдіреді.")
    elif "сан есім" in text:
        bot.send_message(message.chat.id, "Сан есім — санды білдіреді.")
    elif "есімдік" in text:
        bot.send_message(message.chat.id, "Есімдік — заттың орнына қолданылады.")

    # --- ОБЩЕЕ ---
    elif "рахмет" in text:
        bot.send_message(message.chat.id, "Сізге де рахмет! 😊")
    elif "көмек" in text:
        bot.send_message(message.chat.id, "Мен көмектесуге дайынмын 📚")

    else:
        bot.send_message(message.chat.id,
                         "🤔 Сұрақты нақтырақ қойыңыз немесе пән таңдаңыз 📚")

bot.infinity_polling()
  
   



