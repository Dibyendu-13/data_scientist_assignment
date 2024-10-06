import os

class Config:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    PDF_DIR = os.path.join(os.path.dirname(BASE_DIR), 'sample_pdfs')
    EXTRACTED_TEXT_DIR = os.path.join(os.path.dirname(BASE_DIR), 'data', 'extracted_texts')

    @staticmethod
    def ensure_directories():
        if not os.path.exists(Config.EXTRACTED_TEXT_DIR):
            os.makedirs(Config.EXTRACTED_TEXT_DIR)
