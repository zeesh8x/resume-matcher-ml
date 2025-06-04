import nltk
import re
from nltk.corpus import stopwords
import spacy

stop_words = set(stopwords.words('english'))
nlp = spacy.load("en_core_web_sm")

def preprocess(text):
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)
    tokens = text.split()
    filtered = [w for w in tokens if w not in stop_words]
    doc = nlp(" ".join(filtered))
    return " ".join(token.lemma_ for token in doc)
