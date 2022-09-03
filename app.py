import pickle
import streamlit as st
import requests


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(
        movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    namesMovie = []
    posters = []
    for i in distances[1:13]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        posters.append(fetch_poster(movie_id))
        namesMovie.append(movies.iloc[i[0]].title)

    return namesMovie, posters


st.header('Movie Recommender System')
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])
    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col1:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
    with col2:
        st.text(recommended_movie_names[5])
        st.image(recommended_movie_posters[5])
    with col3:
        st.text(recommended_movie_names[6])
        st.image(recommended_movie_posters[6])
    with col4:
        st.text(recommended_movie_names[7])
        st.image(recommended_movie_posters[7])
    with col1:
        st.text(recommended_movie_names[8])
        st.image(recommended_movie_posters[8])
    with col2:
        st.text(recommended_movie_names[9])
        st.image(recommended_movie_posters[9])
    with col3:
        st.text(recommended_movie_names[10])
        st.image(recommended_movie_posters[10])
    with col4:
        st.text(recommended_movie_names[11])
        st.image(recommended_movie_posters[11])
