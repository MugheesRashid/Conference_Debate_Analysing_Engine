import string
import re
import pandas as pd
from loader import load_data

STOPWORDS = {
    "the", "is", "in", "and", "to", "of", "a", "for",
    "on", "with", "that", "this", "it", "as", "are",
    "be", "by", "an", "we", "must"
}

def clean_text(debate):

    if not isinstance(debate, str):
        return ""
    
    debate = debate.lower()

    debate = debate.translate(str.maketrans("", "", string.punctuation))
    debate = re.sub(r"\s+", " ", debate).strip()
    
    clean_text = []
    for word in debate.split():
        if word not in STOPWORDS:
            clean_text.append(word)
    

    return " ".join(clean_text)
    

def preprocess_dataframe(df):

    # Apply clean_text function to every speech
    df["clean_speech"] = df["Speech_Text"].apply(clean_text)

    return df
