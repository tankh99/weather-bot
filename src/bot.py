import telebot
import os
import constants
import markup

TOKEN = "1917294311:AAFQ6125bJSZ_sr4ZiptzHfOCVhNuF6noe8"
bot = telebot.TeleBot(TOKEN)


@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    if call.data == constants.START:
        edit_message("Checking weather for you...", call.message)
        
    if call.data == constants.EXIT:
        edit_message("Goodbye", call.message)

    bot.answer_callback_query(call.id)


def edit_message(text, message, reply_markup=None):
    if message.text != text:
        bot.edit_message_text(
            chat_id=message.chat.id,
            text=text,
            message_id=message.id,
            reply_markup=reply_markup
        )
    else:
        print("No change in edited text")
        

@bot.message_handler(commands=["start"])
def handle_start(message):
    bot.send_message(
        message.chat.id,
        "Welcome to Weather Bot",
        reply_markup=markup.gen_start_markup()
    )


bot.polling()