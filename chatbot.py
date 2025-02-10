import json
import random

with open("intents.json", "r") as file:
    intents = json.load(file)

def chatbot_response(user_input):
    for intent in intents["intents"]:
        for pattern in intent["patterns"]:
            if user_input.lower() in pattern.lower():
                return random.choice(intent["responses"])
    return "I'm sorry, I don't understand."

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        print("Bot:", chatbot_response(user_input))
