from parser import extract_text_from_pdf
from preprocess import preprocess

text = extract_text_from_pdf("Untitled document (1).pdf")
clean_text = preprocess(text)

print(clean_text[:500])  # show first 500 cleaned characters
