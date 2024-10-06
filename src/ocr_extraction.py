import pytesseract
import cv2
import fitz  # PyMuPDF for extracting images

def extract_text_from_scanned_pdf(pdf_path):
    """Extract text from a scanned PDF using OCR."""
    with fitz.open(pdf_path) as pdf_doc:
        ocr_text = ""
        for page_num in range(len(pdf_doc)):
            image_list = pdf_doc[page_num].get_images(full=True)
            for img in image_list:
                xref = img[0]
                base_image = pdf_doc.extract_image(xref)
                image_bytes = base_image["image"]
                image_ext = base_image["ext"]
                # Save image temporarily
                img_path = f"temp_image.{image_ext}"
                with open(img_path, "wb") as img_file:
                    img_file.write(image_bytes)

                # Perform OCR on image
                img_cv = cv2.imread(img_path)
                gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
                ocr_text += pytesseract.image_to_string(gray)

    return ocr_text
