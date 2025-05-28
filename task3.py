#pip install nltk
#import nltk
#nltk.download('punlt')
import nltk
from nltk.tokenize import word_tokenize
import random
intents = {
    'greeting': {'keywords': ['hello', 'hi', 'hey', 'greetings'], 'responses': ['Hello!', 'Hi there!', 'Hey! How can I help you?']},
    'goodbye': {'keywords': ['bye', 'goodbye', 'see you', 'exit', 'quit'], 'responses': ['Goodbye!', 'See you later!', 'Have a nice day!']},
    'thanks': {'keywords': ['thanks', 'thank you', 'thx'], 'responses': ["You're welcome!", 'No problem!', 'Anytime!']},
    'hours': {'keywords': ['hours', 'open', 'close', 'timing'], 'responses': ['We are open from 9 AM to 5 PM, Monday to Friday.']},
    'name': {'keywords': ['your name', 'who are you'], 'responses': ['I am a simple chatbot built with NLTK.']}
}

def chatbot():
    print("Chatbot: Hello! Type 'exit' to quit.")
    while True:
        user_input = input("You: ").lower()
        if user_input in ['exit', 'quit', 'bye']:
            print("Chatbot: Goodbye! Have a great day!")
            break
        tokens = word_tokenize(user_input)
        intent = next((intent for intent, data in intents.items() 
                       if any(k in user_input or k in tokens for k in data['keywords'])), None)
        if intent:
            print("Chatbot:", random.choice(intents[intent]['responses']))
        else:
            print("Chatbot: Sorry, I didn't understand that. Can you rephrase?")

if __name__ == "__main__":
    chatbot()
