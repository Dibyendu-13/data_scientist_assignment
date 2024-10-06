import os
from src.pdf_extraction import extract_text_from_pdf
from src.ocr_extraction import extract_text_from_scanned_pdf
from src.config import Config

def preprocess_pdfs(pdf_dir, output_dir):
    """ Preprocess PDFs from multiple language folders (bn, ur, en, zh). """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Language folders in the sample_pdfs directory
    language_folders = ['bn', 'ur', 'en', 'zh']

    for lang_folder in language_folders:
        lang_output_dir = os.path.join(output_dir, lang_folder)
        if not os.path.exists(lang_output_dir):
            os.makedirs(lang_output_dir)

        lang_pdf_dir = os.path.join(pdf_dir, lang_folder)
        
        # Get all PDF files in the current language folder
        pdf_files = [f for f in os.listdir(lang_pdf_dir) if f.endswith(".pdf")]
        for pdf_file in pdf_files:
            pdf_path = os.path.join(lang_pdf_dir, pdf_file)
            print(f"Processing {pdf_file} from {lang_folder} folder...")

            # Try extracting text using PDF parser
            try:
                extracted_text = extract_text_from_pdf(pdf_path)
            except Exception as e:
                print(f"Standard extraction failed for {pdf_file}, trying OCR... {e}")
                extracted_text = extract_text_from_scanned_pdf(pdf_path)

            # Save extracted text to output directory
            output_file = os.path.join(lang_output_dir, pdf_file.replace('.pdf', '.txt'))
            with open(output_file, 'w') as f:
                f.write(extracted_text)

            print(f"Saved extracted text for {pdf_file} to {output_file}")

def main():
    # Ensure directories exist
    Config.ensure_directories()

    # Preprocess PDFs
    preprocess_pdfs(Config.PDF_DIR, Config.EXTRACTED_TEXT_DIR)

if __name__ == "__main__":
    main()
