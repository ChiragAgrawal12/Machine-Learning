import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, precision_score, recall_score, classification_report

# Sample dataset (replace with actual data)
data = {
    'text': [
        'I love programming in Python',
        'Java is a very popular programming language',
        'Python is great for data science',
        'Machine learning is fun',
        'Java is used for enterprise applications',
        'Deep learning is a subset of machine learning',
        'Python and Java are both powerful languages',
        'I prefer Python over Java',
        'Programming in Python is easy',
        'Java is object-oriented'
    ],
    'label': ['python', 'java', 'python', 'ml', 'java', 'ml', 'both', 'python', 'python', 'java']
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    df['text'], df['label'], test_size=0.2, random_state=42
)

# Convert text to numerical format using TF-IDF
vectorizer = TfidfVectorizer()
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Train Naive Bayes Classifier
model = MultinomialNB()
model.fit(X_train_tfidf, y_train)

# Predict on test set
y_pred = model.predict(X_test_tfidf)

# Calculate metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')

# Display results
print("=== Classification Report ===")
print(classification_report(y_test, y_pred))
print(f"Accuracy: {accuracy:.2f}")
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
