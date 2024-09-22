import streamlit as st
import pickle

def recommend(movie):
    movie = movie.lower()
    moive_index = movies[movies['title'] == movie].index[0]
    distance = similarity[moive_index]
    movie_lists = sorted(list(enumerate(distance)),reverse=True,key = lambda x:x[1])[1:6]
    recommended_movies = []
    for i in movie_lists:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

movies = pickle.load(open('movies.pkl','rb'))

st.title(movies['movie_id'])
movies_list= movies['title'].values
similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')
selected_movie_name = st.selectbox(
'Select Your movies',
    movies_list
)

if st.button('Recommend'):
    re = recommend(selected_movie_name)

    st.write(selected_movie_name)
    st.write("Good Movie Here is the recommended one")
    for i in re:
        st.write(i)