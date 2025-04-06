from flask import Flask, render_template, request
import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

app = Flask(__name__)

# Load the model and vectorizer
model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    message = request.form['message']
    data = [message]
    vect = vectorizer.transform(data)
    prediction = model.predict(vect)
    result = "SPAM" if prediction[0] == 1 else "NOT SPAM"
    return render_template('index.html', prediction_text=result)

if __name__ == '__main__':
    app.run(debug=True)
