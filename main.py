import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import psycopg2
from telebot import apihelper

TOKEN = '8097727230:AAFBgM2pLcfE_-ZuHZmpP3Zv30D-M-8Pi1M'
bot = telebot.TeleBot(TOKEN)

conn = psycopg2.connect(
    host="localhost",
    database="khatt",
    user="postgres",
    password="Khalid2004"
)
cursor = conn.cursor()

user_data = {}

def send_message_to_user(chat_id, message_text, reply_markup=None):
    try:
        bot.send_message(chat_id, message_text, reply_markup=reply_markup)
    except apihelper.ApiTelegramException as e:
        if e.result_json['description'] == 'Forbidden: bot was blocked by the user':
            print(f"Корбар {chat_id} ботро блок кардааст.")
        else:
            print(f"Хатои дигар рух дод: {e}")

@bot.message_handler(commands=['start'])
def start(message):
    user_data[message.chat.id] = {}
    
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("TECNOTOJ", url="https://t.me/tecnotoj04"),
               InlineKeyboardButton("QALB.SHOP", url="https://t.me/qalbb04"))
    
    send_message_to_user(message.chat.id, f"Салом, {message.from_user.first_name}!\n\n\n"
                                    "⚠️ХАБАРИ ФАВРӢ⚠️!\n\n"

"                                   Ба диққати шаҳрвандони Ҷумҳурии Тоҷикистон расонида мешавад, ки  ба қонунҳои федералӣ оид ба будубоши шаҳрвадони хориҷӣ дар Федератсияи Россия тағйиру иловаҳо ворид гардида, аз 5 феврали соли 2025 эътибори қонунӣ  пайдо мекунанд. Вазорати корҳои дохилии Федератсияи Россия(ФР) низоми махсуси ихроҷ (депортатсия)-ро ҷорӣ намуда, ба “рӯйхати шахсони назоратшаванда” зиёда аз 120 ҳазор шаҳрванди Ҷумҳурии Тоҷикистон ҳамчун қонунвайронкунанда ба қайд гирифта шудаанд. \n\n"


                                    " Шаҳрвандоне, ки дар рӯйхат қарор доранд, бояд худро то 5 феврали соли 2025 ба мақомоти дахлдори муҳоҷирати ФР муроҷиат намуда, ба қайди қонунӣ гиранд ё қаламрави ин давлатро тарк намоянд. Дар сурати дар муҳлати муайяншуда ба қайди қонунӣ нагирифтан шаҳрванд бо таври автоматӣ ба рӯйхати шахсони ихроҷшаванда(депортатсия) ворид гардида, ҳуқуқи рафтан ба ин давлатро аз даст медиҳанд.\n"


                                    "Агар шаҳрвандоне, ки дар  руйхати мазкур қарор дошта бошанд ва ФР-ро бо хоҳиши худ тарк кардаанд, ихроҷ(депортатсия) шудаанд ё дар қаламрави Тоҷикистон ё дигар давлат қарор дошта бошанд, нусхаи шиносномаи хориҷии худро бо нишон додани муҳри убури сарҳад бо мақсади аз рӯйхати мазкур баровардан ба мақомоти муҳоҷирати ҷойи зисти худ дар шаҳру ноҳияҳои ҷумҳурӣ пешниҳод  намоянд.\n"


                                    "Агар шумо дорои душаҳрвандӣ Ҷумҳурии Тоҷикистон ва Федератсияи Россия бошед ё қонунӣ фаъолияти меҳнати менамоед ва дар рӯйхат қарор доред, ҳатман нусхаи шиносномаи худро ба Намояндагии Вазорат дар ФР оид ба муҳоҷират пешниҳод намоед.\n "


                                    "Шаҳрвандоне, ки дар қаламрави ФР қарор доранд, метавонанд ба Намояндагии Вазорати меҳнат, муҳоҷират ва шуғли аҳолӣ дар ФР оид ба муҳоҷират тавассути телефонҳои дар зер нишон дода шуда, муроҷиат намоянд."
                                    "Барои муайян намудани вазъи ҳуқуқии худ аз сомонаҳои расмии Вазорати меҳнат, муҳоҷират ва шуғли аҳолии Ҷумҳурии Тоҷикистон mehnat,tj, саҳифаи телеграм t,me/mlmert, Хадамоти муҳоҷират migration,tj, Намояндагии Вазорат дар ФР оид ба муҳоҷират tajmigration,ru ва Вазорати корҳои дохилии Ҷумҳурии Тоҷикистон vkd,tj истифода намоед.\n"
                                    "👇👇👇👇👇👇👇👇\n"
                                    "\n"
                                    "Барои истифодаи бот, лутфан ба каналҳои зерин обуна шавед:\n"
                                    "👇👇👇👇👇👇👇👇\n"
                                    "🛜 ✅ - 🛜 ✅ - 🛜 ✅ - 🛜 ✅", 
                         reply_markup=markup)
    
    check_subscription_button = InlineKeyboardMarkup()
    check_subscription_button.add(InlineKeyboardButton("Обуна шудам", callback_data="check_subscription"))
    
    send_message_to_user(message.chat.id, "Пас аз обуна шудан, тугмаи 'Обуна шудам'-ро пахш кунед:", 
                         reply_markup=check_subscription_button)

