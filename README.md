#  AI Resume Analyzer

**AI Resume Analyzer** is a smart web application built using Python and Streamlit that analyzes resumes in PDF format and provides personalized feedback based on industry-standard expectations. It evaluates your resume's structure, content, keywords, and more — all powered by Natural Language Processing (NLP).

---

##  Features

-  Upload resume in **PDF format**
-  Uses NLP (via spaCy) to extract key information
-  Generates a **resume score (out of 10)**
-  Provides **AI-generated suggestions** for improvement
-  Beautiful and clean **web interface** (Streamlit-based)
-  Modular code: clean separation of extraction, NLP parsing, scoring, and UI

---

##  Tech Stack

| Tool/Library   | Purpose                             |
|----------------|-------------------------------------|
| Python         | Core Programming Language           |
| Streamlit      | Web App Interface                   |
| spaCy (`en_core_web_sm`) | NLP model for entity extraction |
| pdfplumber     | Extract text from PDF resumes       |
| Base64         | Handle resume download              |

---

##  How It Works

1. **Upload a PDF Resume**
2. The app:
   - Extracts text using `pdfplumber`
   - Uses `spaCy` NLP model to extract structured information (skills, experience, education, etc.)
   - Scores the resume using customizable rules (e.g., presence of email, skills, projects)
   - Generates improvement feedback

---

## Installation & Usage

### Prerequisites
Make Python (3.8 or higher) is installed.

### Install Dependencies
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm


