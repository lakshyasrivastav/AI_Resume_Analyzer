import PyPDF2
from docx import Document

def extract_text(file_path):
    if file_path.endswith(".docx"):
        doc = Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs])
    elif file_path.endswith(".pdf"):
        with open(file_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            return "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
    else:
        raise ValueError("Unsupported file type. Use .docx or .pdf")