def is_subscribed(user_id):
    channels = ['@tecnotoj04', '@qalbb04']
    
    for channel in channels:
        try:
            member_status = bot.get_chat_member(channel, user_id).status
            if member_status not in ['member', 'administrator', 'creator']:
                return False
        except Exception as e:
            print(f"Error checking subscription for {channel}: {e}")
            return False
    
    return True

@bot.callback_query_handler(func=lambda call: call.data == "check_subscription")
def continue_process(call):
    if is_subscribed(call.message.chat.id):
        send_message_to_user(call.message.chat.id, "Обуна санҷида шуд!\n✅️✅️✅️✅️✅️✅️\n Лутфан вилояти худро интихоб кунед:\n")

        region_markup = InlineKeyboardMarkup()
        region_markup.row_width = 1
        region_markup.add(InlineKeyboardButton("Рӯйхати шаҳрвандон аз ВМКБ", callback_data="vmkb"),
                          InlineKeyboardButton("Рӯйхати шаҳрвандон аз ш.Душанбе", callback_data="dushanbe"),
                          InlineKeyboardButton("Рӯйхати шаҳрвандон аз в.Хатлон", callback_data="hatlon"),
                          InlineKeyboardButton("Рӯйхати шаҳрвандон аз в.Суғд", callback_data="sugd"),
                          InlineKeyboardButton("Рӯйхати шаҳрвандон аз ШНТҶ", callback_data="tobe"))
        
        send_message_to_user(call.message.chat.id, "ИНТИХОБ КУНЕД:\n↘️⬇️⬇️⬇️⬇️⬇️↙️", reply_markup=region_markup)
    else:
        send_message_to_user(call.message.chat.id, "Шумо ба каналҳо обуна нашудаед.\n❌❌❌❌❌\n Лутфан аввал обуна шавед!")

@bot.callback_query_handler(func=lambda call: call.data in ["vmkb", "dushanbe", "hatlon", "sugd", "tobe"])
def region_selection(call):
    chat_id = call.message.chat.id

    if chat_id in user_data and "region" not in user_data[chat_id]:
        region_map = {
            "vmkb": "ВМКБ",
            "dushanbe": "ш.Душанбе",
            "hatlon": "в.Хатлон",
            "sugd": "в.Суғд",
            "tobe": "ШНТҶ"
        }
        
        user_data[chat_id]["region"] = region_map[call.data]
        send_message_to_user(chat_id, f"Шумо вилояти {region_map[call.data]}-ро интихоб кардед.\n\n"
                                   f"Лутфан ном ва насаб ва санаи тавалуди \n\n худро ҳамчун шиноснома ворид кунед мисол:\n\n\n✅️✅️✅️  Солеҳзода Шоҳбегхуҷа Абдулло , 24.08.2004  ✅️✅️✅️\n\n\n (бе хатогӣ):\n <,>вергул мондан мобайни ном ва \n санаи тавалуд фаромуш нашавад")
    else:
        send_message_to_user(chat_id, "Маъзрат, аслии манзил мавҷуд нест.")

