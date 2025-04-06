import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Load CSV file
data = pd.read_csv("spam.csv")
data.columns = ['label', 'message']
data['label'] = data['label'].map({'ham': 0, 'spam': 1})

# Split data
X_train, X_test, y_train, y_test = train_test_split(data['message'], data['label'], test_size=0.2)

# Convert text to numbers
vectorizer = CountVectorizer()
X_train_vector = vectorizer.fit_transform(X_train)
X_test_vector = vectorizer.transform(X_test)

# Train model
model = MultinomialNB()
model.fit(X_train_vector, y_train)

# Test model
y_pred = model.predict(X_test_vector)
print("Accuracy:", accuracy_score(y_test, y_pred))

# Try a new message
msg = ["You have won $1000 cash prize!"]
msg_vector = vectorizer.transform(msg)
print("Prediction (1 = Spam, 0 = Not Spam):", model.predict(msg_vector))
