import re
import pdfplumber
from nltk.tokenize import TreebankWordTokenizer

tokenizer = TreebankWordTokenizer()

def extract_text_from_pdf(pdf_path):
    text = ''
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + '\n'
    return text

def extract_text_from_txt(txt_path):
    with open(txt_path, 'r', encoding='utf-8') as f:
        return f.read()

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', ' ', text)
    tokens = tokenizer.tokenize(text)  # NO punkt needed
    return ' '.join(tokens)
