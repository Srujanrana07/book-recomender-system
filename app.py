import pickle
import pandas as pd
import streamlit as st

def recommend(book):
    book_index = books[books['original_title'] == book].index[0]
    distances = similarity[book_index]
    book_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:7]  # Adjusted to get 6 recommendations

    recommended_books = []
    book_posters_name = [] 
    original_title_names =  []
    author_names = []
    publication = []
    language_code = []
    for i in book_list:
        recommended_books.append(books.iloc[i[0]]['original_title'])
        book_posters_name.append(books.iloc[i[0]]['image_url'])  
        original_title_names.append(books.iloc[i[0]]['title'])
        author_names.append(books.iloc[i[0]]['authors'])
        publication.append(books.iloc[i[0]]['original_publication_year'])
        language_code.append(books.iloc[i[0]]['language_code'])

    return recommended_books, book_posters_name, original_title_names, author_names, publication, language_code

# Load the model
book_list = pickle.load(open('books_dict.pkl', 'rb'))
books = pd.DataFrame(book_list)
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Book Recommender System')

selected_book_name = st.selectbox('Select a book:', books['original_title'])


col1, col2 = st.columns(2)

if st.button('Recommend'):
    recommendations, book_posters, titles, authors, years, languages = recommend(selected_book_name)

    for i in range(6):  
        if i % 2 == 0:  
            with col1:
                st.write(f"Book {i+1}: {recommendations[i]}")
                st.image(book_posters[i])
                st.write(f"Title: {titles[i]}")
                st.write(f"Publication Year: {years[i]}")
                st.info(f"Author: {authors[i]}")
                st.info(f"Language: {languages[i]}")
        else:  
            with col2:
                st.write(f"Book {i+1}: {recommendations[i]}")
                st.image(book_posters[i])
                st.write(f"Title: {titles[i]}")
                st.write(f"Publication Year: {years[i]}")
                st.info(f"Author: {authors[i]}")
                st.info(f"Language: {languages[i]}")
