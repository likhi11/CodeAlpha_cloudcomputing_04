import json
import random

with open("data/intents.json") as f:
    intents = json.load(f)

def get_response(user_input):
    for intent in intents["intents"]:
        for pattern in intent["patterns"]:
            if pattern.lower() in user_input.lower():
                return random.choice(intent["responses"])
    return "Sorry, I didn't understand that."
