import random
import re
import json
from datetime import datetime

class ChatbotGenerator:
    def __init__(self, name="Chatbot", knowledge_base=None):  # fixed __init__
        self.name = name
        self.knowledge_base = knowledge_base or self.default_knowledge()
        self.memory = []
        self.context = {}

    def default_knowledge(self):
        return {
            "greetings": {
                "patterns": ["hi", "hello", "hey", "greetings"],
                "responses": ["Hello! How can I help you?", "Hi there!", "Greetings!"]
            },
            "farewells": {
                "patterns": ["bye", "goodbye", "see you"],
                "responses": ["Goodbye!", "See you later!", "Have a nice day!"]
            },
            "thanks": {
                "patterns": ["thanks", "thank you", "appreciate it"],
                "responses": ["You're welcome!", "My pleasure!", "No problem!"]
            }
        }

    def add_knowledge(self, intent, patterns, responses):
        if intent not in self.knowledge_base:
            self.knowledge_base[intent] = {"patterns": [], "responses": []}
        self.knowledge_base[intent]["patterns"].extend(patterns)
        self.knowledge_base[intent]["responses"].extend(responses)

    def save_knowledge(self, filename="chatbot_knowledge.json"):
        with open(filename, 'w') as f:
            json.dump(self.knowledge_base, f, indent=2)

    def load_knowledge(self, filename="chatbot_knowledge.json"):
        try:
            with open(filename) as f:
                self.knowledge_base = json.load(f)
            return True
        except FileNotFoundError:
            return False

    def preprocess(self, text):
        text = text.lower().strip()
        text = re.sub(r'[^\w\s]', '', text)
        return text

    def match_intent(self, text):
        processed = self.preprocess(text)
        best_match = None
        best_score = 0
        for intent, data in self.knowledge_base.items():
            for pattern in data["patterns"]:
                if re.search(r'\b' + re.escape(pattern) + r'\b', processed):
                    score = len(pattern.split())
                    if score > best_score:
                        best_match = intent
                        best_score = score
        return best_match

    def generate_response(self, user_input):
        self.memory.append({
            "user": user_input,
            "time": datetime.now().isoformat()
        })
        intent = self.match_intent(user_input)
        if intent:
            responses = self.knowledge_base[intent]["responses"]
            return random.choice(responses)
        else:
            return "I'm not sure how to respond to that. Can you rephrase?"

    def chat(self):
        print(f"{self.name}: Hi! I'm {self.name}. How can I help you? (Type 'quit' to exit)")
        while True:
            user_input = input("You: ")
            if user_input.lower() == 'quit':
                print(f"{self.name}: Goodbye!")
                break
            response = self.generate_response(user_input)
            print(f"{self.name}: {response}")

# Example usage
if __name__ == "__main__":  # fixed __name__
    bot = ChatbotGenerator("Echo")
    custom_intents = {
        "weather": {
            "patterns": ["weather", "forecast", "raining", "sunny"],
            "responses": ["I don't have weather data right now.", "You might want to check a weather app."]
        },
        "name": {
            "patterns": ["your name", "who are you"],
            "responses": ["I'm Echo!", "People call me Echo."]
        }
    }
    for intent, data in custom_intents.items():
        bot.add_knowledge(intent, data["patterns"], data["responses"])
    bot.chat()
