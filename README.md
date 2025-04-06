# Spam Message Detector

This project is a web application that uses a machine learning model to detect whether a given message is spam or not.

## Live Demo
[Click here to try the app](https://share.streamlit.io/your-link-here)

## How It Works
- The model was trained on a dataset of SMS messages.
- It uses a TF-IDF Vectorizer and a Naive Bayes classifier.
- The frontend is built with Streamlit.

## Files in this Repo
- `app.py` – Streamlit web app code.
- `spam_model.pkl` – Trained ML model.
- `vectorizer.pkl` – Text vectorizer used for preprocessing.
- `requirements.txt` – List of libraries needed to run the app.

## Running Locally
```bash
pip install -r requirements.txt
streamlit run app.py
