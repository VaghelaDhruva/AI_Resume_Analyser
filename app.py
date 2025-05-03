import streamlit as st
import time
from extract_text import extract_text_from_pdf
from nlp_parser import extract_entities
from scorer import score_resume, generate_feedback, get_score_reason, get_resume_summary, generate_detailed_summary

st.set_page_config(page_title="AI Resume Analyzer", page_icon="🤖", layout="centered")

# --- Custom Styling ---
st.markdown("""
<style>
    html, body {
        background: linear-gradient(to right, #0f172a, #1e293b);
        color: #e2e8f0;
        font-family: 'Segoe UI', sans-serif;
    }
    .hero-container {
        background: linear-gradient(to right, #8b5cf6, #3b0764);
        text-align: center;
        padding: 3.5rem 2rem;
        border-radius: 2rem;
        margin-top: -3rem;
        margin-bottom: 2.5rem;
        box-shadow: 0 15px 40px rgba(0,0,0,0.35);
        animation: fadeIn 1s ease-out;
    }
    .hero-title {
        font-size: 3.2rem;
        font-weight: 800;
        color: white;
    }
    .hero-highlight {
        color: #facc15;
        text-shadow: 0px 0px 6px #fde68a;
    }
    .hero-tagline {
        font-size: 1.25rem;
        color: #f3f4f6;
        margin-top: 1rem;
    }
    .score-display {
        font-size: 3.5rem;
        font-weight: 900;
        color: #facc15;
        text-align: center;
        margin: 2rem 0;
        animation: popIn 1s ease-in-out;
        text-shadow: 0px 0px 10px #fef3c7;
    }
    .chat-box {
        background-color: #1f2937;
        padding: 1rem;
        border-radius: 0.75rem;
        margin: 0.5rem 0;
        font-size: 1rem;
        color: #e0e7ff;
        border-left: 5px solid #8b5cf6;
    }
    .section-title {
        font-size: 1.5rem;
        font-weight: 700;
        color: #c084fc;
        margin: 1.5rem 0 1rem;
    }
    .divider {
        border-top: 1px solid #334155;
        margin: 2.5rem 0;
    }
    .stButton>button {
        background-color: #8b5cf6;
        color: white;
        font-weight: bold;
        padding: 0.65rem 1.2rem;
        border: none;
        border-radius: 0.5rem;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #a78bfa;
        box-shadow: 0 0 10px #c4b5fd;
    }
    @keyframes fadeIn {
        from {opacity: 0;}
        to {opacity: 1;}
    }
    @keyframes popIn {
        0% {transform: scale(0.6); opacity: 0;}
        100% {transform: scale(1); opacity: 1;}
    }
</style>
""", unsafe_allow_html=True)

# --- Hero Section ---
st.markdown("""
<div class="hero-container">
    <div class="hero-title">Analyze Your Resume with <span class="hero-highlight">AI Precision</span></div>
    <div class="hero-tagline">Upload your resume and get instant insights, feedback, and scoring.</div>
</div>
""",unsafe_allow_html=True)

uploaded_file = st.file_uploader("📄 Upload your resume (PDF only)", type=["pdf"])

st.markdown("<div class='divider'></div>", unsafe_allow_html=True)



# --- Resume Processing ---
if uploaded_file:
    with st.spinner("🔍 Analyzing your resume..."):
        time.sleep(1)
        text = extract_text_from_pdf(uploaded_file)
        entities = extract_entities(text)
        score = score_resume(entities)
        feedback = generate_feedback(entities)
        score_reason = get_score_reason(score, entities)
        conclusion = get_resume_summary(score, feedback)

    st.markdown("## 📊 Resume Score")
    st.markdown(f"<div class='score-display'>{score} / 10</div>", unsafe_allow_html=True)
    st.markdown("This score reflects your resume’s strength based on structure, content, and keyword presence.")

    st.markdown("### 🧐 Why this Score?")
    if score >= 8:
        st.success(" Excellent formatting, clarity, and keyword usage. Great job!")
    elif 5 <= score < 8:
        st.warning("Decent resume but could use improvements in formatting and focus.")
    else:
        st.error(" Your resume lacks structure, clarity, and key information. Let’s fix that!")

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    if st.button("💬 Get Feedback"):
        st.markdown("<div class='section-title'>💡 Suggestions:</div>", unsafe_allow_html=True)
        for fb in feedback:
            with st.spinner("Thinking..."):
                time.sleep(0.6)
                st.markdown(f"<div class='chat-box'>🔹 {fb}</div>", unsafe_allow_html=True)

        st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

        st.markdown("<div class='section-title'>🧾 Resume Conclusion</div>", unsafe_allow_html=True)
        summary = generate_detailed_summary(score, feedback)
        st.info(summary.split("\n\n")[0])

        st.markdown("<div class='section-title'>📃 Detailed Summary</div>", unsafe_allow_html=True)
        st.text(summary)
else:
    st.info("👆 Upload your resume above to begin.")

# --- Why Choose Us Section ---
st.markdown("## 💡 Why Choose Our AI Resume Analyzer?")
st.markdown("""
<div style='display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem;'>
    <div class='chat-box'><strong>🎯 Tailored Scoring</strong><br>Your resume score is based on real alignment to job descriptions.</div>
    <div class='chat-box'><strong>🧠 Multiple AI Perspectives</strong><br>Balanced feedback from multiple AI models.</div>
    <div class='chat-box'><strong>🚀 Innovation-Driven</strong><br>Powered by OpenAI & Anthropic models for cutting-edge insight.</div>
    <div class='chat-box'><strong>📈 Multiple Lenses</strong><br>View your resume's strengths and weaknesses with clarity.</div>
</div>
""", unsafe_allow_html=True)

# --- Features Section ---
st.markdown("## 🚀 Features at a Glance")
st.markdown("""
<div style='display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem;'>
    <div class='chat-box'><strong>📝 Smart Resume Analysis</strong><br>- ATS optimization<br>- Gap identification</div>
    <div class='chat-box'><strong>🔍 Deep Insights</strong><br>- Readability<br>- Achievement metrics</div>
    <div class='chat-box'><strong>🛠️ Actionable Tips</strong><br>- Word usage<br>- Formatting tweaks</div>
</div>
""", unsafe_allow_html=True)

# --- Testimonials ---
st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
st.markdown("## 📣 What People Are Saying")
st.markdown("""
<div style='display: flex; flex-wrap: wrap; gap: 1.2rem;'>
    <div class='chat-box' style='flex:1; min-width: 260px;'>“It’s a solid comparison and assessment tool”<br><small>📱 Brian, TikTok</small></div>
    <div class='chat-box' style='flex:1; min-width: 260px;'>“Incredible idea/execution — lots of folks can benefit!”<br><small>💼 Lou, LinkedIn</small></div>
    <div class='chat-box' style='flex:1; min-width: 260px;'>“This doesn’t feel like just AI recap — it’s thoughtful.”<br><small>📱 Tapon, TikTok</small></div>
</div>
""", unsafe_allow_html=True)