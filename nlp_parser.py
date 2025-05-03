# import spacy

# nlp = spacy.load("en_core_web_sm")

# def extract_entities(text):
#     doc = nlp(text)
#     entities = {"education": [], "experience": [], "skills": []}
    
#     for ent in doc.ents:
#         if ent.label_ == "ORG":
#             entities["education"].append(ent.text)
#         elif ent.label_ in ["DATE", "TIME"]:
#             entities["experience"].append(ent.text)
    
#     # Basic keyword match for skills
#     skills_list = ["Python", "C++", "SQL", "Machine Learning"]
#     for skill in skills_list:
#         if skill.lower() in text.lower():
#             entities["skills"].append(skill)
#     return entities


import spacy

nlp = spacy.load("en_core_web_sm")

def extract_entities(text):
    doc = nlp(text)
    entities = {
        "name": None,
        "email": None,
        "phone": None,
        "skills": [],
        "education": [],
        "experience": [],
        "projects": [],
        "certifications": []
    }

    for ent in doc.ents:
        if ent.label_ == "PERSON" and not entities["name"]:
            entities["name"] = ent.text
        elif ent.label_ == "ORG":
            entities["experience"].append(ent.text)
        elif ent.label_ == "DATE":
            entities["education"].append(ent.text)

    # Regex-based extras
    import re
    email_match = re.search(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text)
    phone_match = re.search(r"\b\d{10}\b", text)

    if email_match:
        entities["email"] = email_match.group()
    if phone_match:
        entities["phone"] = phone_match.group()

    # Match skills from a predefined list
    import json
    with open("skills.json") as f:
        skills_list = json.load(f)
    for skill in skills_list:
        if skill.lower() in text.lower():
            entities["skills"].append(skill)

    return entities
