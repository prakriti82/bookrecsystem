import pickle
import streamlit as st 
import numpy as np
import scipy


st.header("Book Recommender System using Machine Learning")
model=pickle.load(open('artifacts/model.pkl','rb'))
books_name=pickle.load(open('artifacts/books_name.pkl','rb'))
final_rating=pickle.load(open('artifacts/final_rating.pkl','rb'))
book_pivot=pickle.load(open('artifacts/book_pivot.pkl','rb'))

selected_books=st.selectbox(
  "type or select a book",
  books_name
)