import joblib
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# load your precomputed objects
df           = joblib.load('df_cleaned.pkl')
tfidf_matrix = joblib.load('tfidf_matrix.pkl')
vectorizer   = joblib.load('tfidf_vectorizer.pkl')

def recommend_by_answers(genres: list[str],
                         keywords: list[str],
                         tone: str,
                         top_n: int = 5) -> pd.DataFrame:
    query = " ".join(genres + keywords) + " " + tone
    q_vec = vectorizer.transform([query])
    sims  = cosine_similarity(q_vec, tfidf_matrix).flatten()
    top_idx = np.argsort(sims)[::-1][1: top_n+1]
    return df.iloc[top_idx].reset_index(drop=True)
