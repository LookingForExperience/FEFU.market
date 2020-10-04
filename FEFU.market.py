import telebot

from string import Template
from telebot import types

bot = telebot.TeleBot("831712665:AAHb3tp5Jl0XveNi_DuPeqXKM68yKB0dL8c")

user_dict = {}

class User:
    def __init__ (self, city):
        self.city = city

        keys = ['order']

        for key in keys:
            self.key = None

def funcZakaz (message):
    chat_id = message.chat.id
    user_dict[chat_id] = User(message.text)

    back = types.KeyboardButton("Вернуться в главное меню")
    backMarkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    backMarkup.add(back)

    msg = bot.send_message (chat_id, "Напишите список товаров.", reply_markup=backMarkup)
    bot.register_next_step_handler(msg, finalZakaz)

def finalZakaz (message):

    chat_id = message.chat.id
    user_dict[chat_id] = User(message.text)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    zakaz = types.KeyboardButton("Заказать товары")
    support = types.KeyboardButton("Контакты разработчиков")

    markup.add(zakaz, support)

    back = types.KeyboardButton("Вернуться в главное меню")
    backMarkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    backMarkup.add(back)

    if message.text == "Вернуться в главное меню":
        msg = bot.send_message (chat_id, "Вы вернулись в главное меню.", reply_markup=markup)
        bot.register_next_step_handler(msg, mainText)

    else:
        msg = bot.send_message (chat_id, "Спасибо за заказ, ожидайте сообщения от курьера!", reply_markup=markup)
        bot.register_next_step_handler(msg, mainText)
    


@bot.message_handler (content_types = ["text"])
def mainText (message):
    if message.chat.type == 'private':

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        zakaz = types.KeyboardButton("Заказать товары")
        support = types.KeyboardButton("Контакты разработчиков")

        markup.add(zakaz, support)

        if message.text.lower() == 'привет':
            bot.send_message(message.chat.id, "Привет, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный для заказов товаров с материка на кампус ДВФУ!".format(message.from_user, bot.get_me()),
                parse_mode='html', reply_markup=markup)

        categoryMarkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        food = types.KeyboardButton("Продукты питания")
        householdChemicals = types.KeyboardButton("Бытовая химия")
        computerTech = types.KeyboardButton("Компьютерная техника")
        back = types.KeyboardButton("Вернуться в главное меню")

        categoryMarkup.add(food, householdChemicals, computerTech, back)

        backMarkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        
        backMarkup.add(back)

        if message.text == 'Заказать товары':

            bot.send_message(message.chat.id, "Выберите категорию товаров.", reply_markup=categoryMarkup)
            bot.register_next_step_handler(message, funcZakaz)
        
        elif message.text == 'Продукты питания':
            
            bot.register_next_step_handler(message, funcZakaz)

        elif message.text == 'Бытовая химия':

            bot.send_message(message.chat.id, "Напишите список товаров.", reply_markup=backMarkup)

        elif message.text == 'Компьютерная техника':

            bot.send_message(message.chat.id, "Напишите список товаров.", reply_markup=backMarkup)

        elif message.text == 'Вернуться в главное меню':
            
            bot.send_message(message.chat.id, "Вы вернулись в главное меню.", reply_markup=markup)
            
        elif message.text == 'Контакты разработчиков':

            bot.send_message(message.chat.id, "Если возникли вопросы, можете обращаться к нам! \n\n☆   Автор бота Семён - semen.skopin@gmail.com \n☆   Илюха - padkur1234@gmail.com")

        
        # else:
        #     bot.send_message(message.chat.id, "Такой команды не существует ☹")

bot.enable_save_next_step_handlers(delay=2)
bot.load_next_step_handlers()

if __name__ == '__main__':
    bot.polling(none_stop=True)