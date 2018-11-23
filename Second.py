# -*- coding: utf-8 -*-
import config
import telebot

bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    mes1 = message.text*2 + ' твой ответ'
    bot.send_message(message.chat.id, mes1)

if __name__ == '__main__':
     bot.polling(none_stop=True)
