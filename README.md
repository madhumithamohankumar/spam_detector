# 📩 Spam Message Detector

This project is a simple web application that uses machine learning to detect whether a given message is **spam** or **not spam**.

## 🚀 Live Demo
[Click here to try the app](https://share.streamlit.io/)  
_(Replace this link with your actual Streamlit share link if you have one)_

---

## 🧠 How It Works

- The model is trained on a dataset of SMS messages.
- It uses:
  - **TF-IDF Vectorizer** to convert text to numerical features.
  - **Naive Bayes Classifier** for spam detection.
- The app is built using **Streamlit** for a simple web interface.

---

## 📁 Files in this Repository

| File Name         | Description                                 |
|------------------|---------------------------------------------|
| `app.py`         | Main Streamlit app code                     |
| `spam_model.pkl` | Trained machine learning model              |
| `vectorizer.pkl` | TF-IDF vectorizer used during training      |
| `requirements.txt` | List of required Python libraries         |

---

## 💻 Running the Project Locally

To run this app on your local machine:

```bash
# Install required libraries
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
