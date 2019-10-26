from io import StringIO
import datetime
import time

from flask import Flask, render_template, make_response, g

import tts
import calendar_api

# ------------

import threading
import json

import requests
from playsound import playsound

def fetchWeather(use_realtime=False):
    if use_realtime:
        res = requests.get("https://api.darksky.net/forecast/68b57c294028ea3886af9e58b329b435/37.8715,-122.2730")
        data = json.loads(res.text)
        json.dump(data, open("data.json", "w", encoding="utf-8"))
    else:
        data = json.load(open("data.json", encoding="utf-8"))
    data = {
        "temperatureMin": int(data["daily"]["data"][0]["temperatureMin"]),
        "temperatureMax": int(data["daily"]["data"][0]["temperatureMax"]),
        "text": data["daily"]["data"][0]["summary"]
        }
    data["voice"] = "Today's weather is {0}. Maximum temperature's around {1}Fahrenheit.".format(data["text"], data["temperatureMax"])
    return data

def fetchCalendar():
    data = calendar_api.getCalendar()
    dtime = datetime.datetime.strptime(data[0]["start"]["dateTime"], "%Y-%m-%dT%H:%M:%S%z")
    if dtime.day == datetime.datetime.now().day:
        formats = "today at %H:%M"
    else:
        raise NotImplementedError
    
    data = {
        "voice": "you have {0} {1}".format(data[0]["summary"], dtime.strftime(formats)),
        "text": "111",
        }
    return data

def generateVoice(text):
    voic = tts.textToSpeech(text)
    
    return voic
# ------------

user_settings = {
    "name": "Pei hang"
    }

app = Flask(__name__)

data = {}

@app.route('/')
def homePage():
    global data
    data = {}
    data["greet"] = {
        "voice": "Good morning, {0}".format(user_settings["name"]),
        "text": "Good morning, {0}".format(user_settings["name"])
        }
    data["weather"] = fetchWeather()
    data["calendar"] = fetchCalendar()
    
    return render_template("index.html", data=data)

@app.route('/voice')
def voicePage():
    global data
    debug = False
    if not debug:
        voice_string = data["greet"]["voice"] +"\n"+ data["weather"]["voice"] +"\n"+ data["calendar"]["voice"]
        print(voice_string)
        voic = b""
        voic += generateVoice(data["greet"]["voice"])
        print(voic)
        voic += b"\x00"*1
        voic += generateVoice(data["weather"]["voice"])
        
        with open("tmp/output.mp3", "wb") as out:
            out.write(voic)
            print("Audio content written to file 'tmp/output.mp3'")
        playsound("tmp/output.mp3")
        return ""
        time.sleep(1)
        
        time.sleep(1)
        generateVoice(data["calendar"]["voice"])
        time.sleep(1)
    return ""


if __name__ == "__main__":
    app.run(port=80, debug=True)
