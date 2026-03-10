from PyPDF2 import PdfReader
import docx
import os
import logging

logger = logging.getLogger(__name__)

def extract_text_from_pdf(filepath: str) -> str:
    """Extract standard text from a PDF file."""
    try:
        reader = PdfReader(filepath)
        text = ''
        for page in reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + '\n'
        return text
    except Exception as e:
        logger.error(f"Error parsing PDF {filepath}: {str(e)}")
        raise

def extract_text_from_docx(filepath: str) -> str:
    """Extract text from a DOCX file."""
    try:
        doc = docx.Document(filepath)
        text = ''
        for para in doc.paragraphs:
            text += para.text + '\n'
        return text
    except Exception as e:
        logger.error(f"Error parsing DOCX {filepath}: {str(e)}")
        raise

def extract_text(filepath: str) -> str:
    """
    Factory wrapper to extract text based on extension.
    """
    ext = os.path.splitext(filepath)[1].lower()
    
    if ext == '.pdf':
        return extract_text_from_pdf(filepath)
    elif ext in ['.docx', '.doc']:
        # Note: python-docx only supports .docx, .doc might fail natively
        # we strictly validate for docx at upload
        return extract_text_from_docx(filepath)
    else:
        raise ValueError(f"Unsupported file format: {ext}")
