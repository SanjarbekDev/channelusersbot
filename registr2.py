import telebot
from telebot import types

token='1748803780:AAH357m3Klw6hmTa4O0IELRPCIp5eUYn9kw'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def register(message):
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True)
    reg_button = types.KeyboardButton(text="Telefon raqamni yuborish", request_contact=True)
    keyboard.add(reg_button)
    firstName=message.from_user.first_name
    response = bot.send_message(message.chat.id,f"Assalomu aleykum {firstName} botimizga xush kelibsiz ! Botimizga hikoya jo'natishdan oldin raqmingizni yuboring👇👇 ", 
                                reply_markup=keyboard)
    print(response.contact)  # response.contact = None here
@bot.message_handler(content_types=['contact'])
def contact_handler(message):
    print(message.contact.phone_number)
    bot.send_message(message.chat.id,"Raxmat telefon raqami muvoffaqiyatli qabul qilindi , marhamat hikoyani yuborishingiz mumkin ")
@bot.message_handler(content_types=['text'])
def contact_handler(message):
    bot.send_message(message.chat.id,"Ajoyib! \nAdmin javobini kuting")


if __name__ == '__main__':
    bot.polling(none_stop=True)