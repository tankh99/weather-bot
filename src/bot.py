import telebot
import os
import constants
import markup
import json
import weatherapi
from PIL import Image
import requests
from locations import locations


TOKEN = "1917294311:AAFQ6125bJSZ_sr4ZiptzHfOCVhNuF6noe8"
bot = telebot.TeleBot(TOKEN)

# locations_json = open("src/locations.json")
# locations = json.load(locations_json)

@bot.message_handler(func=lambda message: message.text.lower().capitalize() in locations)
def handle_location(message):
    location = [s for s in locations if message.text.lower() == s.lower()][0]
    print(location)
    weather_data = weatherapi.get_weather(message.text)
    icon_url = weather_data["current"]["condition"]["icon"]
    icon_url = f"http:{icon_url}"
    icon = Image.open(requests.get(icon_url, stream=True).raw)

    weather_stats = (
        f'<b>{location}</b>\n'
        f'<b>Condition:</b> {weather_data["current"]["condition"]["text"]}\n'
        f'<b>Temperature</b> {weather_data["current"]["temp_c"]}°C\n'
        f'<b>Wind Speed</b> {weather_data["current"]["wind_kph"]}km/h\n'
        f'<b>Humidity:</b> {weather_data["current"]["humidity"]}'
    )
    bot.send_photo(
        message.chat.id,
        icon,
        weather_stats,
        parse_mode="HTML"
    )

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
        "Welcome to Weather Bot. Type in the area you want to check on",
        reply_markup=markup.gen_start_markup()
    )


bot.polling()