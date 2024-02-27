from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, Bot, InputMediaPhoto, InputMediaVideo
from telegram.ext import CallbackContext
from telegram.parsemode import ParseMode
from pprint import pprint
import json
from .messages import *
from .buttons import *
from settings import *
from database.db import *
bot = Bot(token=TOKEN)

def update_to_json(update: Update) -> str:
    update_dict = update.to_dict()
    update_json = json.dumps(update_dict, indent=4)
    return update_json

def handle_messages(update: Update, context) -> None:
    update_json = update_to_json(update)
    print(update_json)

def start(update: Update, context):
    user_id = update.effective_chat.id
    full_name = update.effective_chat.full_name
    is_subscribed = bot.get_chat_member(GROUP, user_id).status in "creator, member, admin"
    print(is_subscribed)

    if is_subscribed == True:
        if True:
            us = get(table="users", user_id=user_id)
            if not us:
                insert(table="users",user_id=user_id, data={"user_id": user_id, "full_name": full_name})
                insert(table="stage", user_id=user_id, data={"stage": "start"})
                insert(table="index",user_id=user_id, data={"Telefonlar📱": 1, "Telefon jihozlari⚙️": 1, "Quloqliklar🎧": 1, "Soatlar⌚️": 1,"Avtomobil jihozlari⚙️": 1,"Pultlar🕹": 1, "Sichqonchalar🖱": 1, "Fonarlar🔦": 1, "Bataraeykalar🔋": 1,"Kamyob aksessuarlar💎":1, "hamma": 1})
                update.message.reply_photo(
                    photo=START_PHOTO,
                    caption=users_start,
                    reply_markup=ReplyKeyboardMarkup(users_start_but, resize_keyboard=True))
                
            else:
                first = update.effective_chat.first_name
                update.message.reply_photo(
                    photo=START_PHOTO,
                    caption=users_start2,
                    reply_markup=ReplyKeyboardMarkup(users_start_but, resize_keyboard=True))
        else:
            pass
    else:
        update.message.reply_text(
            text="Botdan foydalanish uchun Guruhimizga qo'shiling😊",
            reply_markup=InlineKeyboardMarkup(inline_keyboard)
        )
        
