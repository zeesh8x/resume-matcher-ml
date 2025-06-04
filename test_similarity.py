from parser import extract_text_from_pdf
from preprocess import preprocess
from similarity import calculate_similarity

# Extract and preprocess resume
resume_text = extract_text_from_pdf("Untitled document (1).pdf")
clean_resume = preprocess(resume_text)

# Example job description (you can replace this with any JD text)
job_description = """
We are looking for a software engineer skilled in Python, machine learning, and natural language processing.
Experience with NLP libraries and data preprocessing is a plus.
"""

clean_job = preprocess(job_description)

score = calculate_similarity(clean_resume, clean_job)
print(f"Similarity score between resume and job description: {score:.4f}")
