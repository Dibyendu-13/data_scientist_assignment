import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    """Extract text from a digital PDF."""
    with fitz.open(pdf_path) as pdf_doc:
        text = ""
        for page in pdf_doc:
            text += page.get_text("text")
    return text
