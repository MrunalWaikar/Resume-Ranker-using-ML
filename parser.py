# parser/parser.py
import fitz  # PyMuPDF

def extract_text_from_pdf(uploaded_file) -> str:
    """
    Extract raw text from a PDF file.

    Args:
        uploaded_file: File-like object (e.g., open('resume.pdf','rb'))

    Returns:
        str: Concatenated text content from all pages.
    """
    text = ""
    file_bytes = uploaded_file.read()   # read bytes
    with fitz.open(stream=file_bytes, filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text.strip()
