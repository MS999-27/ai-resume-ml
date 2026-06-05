import spacy
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Common tech skills list (ML-based matching)
SKILLS_DATABASE = [
    "python", "java", "javascript", "c++", "sql", "machine learning",
    "deep learning", "tensorflow", "pytorch", "scikit-learn", "pandas",
    "numpy", "react", "nodejs", "docker", "kubernetes", "aws", "git",
    "data analysis", "nlp", "computer vision", "excel", "tableau",
    "communication", "leadership", "teamwork", "problem solving"
]

def extract_entities(text):
    """
    Uses spaCy NLP to extract named entities from text
    (names, organizations, dates, locations)
    """
    doc = nlp(text)
    
    entities = {
        "names": [],
        "organizations": [],
        "dates": [],
        "locations": []
    }
    
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            entities["names"].append(ent.text)
        elif ent.label_ == "ORG":
            entities["organizations"].append(ent.text)
        elif ent.label_ == "DATE":
            entities["dates"].append(ent.text)
        elif ent.label_ in ["GPE", "LOC"]:
            entities["locations"].append(ent.text)
    
    return entities


def extract_skills(text):
    """
    Uses NLP tokenization + keyword matching to find skills
    This is an ML-based skill extraction technique
    """
    text_lower = text.lower()
    
    # Tokenize using NLTK
    tokens = word_tokenize(text_lower)
    stop_words = set(stopwords.words('english'))
    
    # Filter stopwords
    filtered_tokens = [w for w in tokens if w not in stop_words]
    
    # Match against skills database
    found_skills = []
    for skill in SKILLS_DATABASE:
        if skill in text_lower:
            found_skills.append(skill.title())
    
    return list(set(found_skills))


def analyze_text(raw_input):
    """
    Main function: runs full NLP pipeline on user input
    """
    print("🔍 Running NLP analysis with spaCy...")
    
    entities = extract_entities(raw_input)
    skills = extract_skills(raw_input)
    
    # Count word frequency (basic NLP technique)
    tokens = word_tokenize(raw_input.lower())
    stop_words = set(stopwords.words('english'))
    keywords = [w for w in tokens if w.isalpha() and w not in stop_words]
    
    return {
        "entities": entities,
        "extracted_skills": skills,
        "word_count": len(keywords)
    }


if __name__ == "__main__":
    # Test it
    sample = "John Doe worked at Google in New York as a Python developer using Machine Learning and TensorFlow from 2022 to 2024."
    result = analyze_text(sample)
    print("Entities:", result["entities"])
    print("Skills:", result["extracted_skills"])