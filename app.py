import streamlit as st
import pandas as pd
import joblib
from sklearn.feature_extraction.text import CountVectorizer

# Load the trained model and vectorizer
model = joblib.load("spam_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

st.title("Spam Message Detector")

user_input = st.text_area("Enter your message:")

if st.button("Check if it's spam"):
    if user_input.strip() == "":
        st.warning("Please enter a message.")
    else:
        input_vector = vectorizer.transform([user_input])
        prediction = model.predict(input_vector)

        if prediction[0] == 1:
            st.error("This is a Spam message!")
        else:
            st.success("This is NOT a Spam message.")
