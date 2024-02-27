from telegram import InlineKeyboardButton
from settings import *
users_start_but = [
    ["Telefonlar📱", "Telefon jihozlari⚙️"],
    ["Quloqliklar🎧", "Soatlar⌚️"],
    ['Avtomobil jihozlari⚙️',"Ko'proq tovarlar🖇"],
    ["Admin👨🏻‍💻","Zakaz berish","Statistika📊"]
]

boshqa_tovarlar_but = [
    ["Pultlar🕹", "Sichqonchalar🖱"],
    ["Fonarlar🔦","Bataraeykalar🔋"],
    ["Kamyob aksessuarlar💎"],
    ["Ortga🔙"]
]

add_acces = [
    ["Ortga🔙"]

]
inline_keyboard = [
        [InlineKeyboardButton("Guruh❌", url="https://t.me/ishtixon_telefon_aksesuar")],
        [InlineKeyboardButton("Tekshirish✅", callback_data='subscribe')]
]

next_prev_but = [
        [InlineKeyboardButton("⏮", callback_data="prev"), InlineKeyboardButton("⏭", callback_data="next")],
        [InlineKeyboardButton("Rustam aka👤", url=ADMIN)]
        ]  

group_button = [
    [InlineKeyboardButton("Ko'proq tovarlar📦", url="https://t.me/Aksessuarlar_Ishtixon_Bot")]
]