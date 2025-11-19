from pypdf import PdfReader
from bs4 import BeautifulSoup
import re

def extract_pdf(path: str) -> str:
    """
    Extract text from a PDF file.
    """
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return clean_text(text)


def extract_html(path: str) -> str:
    """
    Extract text from an HTML file.
    """
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text(separator='\n')
    return clean_text(text)

def clean_text(text: str) -> str:
    """
    Clean extracted text by removing extra whitespace and non-printable characters.
    """
    text = re.sub(r"\s+", " ", text)
    text = text.strip()
    return text.strip()