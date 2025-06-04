from parser import extract_text_from_pdf

text = extract_text_from_pdf("Untitled document (1).pdf")
print(text[:1000])  # print first 1000 characters of the resume
