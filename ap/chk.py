import re
def clean_text(text):
    # Remove special characters and split text into words
    text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)
    words = list(text.lower().split())
    return set(words)


"""import string   
def clean_text(text_data):  
    # Appending non punctuated words 
    punctuation ="".join([t for t in text_data if t not in string.punctuation])   
    return set(list(punctuation.lower().split(' ')))
  
# Passing input to the function """

