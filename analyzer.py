import sys
from utils.file_reader import extract_text
from utils.text_processor import clean_and_tokenize

def load_keywords(file_path="job_keywords.txt"):
    with open(file_path, "r") as f:
        return [line.strip().lower() for line in f if line.strip()]

def match_keywords(tokens, keywords):
    return [kw for kw in keywords if kw in tokens]

def score_resume(matched, total):
    return round(len(matched) / len(total) * 100, 2)

def main(resume_path):
    print(f"\nAnalyzing: {resume_path}")
    text = extract_text(resume_path)
    tokens = clean_and_tokenize(text)
    keywords = load_keywords()
    matched = match_keywords(tokens, keywords)
    score = score_resume(matched, keywords)

    print("\n🔍 Matched Keywords:", matched)
    print(f"📊 Resume Score: {score}%")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python analyzer.py <resume_file.docx/pdf>")
    else:
        main(sys.argv[1])
