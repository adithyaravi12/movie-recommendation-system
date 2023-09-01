import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

data = pd.read_csv("encoded_netflix.csv")
tfidf_vec = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vec.fit_transform(data['description'])
cosine_similarity = linear_kernel(tfidf_matrix, tfidf_matrix)

st.set_page_config(
    page_title="Movie/TV Series Recommender",
    page_icon="🎬"
)

page_bg = """
<style>
[data-testid="stAppViewContainer"]{
    background-image: url("https://images.unsplash.com/photo-1535016120720-40c646be5580?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1770&q=80");
    background-size: cover;
    # position: relative;
}
</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

def recommendations(title):
    filtered_data = data[data['title'] == title]
    if not filtered_data.empty:
        index = filtered_data.index[0]
        similarity_score = list(enumerate(cosine_similarity[index]))
        similarity_score = sorted(similarity_score, key=lambda x: x[1], reverse=True)
        similarity_score = similarity_score[1:4]
        show_index = [i[0] for i in similarity_score]
        rec = data['title'].iloc[show_index].values
        return rec
    else:
        return []

st.title('Movie/TV Series Recommender')



# User input
title_input = st.text_input('Enter a movie/TV series title')

if st.button('Recommend'):
    if title_input:
        recommendations_list = recommendations(title_input)
        if len(recommendations_list) > 0:  # Check the length of the array
            st.write(f'Recommendations for {title_input}:')
            for rec in recommendations_list:
                st.write(rec)
        else:
            st.write(f'No recommendations found for {title_input}.')
    else:
        st.write('Please enter a title to get recommendations.')

st.markdown(
    """
    <style>
    .center-bottom {
        position: fixed;
        bottom: 0;
        left: 50%;
        transform: translateX(-50%);
        text-align: center;
        width: 100%;
        padding: 10px;
    }
    footer a {
        text-decoration: none;
        color: #333;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <div class='center-bottom'>
        <a href="https://github.com/adithyaravi12" target="_blank">GitHub</a> |
        <a href="https://www.linkedin.com/in/adithyaravi12/" target="_blank">LinkedIn</a>
    </div>
    """,
    unsafe_allow_html=True
)