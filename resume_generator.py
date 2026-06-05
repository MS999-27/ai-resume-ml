from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def generate_resume_text(user_data: dict, matched_job: str) -> str:
    """
    Uses LLM (Groq/LLaMA) to generate professional resume content
    based on extracted NLP data and ML-matched job role.
    """
    
    prompt = f"""
You are an expert resume writer with 20 years of experience.

Write a complete professional resume for this person:

Name: {user_data.get('name', 'N/A')}
Email: {user_data.get('email', 'N/A')}
Phone: {user_data.get('phone', 'N/A')}
Target Job Title: {matched_job}
Education: {user_data.get('education', 'N/A')}
Work Experience: {user_data.get('experience', 'N/A')}
Detected Skills: {', '.join(user_data.get('skills', []))}

Write the resume with these sections:
1. PROFESSIONAL SUMMARY - 3-4 powerful sentences tailored to {matched_job}
2. TECHNICAL SKILLS - organized by category
3. WORK EXPERIENCE - with strong action verbs and achievements
4. EDUCATION - formatted properly
5. PROJECTS (if applicable)

Make it ATS-friendly, use numbers/metrics where possible, and make it impressive.
Format it cleanly with clear section headers using === markers.
"""
    
    print("🧠 Generating resume with LLM (LLaMA 3 via Groq)...")
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",   # Free LLaMA 3 model
        messages=[
            {"role": "system", "content": "You are a professional resume writer. Write clean, impressive resumes."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=2000,
        temperature=0.7
    )
    
    return response.choices[0].message.content


def generate_cover_letter(user_data: dict, job_title: str, company: str = "the company") -> str:
    """
    Bonus: generates a cover letter using LLM
    """
    prompt = f"""
Write a professional cover letter for:
- Applicant: {user_data.get('name')}
- Position: {job_title}
- Company: {company}
- Skills: {', '.join(user_data.get('skills', []))}
- Experience: {user_data.get('experience', '')}

Keep it to 3 paragraphs. Make it enthusiastic, specific, and professional.
"""
    
    response = client.chat.completions.create(
       model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=800
    )
    
    return response.choices[0].message.content