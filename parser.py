import fitz  # PyMuPDF

def extract_text_from_pdf(file):
    """Extract all text from a PDF file uploaded via Streamlit."""
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text
