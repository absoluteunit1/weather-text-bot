import os
import json
import requests
import datetime
import math
from twilio.rest import Client


tomorrow = datetime.date.today() + datetime.timedelta(days=1)
morning = str(tomorrow) + ' ' + '09:00:00'
afternoon = str(tomorrow) + ' ' + '15:00:00'

weather = (requests.get("http://api.openweathermap.org/data/2.5/forecast?id=6167865&appid=42a29880805143bfa0de8c337535b4c2&units=metric")).json()

# forecast = [temp, wind_speed, description]

def forecast(obj, time):
    temp = 0
    wind_speed = 0
    description = ''
    humidity = 0
    for item in obj['list']:
        if item['dt_txt'] == time:
            temp = item['main']['temp']
            wind_speed = item['wind']['speed']
            description = item['weather'][0]['description']
            humidity = item['main']['humidity']
    return [temp, wind_speed, description, humidity]
def textMeThis(obj):
    account_sid = os.environ["TWILIO_SID"]
    auth_token = os.environ["TWILIO_AUTH"]
    client = Client(account_sid, auth_token)
    client.messages.create(
        to=os.environ["MY_NUMBER"],
        from_=os.environ["TWILIO_NUMBER"],
        body= obj
        )

T1 = forecast(weather, morning)
temp = str(math.ceil(T1[0])) + '°C'
wind_speed = str(math.ceil(T1[1])*3.6) + 'km/h'
description = T1[2]

msg = 'Weather at 9am tomorrow will be: ' + temp + ' ' + wind_speed + ' with ' + description

print(msg)


