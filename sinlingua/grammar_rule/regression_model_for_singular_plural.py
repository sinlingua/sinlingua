import os
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, mean_squared_error
from sinlingua.config import RESOURCE_PATH

file_path = 'IT20167264/word_set/singular_plural_train_data.text'
# Load data from text file
with open(os.path.join(RESOURCE_PATH, file_path), 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Assuming the first column contains the nouns and the second column contains the labels
nouns = []
labels = []
for line in lines:
    line = line.strip()
    columns = line.split(',')
    nouns.append(columns[0])
    labels.append(columns[1])

# Convert labels to numerical values (0 for singular, 1 for plural)
labels = [0 if label.lower() == 'singular' else 1 for label in labels]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(nouns, labels, test_size=0.11, random_state=42)

# Create a CountVectorizer to convert text into numerical features
vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Create a logistic regression model
model = LogisticRegression()

# Train the model
model.fit(X_train_vec, y_train)

# Predict on the test set
y_pred = model.predict(X_test_vec)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Create a table of predictions and actual values
results = pd.DataFrame({'Actual': y_test, 'Prediction': y_pred})

# Calculate the mean squared error
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

# Display the table of predictions and actual values
print(results)
print(y_test)
