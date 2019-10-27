""" one_line_a_day_api.py

Generates a infamous saying by pure randomness and luck.
"""
import random

def getOneLineADay():
    data = ["Push yourself because no one else is going to do it for you", "Don't stop until you're proud", "Get up. Clean your desk. Tie your hair. And just start.", "Discipline is choosing between what you want now and what you want most", "Everything in the world may be endured except continual prosperity."]
    s = data[random.randint(0, len(data)-1)]
    return {
            "voice": s,
            "text": s
            }
