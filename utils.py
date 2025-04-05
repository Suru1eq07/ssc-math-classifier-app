import re

def clean_text(text):
    """
    Cleans the input text by removing special characters and converting to lowercase.
    """
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)  # remove punctuation
    text = text.lower()  # convert to lowercase
    return text
