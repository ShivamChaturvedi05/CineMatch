
---

# 🎥 CineMatch — Intelligent Movie Recommender

CineMatch is a personalized movie recommendation system that helps users discover new films based on their favorite genres, themes, mood, or a movie they already love. Powered by Machine Learning and an intuitive Streamlit web interface, CineMatch bridges the gap between user preferences and meaningful cinema recommendations.

---

## 🚀 Features

✨ **Two Ways to Get Recommendations**:

1. 🎯 **Custom Quiz-Based Recommendations**

   * Choose your favorite **genres**, select **themes/keywords**, or describe the **tone/mood** of the movie you want.
   * CineMatch intelligently suggests movies **matching your preferences**.

2. 🎬 **Direct Movie-Based Recommendations**

   * Already love a movie? Simply select it, and get **similar movies** recommended instantly.

---

💡 **Powered by Machine Learning**:

* 🧠 **Text Similarity Engine**
  Uses **TF-IDF vectorization** and **cosine similarity** on movie metadata (genres, keywords, overview) to find movies with **semantic relevance**.

---

🎨 **Rich Movie Experience**:

* 🖼️ **Posters & Full Plots**
  Integrated with the **OMDb API** to display **high-quality posters** and **movie summaries**.

---

⚡ **Fast, Interactive, and Easy to Use**:

* Built with **Streamlit** to provide a **responsive**, **modern**, and **interactive** user interface.

---

## ⚙️ Tech Stack

| Layer        | Technology                                                      |
| ------------ | --------------------------------------------------------------- |
| Frontend     | Streamlit (Python)                                              |
| Backend      | Scikit-learn, Pandas, NLTK                                      |
| ML           | TF-IDF + Cosine Similarity                                      |
| External API | OMDb API ([https://www.omdbapi.com/](https://www.omdbapi.com/)) |

## 🏁 How to Run

1️⃣ **Install Dependencies**

```bash
pip install -r requirements.txt
```

2️⃣ **Preprocess Dataset (First Time Only)**

```bash
python preprocess.py
```

3️⃣ **Run the App**

```bash
streamlit run main.py
```

4️⃣ **Visit in Browser**
Default URL: `http://localhost:8501`

## 🗝️ OMDb API Setup

1. Sign up for a free OMDb API key: [https://www.omdbapi.com/apikey.aspx](https://www.omdbapi.com/apikey.aspx)
2. Create a `config.json`:

```json
{
  "OMDB_API_KEY": "your_api_key_here"
}


Built with ❤️ by Shivam Chaturvedi


