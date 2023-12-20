import requests
import datetime
import time


while True:

    url = "https://api.openweathermap.org/data/2.5/weather?q=Moscow&appid=368e827be4b38db51ff960ca88b5c396"
    req = round((requests.get(url).json()["main"]["temp"]) -274)
    now_time = datetime.datetime.now().strftime("%y.%m.%d")
    
    bot_token = "6628818385:AAHAYls8JmByYGIRsCe7ZlGDa7bZnY3ElwM"
    user =  '881596032'
    response = requests.get(f'https://api.telegram.org/bot{bot_token}/sendMessage', params={'chat_id': user, 'text': f'[{now_time}] В Москве сейчас - {req} °'}) 
    time.sleep(3600)

