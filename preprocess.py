import nltk
import re
from nltk.corpus import stopwords
import spacy
from spacy.cli import download as spacy_download

# Ensure NLTK stopwords are available
try:
    stop_words = set(stopwords.words('english'))
except LookupError:
    nltk.download('stopwords')
    stop_words = set(stopwords.words('english'))

# Load or download spaCy model
def load_spacy_model():
    try:
        return spacy.load("en_core_web_sm")
    except OSError:
        print("Downloading en_core_web_sm model...")
        spacy_download("en_core_web_sm")
        return spacy.load("en_core_web_sm")

nlp = load_spacy_model()

def preprocess(text):
    # Lowercase and remove non-alphabetic characters
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)

    # Tokenize and remove stopwords
    tokens = text.split()
    filtered = [word for word in tokens if word not in stop_words]

    # Lemmatize with SpaCy
    doc = nlp(" ".join(filtered))
    lemmatized = [token.lemma_ for token in doc]

    return " ".join(lemmatized)