@bot.message_handler(func=lambda message: "region" in user_data.get(message.chat.id, {}))
def receive_name(message):
    chat_id = message.chat.id

    if chat_id in user_data:
        user_data[chat_id]["name"] = message.text.strip()

        cursor.execute("SELECT name, address, nohiya FROM users WHERE similarity(name, %s) > 0.7", (user_data[chat_id]["name"],))
        result = cursor.fetchone()

        if result:
            send_message_to_user(chat_id, f"Маълумот ёфт шуд: {result[0]} {result[1]} ({result[2]})\n\n\n"
                                          "🔴Шумо дар рӯйхат ҳастед.🔴")
            send_message_to_user(chat_id, f"ДИҚАТТ:эҳтимоли хато кардани бот ҳаст.\nҶадвалҳои руйхатро метавонед да ин канал пайдо кунед,\n↘️⬇️⬇️⬇️⬇️⬇️↙️\nhttps://t.me/tecnotoj04")                              
        else:
            send_message_to_user(chat_id, "🟢Шумо дар рӯйхат нестед.🟢")
            send_message_to_user(chat_id, f"ДИҚАТТ:эҳтимоли хато кардани бот ҳаст\nҶадвалҳои руйхатро метавонед да ин канал пайдо кунед,\n↘️⬇️⬇️⬇️⬇️⬇️↙️\nhttps://t.me/tecnotoj04")                              
        
        search_again_markup = InlineKeyboardMarkup()
        search_again_markup.add(InlineKeyboardButton("Дубора санҷидан", callback_data="search_again"))
        send_message_to_user(chat_id, "⚠️ХАМВАТАНХОИ ГИРОМИ!⚠️\n"

                                      "1- АГАР ЯГОН КАС ГУЯД МАН КУМАК МЕКУНАМ БАРОИ АЗ ИН СПИСОК ТОЗА КАРДАНИ НОМАТОН БОВАР НАКУНЕД!!\n"
                                      "ДУРУГ АСТ!\n"
                                      "БА ЯГОН КАС ЯГОН ТИН НАПАРТОЕД!\n\n"

                                      "БАЪЗЕ МОШЕНИКХО АЗ МОМЕНТ ИСТИФОДА КАРДА ХАРХЕЛ БОТ ВА САЙТХО СОХТЕСТАН, КИ ИНЧО ДАРО НОМАТРО САНЧ ГУФТА ПЕШНИХОД МЕКУНАНД ЭХТИЁТ ШАВЕД!\n\n"
     
                                      "ЯГОНХЕЛ ССЫЛКАХО БОШАД НАДАРОЕД, КИ МАБЛАГХОЯТОН АВТОМАТИ АЗ КАРТАХОЯТОН СНИМАТЬ МЕШАВАД!\n\n"

                                      "АЛЛАКАЙ БА МАЪЛУМОТИ МАН ФИРЕБХУРДАГИХО ХАСТАНД! \n\n"
                                      "Агар мехоҳед дубора санҷед, тугмаи 'Дубора санҷидан'-ро пахш кунед:", 
                             reply_markup=search_again_markup)

@bot.callback_query_handler(func=lambda call: call.data == "search_again")
def search_again(call):
    send_message_to_user(call.message.chat.id, "Лутфан ном ва насаби худро дубора ворид кунед:\n↘️⬇️⬇️⬇️⬇️⬇️↙️")

bot.polling(non_stop=True, interval=0, timeout=60, long_polling_timeout=60)
