import pytesseract
from PyPDF2 import PdfReader
from PIL import Image
import fitz  # PyMuPDF for working with digital PDFs

def extract_text(file_path):
    text = ""
    # Extract text for digital PDFs
    if file_path.endswith('.pdf'):
        reader = PdfReader(file_path)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    # Extract text for scanned PDFs
    elif file_path.endswith('.png') or file_path.endswith('.jpg'):
        img = Image.open(file_path)
        text = pytesseract.image_to_string(img)
    else:
        raise ValueError("Unsupported file format.")
    
    return text
