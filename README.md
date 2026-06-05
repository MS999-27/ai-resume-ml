# ai-resume-ml
🤖 AI Resume ML - Intelligent Resume Generator with NLP, ML &amp; LLM  Generate professional, ATS-friendly resumes powered by spaCy NLP, scikit-learn ML matching, and LLaMA 3 AI. Built with Streamlit, Groq API, and ReportLab.
---

## ✨ Features

- **🔍 NLP Text Analysis** – Extracts skills, entities, and keywords using spaCy
- **🤖 ML Job Matching** – TF-IDF vectorization + cosine similarity for optimal role matching
- **🧠 LLM Resume Generation** – LLaMA 3 AI generates compelling, ATS-friendly resume content
- **📄 Professional PDF Output** – ReportLab creates beautifully formatted PDF resumes
- **✉️ Cover Letter Generation** – Bonus feature to draft tailored cover letters
- **💡 Skill Gap Analysis** – Suggests missing skills for target job roles
- **🎨 Interactive Web UI** – Streamlit-based user-friendly interface

---

## 🏗️ Tech Stack

| Component | Technology |
|-----------|-----------|
| **Frontend** | Streamlit |
| **NLP Engine** | spaCy (en_core_web_sm), NLTK |
| **ML Matching** | scikit-learn (TF-IDF, Cosine Similarity) |
| **LLM** | Groq API (LLaMA 3.3 70B) |
| **PDF Generation** | ReportLab |
| **Language** | Python 3.8+ |

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip or conda
- Groq API key (free tier available at [groq.com](https://groq.com))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/ai-resume-ml.git
   cd ai-resume-ml
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download spaCy model**
   ```bash
   python -m spacy download en_core_web_sm
   ```

5. **Set up environment variables**
   ```bash
   cp .env.example .env
   ```
   Edit `.env` and add your Groq API key:
   ```
   GROQ_API_KEY=your_api_key_here
   ```

6. **Run the application**
   ```bash
   streamlit run app.py
   ```

   The app will open at `http://localhost:8501`

---

## 📋 How It Works

### 1️⃣ **User Input** (Streamlit UI)
   - Name, email, phone
   - Target job title & dream company
   - Education, work experience, skills

### 2️⃣ **NLP Analysis** (spaCy + NLTK)
   - Extracts named entities (organizations, dates, locations)
   - Tokenizes and filters stopwords
   - Matches skills against a database

### 3️⃣ **ML Job Matching** (scikit-learn)
   - Vectorizes job profiles using TF-IDF
   - Calculates cosine similarity with user skills
   - Ranks top 3 matching job roles with scores
   - Suggests missing skills for target role

### 4️⃣ **LLM Resume Generation** (Groq/LLaMA)
   - Sends user data + matched job to LLM
   - Generates 5 professional sections:
     - Professional Summary
     - Technical Skills
     - Work Experience
     - Education
     - Projects

### 5️⃣ **PDF Creation** (ReportLab)
   - Formats resume with custom styles
   - Applies professional color scheme
   - Outputs downloadable PDF

---

## 📁 Project Structure

```
ai-resume-ml/
├── app.py                    # Main Streamlit application
├── nlp_processor.py          # spaCy & NLTK NLP pipeline
├── skill_matcher.py          # TF-IDF + Cosine Similarity ML engine
├── resume_generator.py       # Groq LLaMA API integration
├── pdf_builder.py            # ReportLab PDF creation
├── requirements.txt          # Python dependencies
├── .env.example              # Environment variables template
├── .gitignore                # Git ignore file
└── README.md                 # This file
```

---

## 🔧 Configuration

### Job Profiles (Customizable)
Edit `skill_matcher.py` to add or modify job roles:

```python
JOB_PROFILES = {
    "Your Job Title": "skill1 skill2 skill3 ...",
}
```

### Skills Database
Modify `nlp_processor.py` to expand the skills list:

```python
SKILLS_DATABASE = [
    "python", "javascript", "docker", ...
]
```

### PDF Styling
Customize colors and fonts in `pdf_builder.py`:

```python
DARK = HexColor("#1a1a2e")
PURPLE = HexColor("#7c3aed")
```

---

## 📊 ML Model Details

### TF-IDF Vectorization
Converts text into numerical vectors for similarity comparison:
- **Vectorizer**: `sklearn.feature_extraction.text.TfidfVectorizer`
- **Corpus**: Job profile descriptions + user skills

### Cosine Similarity
Measures angle between vectors (0 = no match, 1 = perfect match):
```python
similarity = cos(angle) between user_vector and job_vectors
```

### NLP Pipeline
1. **Tokenization** – Split text into words (NLTK)
2. **Entity Extraction** – Identify names, orgs, dates (spaCy)
3. **Stopword Removal** – Filter common words (NLTK)
4. **Skill Matching** – Match against database

---

## 🎯 Example Usage

### Input
```
Name: Aryan Sharma
Skills: Python, Machine Learning, TensorFlow, Pandas, SQL
Target Job: Data Scientist
Company: Google
```

### Output
1. **NLP Results**: Extracts 5 skills, 0 organizations
2. **ML Matches**: 
   - Data Scientist (95.2% match)
   - ML Engineer (87.1% match)
   - Software Engineer (62.3% match)
3. **Missing Skills**: NumPy, Statistics, Tableau, Deep Learning
4. **Generated Resume**: 5-section resume
5. **PDF Download**: will generate resume.pdf

---

## 🧪 Testing

Run individual modules to test functionality:

```bash
# Test NLP processor
python nlp_processor.py

# Test skill matcher
python skill_matcher.py

# Test full pipeline (requires .env)
streamlit run app.py
```

---

## 🌐 Deployment

### Deploy on Streamlit Cloud
1. Push repo to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Click "Deploy an app" → select your repo
4. Add `GROQ_API_KEY` as a secret in app settings
5. Deploy!

### Deploy on Heroku
```bash
heroku create your-app-name
heroku config:set GROQ_API_KEY=your_key
git push heroku main
```

---

## 📝 Requirements

See `requirements.txt`:
```
streamlit>=1.28.0
python-dotenv>=1.0.0
spacy>=3.7.0
nltk>=3.8.1
scikit-learn>=1.3.0
groq>=0.4.0
reportlab>=4.0.4
```

Install with:
```bash
pip install -r requirements.txt
```

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** – see the LICENSE file for details.

---

## Acknowledgments

- **spaCy** – Industrial-strength NLP
- **scikit-learn** – Machine learning tools
- **Groq** – Fast LLM API (LLaMA 3)
- **ReportLab** – PDF generation
- **Streamlit** – Web app framework

---
## Output Images
<img width="1600" height="869" alt="PHOTO-2026-04-22-19-55-19" src="https://github.com/user-attachments/assets/53151728-65f0-4d63-9a84-72e9e07aebc3" />
<img width="1600" height="747" alt="PHOTO-2026-04-22-19-55-19 (1)" src="https://github.com/user-attachments/assets/9d61bd58-fc9b-4894-9924-e2c0574ed2b3" />
<img width="1600" height="782" alt="PHOTO-2026-04-22-19-55-19 (2)" src="https://github.com/user-attachments/assets/141d6e3b-0567-48d4-904f-a0462078733a" />
<img width="1600" height="1022" alt="PHOTO-2026-04-22-19-55-19 (3)" src="https://github.com/user-attachments/assets/b8591fc3-59bd-410d-a339-dd975d30903e" />
<img width="1160" height="742" alt="PHOTO-2026-04-22-19-55-18" src="https://github.com/user-attachments/assets/31cb95f6-7716-4ead-96c0-c2e30b28e413" />
<img width="1600" height="842" alt="PHOTO-2026-04-22-19-55-19 (4)" src="https://github.com/user-attachments/assets/94b50cef-afaa-4795-84ee-024bfb77edb2" />
<img width="1600" height="484" alt="PHOTO-2026-04-22-19-55-19 (5)" src="https://github.com/user-attachments/assets/1c925550-0916-47f8-9132-8450afcb6231" />
<img width="1600" height="1017" alt="PHOTO-2026-04-22-19-55-19 (6)" src="https://github.com/user-attachments/assets/3956e00a-35fc-4af9-874d-5661fab0d570" />
<img width="1600" height="990" alt="PHOTO-2026-04-22-19-55-19 (7)" src="https://github.com/user-attachments/assets/50ea83af-a191-41b3-b7ee-7df57a4af0c3" />




## 📧 Support & Contact

Have questions or found a bug? 
- Open an [Issue](https://github.com/MS999-27/ai-resume-ml/issues)
- Contact: (mailto:-muditasongara@gmail.com)

---

## 📊 Performance Metrics

- **NLP Processing**: ~500ms (spaCy entity extraction)
- **ML Matching**: ~100ms (TF-IDF + cosine similarity)
- **LLM Generation**: ~5-10s (Groq API response)
- **PDF Creation**: ~300ms (ReportLab rendering)
- **Total Time**: ~7-15 seconds per resume

---

## 🗺️ Roadmap

- [ ] Add more job profiles (100+ roles)
- [ ] Implement fine-tuned skill extraction model
- [ ] Multi-language support
- [ ] Resume templates (modern, classic, minimal)
- [ ] Analytics dashboard (skill trends, match insights)
- [ ] Batch resume generation
- [ ] Interview preparation guide generator

---

## ⭐ Show Your Support

If this project helped you, please give it a ⭐ on GitHub!

---


Status: Active Development
Last Updated: June 2026
