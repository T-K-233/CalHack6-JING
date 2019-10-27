""" greet_api.py

Generates a greeting message based on time.
"""
import datetime

def getGreet(user_settings):
    current_time = datetime.datetime.now().hour
    if current_time >= 0 and current_time <= 12:
        s = "Good morning, {0}"
    elif current_time > 12 and current_time <= 16:
        s = "Good afternoon, {0}"
    elif current_time > 16 and current_time <= 20:
        s = "Good evening, {0}"
    elif current_time > 20 and current_time < 24:
        s = "Good night, {0}"
    return {
        "text": s.format(user_settings["name"]),
        "voice": s.format(user_settings["name"])
        }
