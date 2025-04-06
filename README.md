# Spam Message Detector

This is a simple machine learning web app that detects whether a given message is spam or not.

## How it works

- The message is passed through a trained ML model.
- It uses a vectorizer and a classification algorithm.
- The model predicts whether the message is spam or not spam.

## Technologies Used

- Python
- Scikit-learn
- Streamlit
- Pickle (for saving the model and vectorizer)

## How to Use

1. Type your message in the input box.
2. Click on "Check if it's spam".
3. The app will show whether the message is spam or not.

## Demo

Try the app here:  
[Spam Message Detector App](https://spamdetector-svdtjij3qxsv974pxw8rtsg.streamlit.app)

## Files in this project

- `app.py` – Main Streamlit app
- `spam_model.pkl` – Trained ML model
- `vectorizer.pkl` – TF-IDF vectorizer
