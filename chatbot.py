import nltk
from nltk.chat.util import Chat, reflections
import spacy
from responses import patterns

nlp = spacy.load("en_core_web_sm")

nltk_chatbot = Chat(patterns, reflections)

def analyze_text(text):
    """ Use spaCy to analyze and print parts of speech """
    doc = nlp(text)
    analysis = []
    for token in doc:
        analysis.append(f'{token.text}: {token.pos_}')
    return analysis

def chat():
    print("Hello! I'm here to chat with you. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['bye', 'goodbye', 'see you', 'later']:
            print("Chatbot: Goodbye! Have a great day!")
            break

        response = nltk_chatbot.respond(user_input)
        if response == 'Sorry, I do not understand that. Can you please rephrase?':
            analysis = analyze_text(user_input)
            response = "I couldn't find a response, but here's an analysis of your message:\n" + "\n".join(analysis)

        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chat()
