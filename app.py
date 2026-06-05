import streamlit as st
import os
from dotenv import load_dotenv

from nlp_processor import analyze_text, extract_skills
from skill_matcher import match_job_roles, suggest_missing_skills
from resume_generator import generate_resume_text, generate_cover_letter
from pdf_builder import build_pdf

load_dotenv()

# ─── Page Config ───────────────────────────────────────
st.set_page_config(
    page_title="AI Resume Generator",
    page_icon="🤖",
    layout="wide"
)

# ─── Custom CSS ────────────────────────────────────────
st.markdown("""
<style>
    .main { background-color: #0f0f1a; }
    h1 { color: #c084fc !important; font-size: 2.5rem !important; }
    h2, h3 { color: #818cf8 !important; }
    .stButton > button {
        background: linear-gradient(135deg, #7c3aed, #4f46e5);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.6rem 2rem;
        font-size: 1rem;
        font-weight: 600;
        width: 100%;
    }
    .metric-card {
        background: #1a1a2e;
        padding: 15px;
        border-radius: 10px;
        border-left: 4px solid #c084fc;
        margin: 5px 0;
    }
</style>
""", unsafe_allow_html=True)

# ─── Header ────────────────────────────────────────────
st.title("🤖 AI Resume Generator")
st.markdown("*Powered by spaCy NLP · scikit-learn ML · LLaMA 3 LLM · ReportLab PDF*")
st.divider()

# ─── Input Form ────────────────────────────────────────
col1, col2 = st.columns(2)

with col1:
    st.subheader("👤 Personal Info")
    name = st.text_input("Full Name", placeholder="e.g. Aryan Sharma")
    email = st.text_input("Email", placeholder="aryan@email.com")
    phone = st.text_input("Phone", placeholder="+91 9876543210")

with col2:
    st.subheader("🎯 Career Info")
    target_job = st.text_input("Target Job Title", placeholder="e.g. Data Scientist")
    company = st.text_input("Dream Company (for cover letter)", placeholder="e.g. Google")
    generate_cover = st.checkbox("Also generate Cover Letter")

st.subheader("📚 Background")
col3, col4 = st.columns(2)

with col3:
    education = st.text_area(
        "Education",
        placeholder="B.Tech in Computer Science, ABC University, 2021-2025\nRelevant courses: ML, AI, Data Structures",
        height=120
    )

with col4:
    experience = st.text_area(
        "Work Experience / Projects",
        placeholder="ML Intern at XYZ Corp (2024)\n- Built a sentiment analysis model with 92% accuracy\n- Used Python, TensorFlow, and scikit-learn",
        height=120
    )

skills_input = st.text_input(
    "Your Skills (comma separated)",
    placeholder="Python, Machine Learning, TensorFlow, SQL, Data Analysis, Communication"
)

# ─── Generate Button ───────────────────────────────────
if st.button("🚀 Generate AI Resume"):
    
    if not name or not email or not skills_input:
        st.error("Please fill in at least: Name, Email, and Skills!")
    else:
        # Combine all text for NLP analysis
        full_text = f"{name} {experience} {education} {skills_input}"
        
        # ── Step 1: NLP Analysis ──────────────────────
        with st.spinner("🔍 Step 1/4: Running NLP analysis with spaCy..."):
            nlp_result = analyze_text(full_text)
            user_skills = skills_input.split(",")
            user_skills = [s.strip() for s in user_skills]
        
        st.success(f"✅ NLP Done — Found {len(nlp_result['extracted_skills'])} skills in your text")
        
        # ── Step 2: ML Job Matching ───────────────────
        with st.spinner("🤖 Step 2/4: Running ML skill matching (TF-IDF + Cosine Similarity)..."):
            matches = match_job_roles(user_skills)
            best_match = matches[0]["job_title"] if not target_job else target_job
        
        # Show ML results
        st.subheader("📊 ML Analysis Results")
        cols = st.columns(3)
        for i, match in enumerate(matches):
            with cols[i]:
                st.markdown(f"""
                <div class="metric-card">
                    <strong>{match['job_title']}</strong><br>
                    Match Score: <b>{match['match_score']}%</b>
                </div>
                """, unsafe_allow_html=True)
        
        # Missing skills
        missing = suggest_missing_skills(user_skills, best_match)
        if missing:
            st.info(f"💡 Skills to add for **{best_match}**: {', '.join(missing)}")
        
        # NLP Entities
        entities = nlp_result["entities"]
        if entities["organizations"]:
            st.info(f"🏢 Organizations detected by spaCy: {', '.join(entities['organizations'][:3])}")
        
        # ── Step 3: LLM Resume Generation ────────────
        with st.spinner("🧠 Step 3/4: Generating resume with LLaMA 3 AI..."):
            user_data = {
                "name": name, "email": email, "phone": phone,
                "education": education, "experience": experience,
                "skills": user_skills
            }
            resume_text = generate_resume_text(user_data, best_match)
        
        # ── Step 4: PDF Creation ──────────────────────
        with st.spinner("📄 Step 4/4: Building PDF with ReportLab..."):
            pdf_path = f"{name.replace(' ', '_')}_resume.pdf"
            build_pdf(resume_text, name, pdf_path)
        
        # ── Show Results ──────────────────────────────
        st.success("🎉 Resume Generated Successfully!")
        st.divider()
        
        st.subheader("📄 Your AI-Generated Resume")
        st.text_area("Resume Content", resume_text, height=500)
        
        # Download PDF
        with open(pdf_path, "rb") as f:
            st.download_button(
                label="⬇️ Download Resume as PDF",
                data=f,
                file_name=pdf_path,
                mime="application/pdf"
            )
        
        # Cover Letter
        if generate_cover:
            with st.spinner("✉️ Generating cover letter..."):
                cover = generate_cover_letter(user_data, best_match, company)
            st.subheader("✉️ Cover Letter")
            st.text_area("Cover Letter", cover, height=300)
        
        st.balloons()