def text(update: Update, context):
    user_id = update.effective_chat.id
    xab = update.message.text
    stage = get(table="stage", user_id=user_id)['stage']
    try:
        index = get(table="index", user_id=user_id)[xab]
    except:
        index = None
    tip = Query()
    if user_id == ADMIN_ID:

        if xab == "Telefonlar📱":
            update.message.reply_text(
                text="Tovar qo'shish uchun Rasm yoki Video jo'nating➕...",
                reply_markup=ReplyKeyboardMarkup(add_acces, resize_keyboard=True)
            )
            upd(table="stage", user_id=user_id, data={"stage": xab}) 
        if xab == "Telefon jihozlari⚙️":
            update.message.reply_text(
                text="Tovar qo'shish uchun Rasm yoki Video jo'nating➕...",
                reply_markup=ReplyKeyboardMarkup(add_acces, resize_keyboard=True)
            )
            upd(table="stage", user_id=user_id, data={"stage": xab})          
        if xab == "Quloqliklar🎧":
            update.message.reply_text(
                text="Tovar qo'shish uchun Rasm yoki Video jo'nating➕...",
                reply_markup=ReplyKeyboardMarkup(add_acces, resize_keyboard=True)
            )
            upd(table="stage", user_id=user_id, data={"stage": xab})
        if xab == "Soatlar⌚️":
            update.message.reply_text(
                text="Tovar qo'shish uchun Rasm yoki Video jo'nating➕...",
                reply_markup=ReplyKeyboardMarkup(add_acces, resize_keyboard=True)
            )
            upd(table="stage", user_id=user_id, data={"stage": xab})
        if xab == "Avtomobil jihozlari⚙️":
            update.message.reply_text(
                text="Tovar qo'shish uchun Rasm yoki Video jo'nating➕...",
                reply_markup=ReplyKeyboardMarkup(add_acces, resize_keyboard=True)
            )
            upd(table="stage", user_id=user_id, data={"stage": xab})
        if xab == "Ko'proq tovarlar🖇":
            update.message.reply_text(
                text="Pastdagi bo'limlardan birini tanlang👇",
                reply_markup=ReplyKeyboardMarkup(boshqa_tovarlar_but, resize_keyboard=True)
            )
            upd(table="stage", user_id=user_id, data={"stage": xab})
        if xab == "Pultlar🕹":
            update.message.reply_text(
                text="Tovar qo'shish uchun Rasm yoki Video jo'nating➕...",
                reply_markup=ReplyKeyboardMarkup(add_acces, resize_keyboard=True)
            )
            upd(table="stage", user_id=user_id, data={"stage": xab})
        if xab == "Sichqonchalar🖱":
            update.message.reply_text(
                text="Tovar qo'shish uchun Rasm yoki Video jo'nating➕...",
                reply_markup=ReplyKeyboardMarkup(add_acces, resize_keyboard=True)
            )
            upd(table="stage", user_id=user_id, data={"stage": xab})
        if xab == "Fonarlar🔦":
            update.message.reply_text(
                text="Tovar qo'shish uchun Rasm yoki Video jo'nating➕...",
                reply_markup=ReplyKeyboardMarkup(add_acces, resize_keyboard=True)
            )
            upd(table="stage", user_id=user_id, data={"stage": xab})
        if xab == "Bataraeykalar🔋":
            update.message.reply_text(
                text="Tovar qo'shish uchun Rasm yoki Video jo'nating➕...",
                reply_markup=ReplyKeyboardMarkup(add_acces, resize_keyboard=True)
            )
            upd(table="stage", user_id=user_id, data={"stage": xab})
        if xab == "Kamyob aksessuarlar💎":
            update.message.reply_text(
                text="Tovar qo'shish uchun Rasm yoki Video jo'nating➕...:",
                reply_markup=ReplyKeyboardMarkup(add_acces, resize_keyboard=True)
            )
            upd(table="stage", user_id=user_id, data={"stage": xab})
        if xab == "Ortga🔙":
            if True:
                update.message.reply_text(
                    text=users_start2,
                    reply_markup=ReplyKeyboardMarkup(users_start_but, resize_keyboard=True)
                )
                upd(table="stage", user_id=user_id, data={"stage": xab})
                upd(table="stage", user_id=user_id, data={"pricing": "false"})
        else:
            try:
                stage_pricing = get(table="stage", user_id=user_id)['pricing']
                print(db2.all()[-1])
                if stage_pricing == "true":

                    upd(table="products",product=stage, data={"price": xab})
                    update.message.reply_text(
                    text="Aksessuar muvaffaqiyatli qo'shildi",
                    reply_markup=ReplyKeyboardMarkup(add_acces, resize_keyboard=True)
                    )
                    tip = Query()
                    product = db2.search(tip.type == stage)
                    data = product[-1]
                    pprint(data)
                    if data['media'] == "photo":
                        print("rasm ketdi")
                        try:
                            bot.send_photo(photo=data['file_id'], caption=f"<b>Yangi tovar rasmi❗️\n\nBo'lim:</b> {stage} \n<b>Mahsulot</b>: {data['text']}\n<b>Narxi:</b> {data['price']}💸\n\n<i>Manzilimiz</i>: {MANZIL}📍",chat_id=GROUP, parse_mode=ParseMode.HTML, reply_markup=InlineKeyboardMarkup(group_button))
                        except: 
                            bot.send_photo(photo=data['file_id'], caption=f"<b>Yangi tovar rasmi❗️\n\nBo'lim</b>: {stage}\n<b>Narxi:</b> {data['price']}💸\n\n<i>Manzilimiz</i>: {MANZIL}📍",chat_id=GROUP, parse_mode=ParseMode.HTML, reply_markup=InlineKeyboardMarkup(group_button))
                    else:
                        print('video ketdi')
                        try:
                            caption = f"<b>Yangi tovar videosi</b>❗️\n \n <b>Mahsulot</b>: {data['message']['caption']}\n <b>Bo'lim </b>: {stage}\n<b>Narxi:</b> {data['price']}💸\n\n<i>Manzilimiz</i>: {MANZIL}📍"
                            bot.send_video(video=data["message"]['video']['file_id'], caption=caption, chat_id=GROUP, parse_mode=ParseMode.HTML, reply_markup=InlineKeyboardMarkup(group_button))
                        except:
                            
                            caption = f"<b>Yangi tovar</b>❗️\n\n <b>Bo'lim </b>: {stage}\n<b>Narxi:</b> {data['price']}💸\n\n<i>Manzilimiz</i>: {MANZIL}📍"
                            bot.send_video(video=data["message"]['video']['file_id'], caption=caption, chat_id=GROUP, parse_mode=ParseMode.HTML, reply_markup=InlineKeyboardMarkup(group_button))
                else:
                    print("Stage pricing True emas!")
            except:
                pass
        
    else:
        if xab == "Ko'proq tovarlar🖇":
            update.message.reply_text(
                text="Ko'proq tovarlar🖇",
                reply_markup=ReplyKeyboardMarkup(boshqa_tovarlar_but, resize_keyboard=True)
            )
        if xab == "Statistika📊":
            update.message.reply_photo(
                photo=STATS_PHOTO,
                caption=stats_mes.format(len(get(table="users")), len(db2.all())),
                reply_markup=ReplyKeyboardMarkup(add_acces, resize_keyboard=True),
                parse_mode=ParseMode.HTML
            )
        if xab == "Ortga🔙":
            if True:
                update.message.reply_text(
                    text=users_start2,
                    reply_markup=ReplyKeyboardMarkup(users_start_but, resize_keyboard=True)
                )
            else:
                pass
        if xab == "Zakaz berish":
            update.message.reply_photo(
                photo=START_PHOTO,
                caption=zakaz_ber,
                reply_markup=ReplyKeyboardMarkup(add_acces, resize_keyboard=True),
                parse_mode=ParseMode.HTML
            )
        if index >= len(db2.search(tip.type == xab)):
            upd(table="index", user_id=user_id, data={xab: 0})

        

        if xab == "Kamyob aksessuarlar💎":
            update.message.reply_text(
                text=xab,
                reply_markup=ReplyKeyboardMarkup(add_acces, resize_keyboard=True)
            )
            
            tip = Query()
            product = db2.search(tip.type == xab)
            print(product)
            media = product[index]['media']
            index = get(table="index",user_id=user_id)[xab]
            if media == "photo":
                try:
                    update.message.reply_photo(
                    photo=product[index]['file_id'],
                    caption=f"<b>{xab}: </b>{index+1}\{len(product)}🔗\n<b>Mahsulot: </b>{product[index]['text']}\n<b>Narxi:</b> {product[index]['price']}💸\n\n<i>Manzil: </i> {MANZIL} 📍",
                    reply_markup=InlineKeyboardMarkup(next_prev_but),
                    parse_mode=ParseMode.HTML
                )
                except:
                    update.message.reply_photo(
                    photo=product[index]['file_id'],
                    caption=f"<b>{xab}: </b>{index+1}\{len(product)}🔗\n<b>Narxi:</b> {product[index]['price']}💸\n\n<i>Manzil: </i> {MANZIL} 📍",
                    reply_markup=InlineKeyboardMarkup(next_prev_but),
                    parse_mode=ParseMode.HTML
                    )
            elif media == "video":
                try:
                    update.message.reply_video(
                    video=product[index]['file_id'],
                    caption=f"<b>{xab}: </b>{index+1}\{len(product)}🔗\n<b>Mahsulot: </b>{product[index]['text']}\n<b>Narxi:</b> {product[index]['price']}💸\n\n<i>Manzil: </i> {MANZIL} 📍",
                    reply_markup=InlineKeyboardMarkup(next_prev_but),
                    parse_mode=ParseMode.HTML)
                except:
                    update.message.reply_video(
                    video=product[index]['file_id'],
                    caption=f"<b>{xab}: </b>{index+1}\{len(product)}🔗\n<b>Narxi:</b> {product[index]['price']}💸\n\n<i>Manzil: </i> {MANZIL} 📍",
                    reply_markup=InlineKeyboardMarkup(next_prev_but),
                    parse_mode=ParseMode.HTML)
            upd(table="index",user_id=user_id, data={xab: index+1})

        if xab == "Telefonlar📱":
            update.message.reply_text(
                text=xab,
                reply_markup=ReplyKeyboardMarkup(add_acces, resize_keyboard=True)
            )
            
            tip = Query()
            product = db2.search(tip.type == xab)
            print(product)
            media = product[index]['media']
            index = get(table="index",user_id=user_id)[xab]
            if media == "photo":
                try:
                    update.message.reply_photo(
                    photo=product[index]['file_id'],
                    caption=f"<b>{xab}: </b>{index+1}\{len(product)}🔗\n<b>Mahsulot: </b>{product[index]['text']}\n<b>Narxi:</b> {product[index]['price']}💸\n\n<i>Manzil: </i> {MANZIL} 📍",
                    reply_markup=InlineKeyboardMarkup(next_prev_but),
                    parse_mode=ParseMode.HTML
                )
                except:
                    update.message.reply_photo(
                    photo=product[index]['file_id'],
                    caption=f"<b>{xab}: </b>{index+1}\{len(product)}🔗\n<b>Narxi:</b> {product[index]['price']}💸\n\n<i>Manzil: </i> {MANZIL} 📍",
                    reply_markup=InlineKeyboardMarkup(next_prev_but),
                    parse_mode=ParseMode.HTML
                    )
            elif media == "video":
                try:
                    update.message.reply_video(
                    video=product[index]['file_id'],
                    caption=f"<b>{xab}: </b>{index+1}\{len(product)}🔗\n<b>Mahsulot: </b>{product[index]['text']}\n<b>Narxi:</b> {product[index]['price']}💸\n\n<i>Manzil: </i> {MANZIL} 📍",
                    reply_markup=InlineKeyboardMarkup(next_prev_but),
                    parse_mode=ParseMode.HTML)
                except:
                    update.message.reply_video(
                    video=product[index]['file_id'],
                    caption=f"<b>{xab}: </b>{index+1}\{len(product)}🔗\n<b>Narxi:</b> {product[index]['price']}💸\n\n<i>Manzil: </i> {MANZIL} 📍",
                    reply_markup=InlineKeyboardMarkup(next_prev_but),
                    parse_mode=ParseMode.HTML)
            upd(table="index",user_id=user_id, data={xab: index+1})
            
        if xab == "Telefon jihozlari⚙️":
            update.message.reply_text(
                text=xab,
                reply_markup=ReplyKeyboardMarkup(add_acces, resize_keyboard=True)
            )
            
            tip = Query()
            product = db2.search(tip.type == xab)
            print(product)
            media = product[index]['media']
            index = get(table="index",user_id=user_id)[xab]
            if media == "photo":
                try:
                    update.message.reply_photo(
                    photo=product[index]['file_id'],
                    caption=f"<b>{xab}: </b>{index+1}\{len(product)}🔗\n<b>Mahsulot: </b>{product[index]['text']}\n<b>Narxi:</b> {product[index]['price']}💸\n\n<i>Manzil: </i> {MANZIL} 📍",
                    reply_markup=InlineKeyboardMarkup(next_prev_but),
                    parse_mode=ParseMode.HTML
                )
                except:
                    update.message.reply_photo(
                    photo=product[index]['file_id'],
                    caption=f"<b>{xab}: </b>{index+1}\{len(product)}🔗\n<b>Narxi:</b> {product[index]['price']}💸\n\n<i>Manzil: </i> {MANZIL} 📍",
                    reply_markup=InlineKeyboardMarkup(next_prev_but),
                    parse_mode=ParseMode.HTML
                    )
            elif media == "video":
                try:
                    update.message.reply_video(
                    video=product[index]['file_id'],
                    caption=f"<b>{xab}: </b>{index+1}\{len(product)}🔗\n<b>Mahsulot: </b>{product[index]['text']}\n<b>Narxi:</b> {product[index]['price']}💸\n\n<i>Manzil: </i> {MANZIL} 📍",
                    reply_markup=InlineKeyboardMarkup(next_prev_but),
                    parse_mode=ParseMode.HTML)
                except:
                    update.message.reply_video(
                    video=product[index]['file_id'],
                    caption=f"<b>{xab}: </b>{index+1}\{len(product)}🔗\n<b>Narxi:</b> {product[index]['price']}💸\n\n<i>Manzil: </i> {MANZIL} 📍",
                    reply_markup=InlineKeyboardMarkup(next_prev_but),
                    parse_mode=ParseMode.HTML)
            upd(table="index",user_id=user_id, data={xab: index+1})
            
        if xab == "Quloqliklar🎧":
            update.message.reply_text(
                text=xab,
                reply_markup=ReplyKeyboardMarkup(add_acces, resize_keyboard=True)
            )
            
            tip = Query()
            product = db2.search(tip.type == xab)
            print(product)
            media = product[index]['media']
            index = get(table="index",user_id=user_id)[xab]
            if media == "photo":
                try:
                    update.message.reply_photo(
                    photo=product[index]['file_id'],
                    caption=f"<b>{xab}: </b>{index+1}\{len(product)}🔗\n<b>Mahsulot: </b>{product[index]['text']}\n<b>Narxi:</b> {product[index]['price']}💸\n\n<i>Manzil: </i> {MANZIL} 📍",
                    reply_markup=InlineKeyboardMarkup(next_prev_but),
                    parse_mode=ParseMode.HTML
                )
                except:
                    update.message.reply_photo(
                    photo=product[index]['file_id'],
                    caption=f"<b>{xab}: </b>{index+1}\{len(product)}🔗\n<b>Narxi:</b> {product[index]['price']}💸\n\n<i>Manzil: </i> {MANZIL} 📍",
                    reply_markup=InlineKeyboardMarkup(next_prev_but),
                    parse_mode=ParseMode.HTML
                    )
            elif media == "video":
                try:
                    update.message.reply_video(
                    video=product[index]['file_id'],
                    caption=f"<b>{xab}: </b>{index+1}\{len(product)}🔗\n<b>Mahsulot: </b>{product[index]['text']}\n<b>Narxi:</b> {product[index]['price']}💸\n\n<i>Manzil: </i> {MANZIL} 📍",
                    reply_markup=InlineKeyboardMarkup(next_prev_but),
                    parse_mode=ParseMode.HTML)
                except:
                    update.message.reply_video(
                    video=product[index]['file_id'],
                    caption=f"<b>{xab}: </b>{index+1}\{len(product)}🔗\n<b>Narxi:</b> {product[index]['price']}💸\n\n<i>Manzil: </i> {MANZIL} 📍",
                    reply_markup=InlineKeyboardMarkup(next_prev_but),
                    parse_mode=ParseMode.HTML)
            upd(table="index",user_id=user_id, data={xab: index+1})
        if xab == "Soatlar⌚️":
            update.message.reply_text(
                text=xab,
                reply_markup=ReplyKeyboardMarkup(add_acces, resize_keyboard=True)
            )
            
            tip = Query()
            product = db2.search(tip.type == xab)
            print(product)
            media = product[index]['media']
            index = get(table="index",user_id=user_id)[xab]
            if media == "photo":
                try:
                    update.message.reply_photo(
                    photo=product[index]['file_id'],
                    caption=f"<b>{xab}: </b>{index+1}\{len(product)}🔗\n<b>Mahsulot: </b>{product[index]['text']}\n<b>Narxi:</b> {product[index]['price']}💸\n\n<i>Manzil: </i> {MANZIL} 📍",
                    reply_markup=InlineKeyboardMarkup(next_prev_but),
                    parse_mode=ParseMode.HTML
                )
                except:
                    update.message.reply_photo(
                    photo=product[index]['file_id'],
                    caption=f"<b>{xab}: </b>{index+1}\{len(product)}🔗\n<b>Narxi:</b> {product[index]['price']}💸\n\n<i>Manzil: </i> {MANZIL} 📍",
                    reply_markup=InlineKeyboardMarkup(next_prev_but),
                    parse_mode=ParseMode.HTML
                    )
            elif media == "video":
                try:
                    update.message.reply_video(
                    video=product[index]['file_id'],
                    caption=f"<b>{xab}: </b>{index+1}\{len(product)}🔗\n<b>Mahsulot: </b>{product[index]['text']}\n<b>Narxi:</b> {product[index]['price']}💸\n\n<i>Manzil: </i> {MANZIL} 📍",
                    reply_markup=InlineKeyboardMarkup(next_prev_but),
                    parse_mode=ParseMode.HTML)
                except:
                    update.message.reply_video(
                    video=product[index]['file_id'],
                    caption=f"<b>{xab}: </b>{index+1}\{len(product)}🔗\n<b>Narxi:</b> {product[index]['price']}💸\n\n<i>Manzil: </i> {MANZIL} 📍",
                    reply_markup=InlineKeyboardMarkup(next_prev_but),
                    parse_mode=ParseMode.HTML)
            upd(table="index",user_id=user_id, data={xab: index+1})
        if xab == "Avtomobil jihozlari⚙️":
            update.message.reply_text(
                text=xab,
                reply_markup=ReplyKeyboardMarkup(add_acces, resize_keyboard=True)
            )
            
            tip = Query()
            product = db2.search(tip.type == xab)
            print(product)
            media = product[index]['media']
            index = get(table="index",user_id=user_id)[xab]
            if media == "photo":
                try:
                    update.message.reply_photo(
                    photo=product[index]['file_id'],
                    caption=f"<b>{xab}: </b>{index+1}\{len(product)}🔗\n<b>Mahsulot: </b>{product[index]['text']}\n<b>Narxi:</b> {product[index]['price']}💸\n\n<i>Manzil: </i> {MANZIL} 📍",
                    reply_markup=InlineKeyboardMarkup(next_prev_but),
                    parse_mode=ParseMode.HTML
                )
                except:
                    update.message.reply_photo(
                    photo=product[index]['file_id'],
                    caption=f"<b>{xab}: </b>{index+1}\{len(product)}🔗\n<b>Narxi:</b> {product[index]['price']}💸\n\n<i>Manzil: </i> {MANZIL} 📍",
                    reply_markup=InlineKeyboardMarkup(next_prev_but),
                    parse_mode=ParseMode.HTML
                    )
            elif media == "video":
                try:
                    update.message.reply_video(
                    video=product[index]['file_id'],
                    caption=f"<b>{xab}: </b>{index+1}\{len(product)}🔗\n<b>Mahsulot: </b>{product[index]['text']}\n<b>Narxi:</b> {product[index]['price']}💸\n\n<i>Manzil: </i> {MANZIL} 📍",
                    reply_markup=InlineKeyboardMarkup(next_prev_but),
                    parse_mode=ParseMode.HTML)
                except:
                    update.message.reply_video(
                    video=product[index]['file_id'],
                    caption=f"<b>{xab}: </b>{index+1}\{len(product)}🔗\n<b>Narxi:</b> {product[index]['price']}💸\n\n<i>Manzil: </i> {MANZIL} 📍",
                    reply_markup=InlineKeyboardMarkup(next_prev_but),
                    parse_mode=ParseMode.HTML)
            upd(table="index",user_id=user_id, data={xab: index+1})
        if xab == "Ko'proq tovarlar🖇":
            update.message.reply_text(
                text="Pastdagi bo'limlardan birini tanlang👇",
                reply_markup=ReplyKeyboardMarkup(boshqa_tovarlar_but, resize_keyboard=True)
            )
        if xab == "Pultlar🕹":
            update.message.reply_text(
                text=xab,
                reply_markup=ReplyKeyboardMarkup(add_acces, resize_keyboard=True)
            )
            
            tip = Query()
            product = db2.search(tip.type == xab)
            print(product)
            media = product[index]['media']
            index = get(table="index",user_id=user_id)[xab]
            if media == "photo":
                try:
                    update.message.reply_photo(
                    photo=product[index]['file_id'],
                    caption=f"<b>{xab}: </b>{index+1}\{len(product)}🔗\n<b>Mahsulot: </b>{product[index]['text']}\n<b>Narxi:</b> {product[index]['price']}💸\n\n<i>Manzil: </i> {MANZIL} 📍",
                    reply_markup=InlineKeyboardMarkup(next_prev_but),
                    parse_mode=ParseMode.HTML
                )
                except:
                    update.message.reply_photo(
                    photo=product[index]['file_id'],
                    caption=f"<b>{xab}: </b>{index+1}\{len(product)}🔗\n<b>Narxi:</b> {product[index]['price']}💸\n\n<i>Manzil: </i> {MANZIL} 📍",
                    reply_markup=InlineKeyboardMarkup(next_prev_but),
                    parse_mode=ParseMode.HTML
                    )
            elif media == "video":
                try:
                    update.message.reply_video(
                    video=product[index]['file_id'],
                    caption=f"<b>{xab}: </b>{index+1}\{len(product)}🔗\n<b>Mahsulot: </b>{product[index]['text']}\n<b>Narxi:</b> {product[index]['price']}💸\n\n<i>Manzil: </i> {MANZIL} 📍",
                    reply_markup=InlineKeyboardMarkup(next_prev_but),
                    parse_mode=ParseMode.HTML)
                except:
                    update.message.reply_video(
                    video=product[index]['file_id'],
                    caption=f"<b>{xab}: </b>{index+1}\{len(product)}🔗\n<b>Narxi:</b> {product[index]['price']}💸\n\n<i>Manzil: </i> {MANZIL} 📍",
                    reply_markup=InlineKeyboardMarkup(next_prev_but),
                    parse_mode=ParseMode.HTML)
            upd(table="index",user_id=user_id, data={xab: index+1})
        if xab == "Sichqonchalar🖱":
            update.message.reply_text(
                text=xab,
                reply_markup=ReplyKeyboardMarkup(add_acces, resize_keyboard=True)
            )
            
            tip = Query()
            product = db2.search(tip.type == xab)
            print(product)
            media = product[index]['media']
            index = get(table="index",user_id=user_id)[xab]
            if media == "photo":
                try:
                    update.message.reply_photo(
                    photo=product[index]['file_id'],
                    caption=f"<b>{xab}: </b>{index+1}\{len(product)}🔗\n<b>Mahsulot: </b>{product[index]['text']}\n<b>Narxi:</b> {product[index]['price']}💸\n\n<i>Manzil: </i> {MANZIL} 📍",
                    reply_markup=InlineKeyboardMarkup(next_prev_but),
                    parse_mode=ParseMode.HTML
                )
                except:
                    update.message.reply_photo(
                    photo=product[index]['file_id'],
                    caption=f"<b>{xab}: </b>{index+1}\{len(product)}🔗\n<b>Narxi:</b> {product[index]['price']}💸\n\n<i>Manzil: </i> {MANZIL} 📍",
                    reply_markup=InlineKeyboardMarkup(next_prev_but),
                    parse_mode=ParseMode.HTML
                    )
            elif media == "video":
                try:
                    update.message.reply_video(
                    video=product[index]['file_id'],
                    caption=f"<b>{xab}: </b>{index+1}\{len(product)}🔗\n<b>Mahsulot: </b>{product[index]['text']}\n<b>Narxi:</b> {product[index]['price']}💸\n\n<i>Manzil: </i> {MANZIL} 📍",
                    reply_markup=InlineKeyboardMarkup(next_prev_but),
                    parse_mode=ParseMode.HTML)
                except:
                    update.message.reply_video(
                    video=product[index]['file_id'],
                    caption=f"<b>{xab}: </b>{index+1}\{len(product)}🔗\n<b>Narxi:</b> {product[index]['price']}💸\n\n<i>Manzil: </i> {MANZIL} 📍",
                    reply_markup=InlineKeyboardMarkup(next_prev_but),
                    parse_mode=ParseMode.HTML)
            upd(table="index",user_id=user_id, data={xab: index+1})
        if xab == "Fonarlar🔦":
            update.message.reply_text(
                text=xab,
                reply_markup=ReplyKeyboardMarkup(add_acces, resize_keyboard=True)
            )
            
            tip = Query()
            product = db2.search(tip.type == xab)
            print(product)
            media = product[index]['media']
            index = get(table="index",user_id=user_id)[xab]
            if media == "photo":
                try:
                    update.message.reply_photo(
                    photo=product[index]['file_id'],
                    caption=f"<b>{xab}: </b>{index+1}\{len(product)}🔗\n<b>Mahsulot: </b>{product[index]['text']}\n<b>Narxi:</b> {product[index]['price']}💸\n\n<i>Manzil: </i> {MANZIL} 📍",
                    reply_markup=InlineKeyboardMarkup(next_prev_but),
                    parse_mode=ParseMode.HTML
                )
                except:
                    update.message.reply_photo(
                    photo=product[index]['file_id'],
                    caption=f"<b>{xab}: </b>{index+1}\{len(product)}🔗\n<b>Narxi:</b> {product[index]['price']}💸\n\n<i>Manzil: </i> {MANZIL} 📍",
                    reply_markup=InlineKeyboardMarkup(next_prev_but),
                    parse_mode=ParseMode.HTML
                    )
            elif media == "video":
                try:
                    update.message.reply_video(
                    video=product[index]['file_id'],
                    caption=f"<b>{xab}: </b>{index+1}\{len(product)}🔗\n<b>Mahsulot: </b>{product[index]['text']}\n<b>Narxi:</b> {product[index]['price']}💸\n\n<i>Manzil: </i> {MANZIL} 📍",
                    reply_markup=InlineKeyboardMarkup(next_prev_but),
                    parse_mode=ParseMode.HTML)
                except:
                    update.message.reply_video(
                    video=product[index]['file_id'],
                    caption=f"<b>{xab}: </b>{index+1}\{len(product)}🔗\n<b>Narxi:</b> {product[index]['price']}💸\n\n<i>Manzil: </i> {MANZIL} 📍",
                    reply_markup=InlineKeyboardMarkup(next_prev_but),
                    parse_mode=ParseMode.HTML)
            upd(table="index",user_id=user_id, data={xab: index+1})
        if xab == "Bataraeykalar🔋":
            update.message.reply_text(
                text=xab,
                reply_markup=ReplyKeyboardMarkup(add_acces, resize_keyboard=True)
            )
            
            tip = Query()
            product = db2.search(tip.type == xab)
            print(product)
            media = product[index]['media']
            index = get(table="index",user_id=user_id)[xab]
            if media == "photo":
                try:
                    update.message.reply_photo(
                    photo=product[index]['file_id'],
                    caption=f"<b>{xab}: </b>{index+1}\{len(product)}🔗\n<b>Mahsulot: </b>{product[index]['text']}\n<b>Narxi:</b> {product[index]['price']}💸\n\n<i>Manzil: </i> {MANZIL} 📍",
                    reply_markup=InlineKeyboardMarkup(next_prev_but),
                    parse_mode=ParseMode.HTML
                )
                except:
                    update.message.reply_photo(
                    photo=product[index]['file_id'],
                    caption=f"<b>{xab}: </b>{index+1}\{len(product)}🔗\n<b>Narxi:</b> {product[index]['price']}💸\n\n<i>Manzil: </i> {MANZIL} 📍",
                    reply_markup=InlineKeyboardMarkup(next_prev_but),
                    parse_mode=ParseMode.HTML
                    )
            elif media == "video":
                try:
                    update.message.reply_video(
                    video=product[index]['file_id'],
                    caption=f"<b>{xab}: </b>{index+1}\{len(product)}🔗\n<b>Mahsulot: </b>{product[index]['text']}\n<b>Narxi:</b> {product[index]['price']}💸\n\n<i>Manzil: </i> {MANZIL} 📍",
                    reply_markup=InlineKeyboardMarkup(next_prev_but),
                    parse_mode=ParseMode.HTML)
                except:
                    update.message.reply_video(
                    video=product[index]['file_id'],
                    caption=f"<b>{xab}: </b>{index+1}\{len(product)}🔗\n<b>Narxi:</b> {product[index]['price']}💸\n\n<i>Manzil: </i> {MANZIL} 📍",
                    reply_markup=InlineKeyboardMarkup(next_prev_but),
                    parse_mode=ParseMode.HTML)
            upd(table="index",user_id=user_id, data={xab: index+1})
        upd(table="stage", user_id=user_id, data={"stage": xab})

        
                
