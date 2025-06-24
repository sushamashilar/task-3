import nltk
from nltk.tokenize import word_tokenize

# Download the tokenizer if not already downloaded
nltk.download('punkt')

def preprocess(text):
    # Tokenize input text
    tokens = word_tokenize(text)
    return tokens

def generate_response(tokens):
    tokens = [t.lower() for t in tokens]  # convert tokens to lowercase

    if 'hello' in tokens or 'hi' in tokens:
        return "Hello! How can I help you today?"
    elif 'how' in tokens and 'you' in tokens:
        return "I'm a bot, so I don't have feelings, but thanks for asking!"
    elif 'bye' in tokens or 'quit' in tokens or 'exit' in tokens:
        return "Goodbye! Have a nice day."
    else:
        return "Sorry, I don't understand that yet."

def chatbot():
    print("Chatbot: Hello! Type 'quit' or 'exit' to exit.")
    while True:
        inp = input("You: ")
        if inp.lower() in ['quit', 'exit']:
            print("Chatbot: Bye!")
            break
        tokens = preprocess(inp)
        response = generate_response(tokens)
        print("Chatbot:", response)

if __name__ == "__main__":
    chatbot()
