import nltk
from nltk.tokenize.punkt import PunktSentenceTokenizer

# Download 'punkt' tokenizer models (run once)
nltk.download('punkt')

text = "Hello world. This is a test."

# Initialize the tokenizer
tokenizer = PunktSentenceTokenizer()

# Tokenize the text into sentences
sentences = tokenizer.tokenize(text)

print(sentences)
