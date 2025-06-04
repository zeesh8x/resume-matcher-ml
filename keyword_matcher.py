import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter

stop_words = set(stopwords.words('english'))

def extract_keywords(text, top_n=15):
    words = word_tokenize(text.lower())
    words = [w for w in words if w.isalpha() and w not in stop_words]
    return [w for w, _ in Counter(words).most_common(top_n)]

def keyword_match(resume_text, job_desc_text):
    resume_keywords = extract_keywords(resume_text)
    job_keywords = extract_keywords(job_desc_text)

    matched = [kw for kw in job_keywords if kw in resume_keywords]
    missing = [kw for kw in job_keywords if kw not in resume_keywords]

    return matched, missing