def button_callback(update: Update, context):
    query = update.callback_query
    user_id = query.from_user.id
    first_name = query.from_user.first_name
    full_name = query.from_user.full_name
    if query.data == 'subscribe':
        is_subscribed = bot.get_chat_member(GROUP, user_id).status in "member, creator, admin"
        if is_subscribed == True:
            bot.send_photo(chat_id=user_id, photo=START_PHOTO,caption=users_start.format(first_name), reply_markup=ReplyKeyboardMarkup(users_start_but, resize_keyboard=True))
            if True:
                us = get(table="users", user_id=user_id)
                if not us:
                    insert(table="users",user_id=user_id, data={"user_id": user_id, "full_name": full_name})
                    insert(table="stage", user_id=user_id, data={"stage": "start"})
                    insert(table="index",user_id=user_id,  data={"Telefonlar📱": 1, "Telefon jihozlari⚙️": 1, "Quloqliklar🎧": 1, "Soatlar⌚️": 1,"Avtomobil jihozlari⚙️": 1,"Pultlar🕹": 1, "Sichqonchalar🖱": 1, "Fonarlar🔦": 1, "Bataraeykalar🔋": 1,"Kamyob aksessuarlar💎":1, "hamma": 1})
                    bot.send_photo(chat_id=user_id, photo=START_PHOTO,caption=users_start.format(first_name), reply_markup=ReplyKeyboardMarkup(users_start_but, resize_keyboard=True))
                else:
                    bot.send_photo(chat_id=user_id, photo=START_PHOTO,caption=users_start.format(first_name), reply_markup=ReplyKeyboardMarkup(users_start_but, resize_keyboard=True))
        else:
            query.answer("Siz kanalga a'zo bo'lmagansiz❌")
    if query.data == "next":
        stage = get(table="stage", user_id=user_id)['stage']
        last_index = get(table="index", user_id=user_id)[stage]
        
        tip = Query()
        product = db2.search(tip.type == stage)
        if last_index >= len(product)-1:
            upd(table="index", user_id=user_id, data={stage: 0})
        else:
            upd(table="index", user_id=user_id, data={stage: last_index+1})
        last_index = get(table="index", user_id=user_id)[stage]
        media = product[last_index]['media']
        index = get(table="index",user_id=user_id)[stage]
        # if index >= len(product):
        #     upd(table="index", user_id=user_id, data={stage: 0})
        med = product[last_index]['file_id']

        if media == "photo":
            new_media=InputMediaPhoto(med)
        if media == "video":
            new_media=InputMediaVideo(med)
        try:
            caption = f"<b>{stage}:  </b>{index+1}\{len(product)}🔢 \n<b>Mahsulot: </b>{product[index]['text']}\n<b>Narxi:</b> {product[index]['price']}💸\n\n<i>Manzil: </i> {MANZIL} 📍"
        except:
            caption = f"<b>{stage}:  </b>{index+1}\{len(product)}🔢 \n<b>Narxi:</b> {product[index]['price']}💸\n\n<i>Manzil: </i> {MANZIL} 📍"
        query.edit_message_media(media=new_media)
        query.edit_message_caption(caption=caption, parse_mode=ParseMode.HTML)
        query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(next_prev_but))

    if query.data == "prev":
        stage = get(table="stage", user_id=user_id)['stage']
        last_index = get(table="index", user_id=user_id)[stage]
        
        tip = Query()
        product = db2.search(tip.type == stage)
        if last_index <= 0:
            upd(table="index", user_id=user_id, data={stage: len(product)-1})
        else:
            upd(table="index", user_id=user_id, data={stage: last_index-1})
        last_index = get(table="index", user_id=user_id)[stage]
        media = product[last_index]['media']
        index = get(table="index",user_id=user_id)[stage]
        # if index >= len(product):
        #     upd(table="index", user_id=user_id, data={stage: 0})
        med = product[last_index]['file_id']

        if media == "photo":
            new_media=InputMediaPhoto(med)
        if media == "video":
            new_media=InputMediaVideo(med)
        try:
            caption = f"<b>{stage}:  </b>{index+1}\{len(product)}🔢 \n<b>Mahsulot: </b>{product[index]['text']}\n<b>Narxi:</b> {product[index]['price']}💸\n\n<i>Manzil: </i> {MANZIL} 📍"
        except:
            caption = f"<b>{stage}:  </b>{index+1}\{len(product)}🔢 \n<b>Narxi:</b> {product[index]['price']}💸\n\n<i>Manzil: </i> {MANZIL} 📍"
        query.edit_message_media(media=new_media)
        query.edit_message_caption(caption=caption, parse_mode=ParseMode.HTML)
        query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(next_prev_but))
