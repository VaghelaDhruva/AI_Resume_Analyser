# def score_resume(entities):
#     score = 0
#     if entities["skills"]: score += 4
#     if entities["education"]: score += 3
#     if entities["experience"]: score += 3
#     return score

# def generate_feedback(entities):
#     feedback = []
#     if not entities["skills"]:
#         feedback.append("Add more relevant skills.")
#     if not entities["education"]:
#         feedback.append("Mention your education details.")
#     if not entities["experience"]:
#         feedback.append("Include your work/project experience.")
#     return feedback

def score_resume(entities):
    score = 0
    weights = {
        "name": 1,
        "email": 1,
        "phone": 1,
        "skills": 3,
        "education": 2,
        "experience": 3,
        "certifications": 1,
        "projects": 2,
    }

    for key, weight in weights.items():
        if entities.get(key):
            if isinstance(entities[key], list):
                score += min(len(entities[key]), 5) * weight  # cap large lists
            else:
                score += weight

    max_score = sum(weights.values()) * 5
    return round((score / max_score) * 10, 2)  # return score out of 10


def generate_feedback(entities):
    feedback = []

    if not entities.get("skills"):
        feedback.append("Add relevant technical and soft skills.")
    if not entities.get("projects"):
        feedback.append("Include 1-2 significant academic or personal projects.")
    if not entities.get("certifications"):
        feedback.append("Add certifications from platforms like Coursera or Udemy.")
    if not entities.get("experience"):
        feedback.append("Include internships or work experience, if available.")
    if not entities.get("education"):
        feedback.append("Education section is incomplete or missing.")
    if not entities.get("phone") or not entities.get("email"):
        feedback.append("Contact info (phone/email) is missing or incorrect.")
    if not entities.get("name"):
        feedback.append("Add your name at the top of your resume.")
    
    if not feedback:
        feedback.append("Your resume looks solid! Consider tailoring it for each job.")

    return feedback

def get_score_reason(score, entities):
    if score >= 8:
        return "Your resume is strong, well-structured, and includes most of the important details such as skills, education, and experience."
    elif score >= 5:
        return "Your resume covers some key areas, but it lacks completeness or proper formatting in certain sections like experience or summary."
    else:
        return "Your resume is missing many crucial sections or keywords. It may not be ATS-friendly or role-specific."

def get_resume_summary(score, feedback):
    if score >= 8:
        return "Excellent resume. With a few minor tweaks, you're ready to apply!"
    elif score >= 5:
        return "Good start, but there’s room for improvement. Focus on structure, clarity, and adding more achievements."
    else:
        return "Resume needs major improvements. Start by adding a summary, relevant experience, and proper formatting."
def generate_detailed_summary(score, feedback):
    summary = ""

    if score >= 8:
        summary += "Your resume is excellent and aligns well with industry standards. It demonstrates strong presentation, includes essential sections like skills, experience, and education, and likely performs well in Applicant Tracking Systems (ATS).\n\n"
    elif 5 <= score < 8:
        summary += "Your resume is on the right path but requires moderate improvement. While it includes important information, it may lack clarity, keyword optimization, or polish in some sections such as achievements, summary statement, or formatting.\n\n"
    else:
        summary += "Your resume needs major enhancements. It may be missing critical sections, use poor formatting, or lack industry-relevant keywords, making it less likely to pass through ATS or impress recruiters.\n\n"

    summary += " Key Observations:\n"
    for point in feedback[:5]:
        summary += f"• {point}\n"

    summary += "\n  Next Steps:\n"
    summary += "- Prioritize adding measurable achievements to your experience.\n"
    summary += "- Include a professional summary and relevant skills.\n"
    summary += "- Use job-related keywords to increase ATS ranking.\n"
    summary += "- Maintain clean formatting with clear section headings.\n"

    return summary
