import json
import streamlit as st
from recommend import df, recommend_movies
from utility import get_movie_details
from custom_recommend import recommend_by_answers

# ─── Config & Page Setup ─────────────────────────────────────────────────────
config = json.load(open("config.json"))
OMDB_API_KEY = config["OMDB_API_KEY"]

st.set_page_config(
    page_title="CineMatch",
    page_icon="🎥",
    layout="wide",
)

# ─── Load genre & keyword lists ───────────────────────────────────────────────
with open('genres_list.json', 'r', encoding='utf-8') as f:
    ALL_GENRES = json.load(f)
with open('keywords_list.json', 'r', encoding='utf-8') as f:
    ALL_KEYWORDS = json.load(f)

# ─── Helper to Render Recommendations ─────────────────────────────────────────
def display_recs(recs_df):
    for _, row in recs_df.iterrows():
        title = row['title']
        plot, poster = get_movie_details(title, OMDB_API_KEY)

        # two columns: poster (1/4), text (3/4)
        col1, col2 = st.columns([1, 3], gap="large")
        with col1:
            if poster and poster != "N/A":
                st.image(poster, use_container_width=True)
            else:
                st.info("No Poster")
        with col2:
            st.markdown(f"### {title}")
            st.write(plot or "_Plot unavailable_")

        st.markdown("---")

# ─── UI Styling ───────────────────────────────────────────────────────────────
st.markdown("""
    <style>
      .stButton>button { background-color: #1e90ff; color: white; border-radius:6px; }
      .stSelectbox>div, .stMultiselect>div, .stTextArea>div { border-radius:6px; }
      .stSidebar .stSelectbox > div, .stSidebar .stMultiselect > div { margin-bottom: 1rem; }
    </style>
""", unsafe_allow_html=True)

# ─── Sidebar Mode Selector ───────────────────────────────────────────────────
# st.sidebar.title("🍿 CineMatch")
mode = st.sidebar.radio("Choose mode", ("Custom Quiz", "Movie Search"))

# ─── Prepare Movie List for search ───────────────────────────────────────────
MOVIES = sorted(df['title'].dropna().unique())

# ─── Main Content ────────────────────────────────────────────────────────────
st.title("🎥 CineMatch")

if mode == "Custom Quiz":
    st.subheader("Tell us what kind of movie you like")

    # 1) Genre multiselect
    chosen_genres = st.multiselect(
        "Pick your favorite genres",
        ALL_GENRES
    )

    # 2) Keyword multiselect
    chosen_keywords = st.multiselect(
        "Pick themes/keywords you like",
        ALL_KEYWORDS
    )

    # 3) Tone/mood free-text
    tone = st.text_area(
        "Describe the tone or mood you want",
        placeholder="e.g. dark and suspenseful, lighthearted comedy..."
    )

    # 4) Recommend button
    if st.button("Find me movies"):
        if not (chosen_genres or chosen_keywords or tone.strip()):
            st.warning("Please select at least one genre, keyword, or describe the tone.")
        else:
            recs = recommend_by_answers(
                genres=chosen_genres,
                keywords=chosen_keywords,
                tone=tone,
                top_n=5
            )
            st.success(f"Here are movies matching your tastes:")
            display_recs(recs)

else:  # Movie Search path
    st.subheader("Pick a movie you already love")
    selected = st.selectbox("Select title:", MOVIES)
    if st.button("Recommend"):
        st.info(f"Movies similar to **{selected}**:")
        recs = recommend_movies(selected)
        display_recs(recs)