def add_photo(update: Update, context):
    user_id = update.effective_chat.id
    stage=get(table="stage", user_id=user_id)['stage']
    data = update.to_dict()

    if stage == "Ortga🔙":
        update.message.reply_text(
            text="Not'og'ri harakat🚧❗️",
            reply_markup=ReplyKeyboardMarkup(users_start_but)
        )
    if stage == "/start":
        update.message.reply_text(
            text="Not'og'ri harakat🚧❗️",
            reply_markup=ReplyKeyboardMarkup(users_start_but)
        )
    else:
        try:
            insert(table=products,data={"file_id": data["message"]['photo'][-1]['file_id'],"text": data['message']['caption'],"type": stage, "media": "photo"})
        except:
            insert(table=products, data={"file_id": data["message"]['photo'][-1]['file_id'],"type": stage, "media": "photo"})
        upd(table="stage", user_id=user_id, data={"pricing": "true"})
        update.message.reply_text(
            text="Ushbu mahsulot narxini kiriting! ...",
            reply_markup=ReplyKeyboardMarkup(add_acces, resize_keyboard=True)
        )
    


def add_video(update: Update, context):
    user_id = update.effective_chat.id
    stage = get(table="stage", user_id=user_id)['stage']
    data = update.to_dict()
    

    if stage == "Ortga🔙":
        update.message.reply_text(
            text="Not'og'ri harakat🚧❗️",
            reply_markup=ReplyKeyboardMarkup(users_start_but)
        )
    if stage == "/start":
        update.message.reply_text(
            text="Not'og'ri harakat🚧❗️",
            reply_markup=ReplyKeyboardMarkup(users_start_but)
        )
    else:
        try:
            insert(table=products,data={"file_id": data["message"]['video']['file_id'],"text": data['message']['caption'],"type": stage, "media": "video"})
            update.message.reply_text(
            text="Ushbu mahsulot narxini kiriting... ",
            reply_markup=ReplyKeyboardMarkup(add_acces, resize_keyboard=True)
        )
        except:
            insert(table=products,data={"file_id": data["message"]['video']['file_id'],"type": stage, "media": "video"})
        update.message.reply_text(
            text="Ushbu mahsulot narxini kiriting... ",
            reply_markup=ReplyKeyboardMarkup(add_acces, resize_keyboard=True)
        )
        upd(table="stage", user_id=user_id, data={"pricing": "true"})

    