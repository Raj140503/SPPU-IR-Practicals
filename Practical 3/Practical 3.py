# Practical 3 - Write a program for Pre-processing of a Text Document: stop word removal


import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')
nltk.download('punkt')

def preprocess_text(text):
    words = word_tokenize(text)
    
    words = [word.lower() for word in words]
    
    stop_words = set(stopwords.words('english'))
    
    filtered_words = [word for word in words if word.isalnum() and word not in stop_words]
    
    return filtered_words

text = """
Natural Language Processing (NLP) is a field of artificial intelligence that deals with the interaction between computers and humans using natural language. 
The ultimate objective of NLP is to read, decipher, understand, and make sense of human language in a valuable way.
"""

processed_text = preprocess_text(text)

print("Original Text:", text)
print("\nProcessed Text (after stop word removal):", processed_text)

#INPUT
# Jane Austen’s Pride and Prejudice is an 18th-century novel of manners set in rural.

# OUTPUT
# Jane Austen’s Pride Prejudice 18th-century novel manners set rural England.