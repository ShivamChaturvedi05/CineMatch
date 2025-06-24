import pandas as pd
import re
import nltk
import joblib
import json
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download required NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Setup stopwords
stop_words = set(stopwords.words('english'))

# Function to clean text data
def clean_text(text):
    text = re.sub(r"[^a-zA-Z\s]", "", str(text))  # remove non-alphabetic characters
    text = text.lower()
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in stop_words]
    return " ".join(tokens)

# Load dataset
df = pd.read_csv("movies.csv")

# Use only required columns and drop rows with missing values
df = df[["genres", "keywords", "overview", "title"]].dropna().reset_index(drop=True)

# Combine important textual features for vectorization
df['combined'] = df['genres'] + ' ' + df['keywords'] + ' ' + df['overview']

# Apply cleaning to the combined text
df['cleaned_text'] = df['combined'].apply(clean_text)

# TF-IDF vectorization of the cleaned text
tfidf_vectorizer = TfidfVectorizer(max_features=5000)
tfidf_matrix = tfidf_vectorizer.fit_transform(df['cleaned_text'])

# Compute cosine similarity matrix for recommendations
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Extract unique genres for the quiz options
all_genres = sorted({genre.strip() for row in df['genres'] for genre in row.split(',') if genre.strip()})

# Extract unique keywords for the quiz options
all_keywords = sorted({kw.strip() for row in df['keywords'] for kw in row.split(',') if kw.strip()})

# Save processed data and models
joblib.dump(df, 'df_cleaned.pkl')
joblib.dump(tfidf_matrix, 'tfidf_matrix.pkl')
joblib.dump(cosine_sim, 'cosine_sim.pkl')
joblib.dump(tfidf_vectorizer, 'tfidf_vectorizer.pkl')

# Save genres and keywords for use in the quiz
with open('genres_list.json', 'w', encoding='utf-8') as f:
    json.dump(all_genres, f, indent=2)
with open('keywords_list.json', 'w', encoding='utf-8') as f:
    json.dump(all_keywords, f, indent=2)
