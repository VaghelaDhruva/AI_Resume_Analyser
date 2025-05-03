# import pdfplumber

# def extract_text_from_pdf(uploaded_file):
#     with pdfplumber.open(uploaded_file) as pdf:
#         text = ''
#         for page in pdf.pages:
#             text += page.extract_text() or ''
#     return text

import pdfplumber

def extract_text_from_pdf(file):
    text = ''
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ''
    return text.strip()