import argparse
from parser import extract_text_from_pdf
from preprocess import preprocess
from similarity import calculate_similarity
from keyword_matcher import keyword_match

def main(resume_path, job_desc_path):
    # Extract & preprocess resume
    resume_text = extract_text_from_pdf(resume_path)
    clean_resume = preprocess(resume_text)

    # Load and preprocess job description
    with open(job_desc_path, 'r', encoding='utf-8') as f:
        job_desc = f.read()
    clean_job = preprocess(job_desc)

    # Calculate similarity
    score = calculate_similarity(clean_resume, clean_job)
    print("\n📊 SIMILARITY SCORE")
    print("=" * 30)
    print(f"Match Score: {score * 100:.2f}%")
    # Keyword feedback
    matched, missing = keyword_match(resume_text, job_desc)
    print("\n🔍 Keyword Match Report:")
    print("="*30)
    print("✅ Matched Keywords:\n", ", ".join(matched) if matched else "None")
    print("\n❌ Missing Keywords:\n", ", ".join(missing) if missing else "None")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Resume Matcher CLI")
    parser.add_argument("resume", help="Path to the resume PDF file")
    parser.add_argument("jobdesc", help="Path to the job description text file")

    args = parser.parse_args()
    main(args.resume, args.jobdesc)
