""" run.py

The entrance point
"""
import datetime
import time

from flask import Flask, render_template, make_response
import pyaudio

import tts_api
import calendar_api
import weather_api
import one_line_a_day_api
import greet_api

import requests



# ------------

user_settings = {
    "name": "Mr. Denero",
    "habits": ["Do exercise", "Apply Sunscreen", "Prepare lunch sandwich"],
    }

app = Flask(__name__)

data = {}

@app.route("/")
def modify():
    global user_settings
    return render_template("modify.html", user_settings=user_settings)
    
@app.route("/landingpage")
def landingPage():
    global data
    data = {}
    # generate greet message based on time
    
    data["greet"] = greet_api.getGreet(user_settings)
    data["one_line_a_day"] = one_line_a_day_api.getOneLineADay()
    
    data["weather"] = weather_api.getWeather()
    data["calendar"] = calendar_api.getCalendar()
    data["habits"] = user_settings["habits"]
    
    return render_template("index.html", data=data)

@app.route("/voice")
def voicePage():
    global data
    debug = False
    if not debug:
        voice_string = data["greet"]["voice"] +"\n"+ data["weather"]["voice"] +"\n"+ data["calendar"]["voice"]
        byte_stream = tts_api.textToSpeech(data["greet"]["voice"])
        byte_stream += b"\x00" * 10240
        byte_stream += tts_api.textToSpeech(data["weather"]["voice"])
        byte_stream += b"\x00" * 10240
        byte_stream += tts_api.textToSpeech(data["calendar"]["voice"])
        p = pyaudio.PyAudio()
        stream = p.open(format=pyaudio.paInt16,
            channels=2,
            rate=12000,
            output=True,
            frames_per_buffer=1024)
        stream.write(byte_stream)
    return ""


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
