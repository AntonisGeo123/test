from telebot import types

menu_btn = types.ReplyKeyboardMarkup()
btn_1 = types.KeyboardButton(text='/help')
btn_2 = types.KeyboardButton(text='/thanks')
menu_btn.add(btn_1, btn_2)














