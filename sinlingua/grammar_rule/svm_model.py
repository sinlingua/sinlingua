import os
import numpy as np
from sklearn.svm import SVC
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
import pickle
from sinlingua.config import RESOURCE_PATH

# Load the dataset
data_file = 'IT20167264/word_set/singular_plural_train_data.text'
data = np.loadtxt(os.path.join(RESOURCE_PATH, data_file), delimiter=',', dtype=str, encoding='utf-8')

# Split the dataset into input features and labels
X = data[:, 0]  # Sinhala nouns
y = data[:, 1]  # Singular or Plural labels

# Convert labels to numeric values: Singular -> 0, Plural -> 1
y = np.where(y == 'Singular', 0, 1)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.11, random_state=42)

# Feature extraction
vectorizer = CountVectorizer()
X_train_features = vectorizer.fit_transform(X_train)
X_test_features = vectorizer.transform(X_test)

# Train the SVM model
svm_model = SVC(kernel='linear')
svm_model.fit(X_train_features, y_train)

# Evaluate the model
accuracy = svm_model.score(X_test_features, y_test)
print(f"Accuracy: {accuracy}")

# Make predictions on new data
# new_data = ["අය", "හෙසිනි"]
# new_data_features = vectorizer.transform(new_data)
# predictions = svm_model.predict(new_data_features)

# Print the predictions
# for noun, prediction in zip(new_data, predictions):
# label = "Singular" if prediction == 0 else "Plural"
# print(f"Noun: {noun} - Prediction: {label}")

# Serialize and save the object as a pickle file
dict = {"model": svm_model, "vectorizer": vectorizer}
with open('../../resources/pickels/svm_singular_plural.pkl', 'wb') as file:
    pickle.dump(dict, file)

print("Python object converted to a pickle file.")



