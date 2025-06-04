import os
from parser import extract_text_from_pdf
from preprocess import preprocess
from similarity import calculate_similarity

def batch_process(resume_folder, job_desc_path):
    # Load and preprocess job description
    with open(job_desc_path, 'r', encoding='utf-8') as f:
        job_desc = f.read()
    clean_job = preprocess(job_desc)

    results = []

    for filename in os.listdir(resume_folder):
        if filename.lower().endswith('.pdf'):
            filepath = os.path.join(resume_folder, filename)
            try:
                resume_text = extract_text_from_pdf(filepath)
                clean_resume = preprocess(resume_text)
                score = calculate_similarity(clean_resume, clean_job)
                results.append((filename, score))
                print(f"Processed {filename} - Score: {score:.4f}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

    # Sort results by score descending
    results.sort(key=lambda x: x[1], reverse=True)

    print("\nRanking of resumes:")
    for rank, (filename, score) in enumerate(results, start=1):
        print(f"{rank}. {filename}: {score:.4f}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Batch Resume Matcher")
    parser.add_argument("resume_folder", help="Path to folder containing resume PDFs")
    parser.add_argument("jobdesc", help="Path to the job description text file")
    args = parser.parse_args()

    batch_process(args.resume_folder, args.jobdesc)
