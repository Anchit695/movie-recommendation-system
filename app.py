import streamlit as st
import pickle
import pandas as pd








def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movie_names = []


    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
print(movies.columns)
similarity =pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommendation System')

selected_movie_name = st.selectbox(
'How would you like to be contacted?',
movies['title'].values)

if st.button('Recommend'):
   names = recommend(selected_movie_name)

   col1, col2, col3, col4, col5 = st.columns(5)

   with col1:
       st.text(names[0])

   with col2:
       st.text(names[1])

   with col3:
       st.text(names[2])

   with col4:
       st.text(names[3])

   with col5:
       st.text(names[4])

